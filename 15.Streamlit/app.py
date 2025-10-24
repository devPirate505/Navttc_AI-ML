import os
import numpy as np
import pandas as pd
import streamlit as st
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Bank Churn Predictor", layout="wide")
st.title("🏦 Bank Churn Prediction App")

# Model path
MODEL_PATH = os.path.join(os.path.dirname(__file__), "churn_model.h5")

# Load model
@st.cache_resource
def load_trained_model():
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model not found at {MODEL_PATH}")
        st.stop()
    return load_model(MODEL_PATH)

model = load_trained_model()
st.sidebar.success("✅ Model loaded successfully!")

# Feature columns (same order as training)
FEATURE_COLUMNS = [
    'CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
    'HasCrCard', 'IsActiveMember', 'EstimatedSalary',
    'Geography_Germany', 'Geography_Spain', 'Gender_Male'
]

st.sidebar.header("📊 Model Info")
st.sidebar.write(f"Input features: {len(FEATURE_COLUMNS)}")
st.sidebar.write("Task: Binary Classification")
st.sidebar.write("Output: Churn Probability")

# Main content
st.subheader("Enter Customer Information")

col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    tenure = st.number_input("Tenure (years)", min_value=0, max_value=10, value=5)
    balance = st.number_input("Balance", min_value=0.0, value=50000.0)
    num_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)

with col2:
    has_credit_card = st.selectbox("Has Credit Card", [0, 1], index=1)
    is_active = st.selectbox("Is Active Member", [0, 1], index=1)
    salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Female", "Male"])

if st.button("Predict Churn", type="primary"):
    # Prepare input data
    input_data = pd.DataFrame({
        'CreditScore': [credit_score],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'NumOfProducts': [num_products],
        'HasCrCard': [has_credit_card],
        'IsActiveMember': [is_active],
        'EstimatedSalary': [salary],
        'Geography_Germany': [1 if geography == 'Germany' else 0],
        'Geography_Spain': [1 if geography == 'Spain' else 0],
        'Gender_Male': [1 if gender == 'Male' else 0]
    })
    
    scaler = StandardScaler()
    input_scaled = scaler.fit_transform(input_data)
    
    # Make prediction
    prediction_prob = model.predict(input_scaled, verbose=0)[0][0]
    prediction = 1 if prediction_prob > 0.5 else 0
    
    # Display result
    st.divider()
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Prediction", prediction)
    with col_b:
        churn_status = "Will Stay" if prediction == 1 else "Will Churn"
        st.metric("Status", churn_status)

st.divider()
