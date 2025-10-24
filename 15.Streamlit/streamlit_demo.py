
# # Basic webpage

# import streamlit as st

# st.title("Hello Streamlit 👋")
# st.write("This is your first Streamlit app!")
# st.write("Streamlit makes it easy to turn data scripts into web apps.")

# -------------------- Interactive Widgets -------------------- #

# import streamlit as st

# st.header("🎛️ Interactive Widgets Example")

# # Text input
# name = st.text_input("Enter your name:")

# # Slider
# age = st.slider("Select your age:", 1, 100, 25)

# # Button
# if st.button("Submit"):
#     st.success(f"Hello {name}! You are {age} years old.")


# -------------------- Chart Widgets -------------------- #

# import streamlit as st
# import pandas as pd
# import numpy as np

# st.header("📈 Displaying Data and Charts")

# data = pd.DataFrame(
#     np.random.randn(10, 3),
#     columns=['A', 'B', 'C']
# )

# st.write("### DataFrame:")
# st.dataframe(data)

# st.write("### Line Chart:")
# st.line_chart(data)

# st.write("### Area Chart:")
# st.area_chart(data)


# -------------------- Simple BMI Calculator -------------------- #

# import streamlit as st

# st.title("💪 BMI Calculator")

# weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.5)
# height = st.number_input("Enter your height (m):", min_value=0.5, step=0.01)

# if st.button("Calculate BMI"):
#     bmi = weight / (height ** 2)
#     st.write(f"Your BMI is: **{bmi:.2f}**")
    
#     if bmi < 18.5:
#         st.warning("You are underweight.")
#     elif 18.5 <= bmi < 24.9:
#         st.success("You have a healthy weight!")
#     elif 25 <= bmi < 29.9:
#         st.info("You are overweight.")
#     else:
#         st.error("You are obese.")


#Import the Streamlit library
import streamlit as st


st.title("Streamlit Layout Basics")
st.write("This app demonstrates how to use columns, rows, and other layout features in Streamlit.")

    # --- Using Columns ---
st.header("Columns Example")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Column 1")
    st.write("This is the first column.")
with col2:
    st.subheader("Column 2")
    st.write("This is the second column.")
with col3:
    st.subheader("Column 3")
    st.write("This is the third column.")

    # --- Using Sidebar ---
st.sidebar.header("Sidebar Example")
st.sidebar.write("You can add widgets and controls here.")
choice = st.sidebar.selectbox("Choose an option:", ["Home", "About", "Contact"])
st.sidebar.write(f"You selected: {choice}")

    # --- Using Containers ---
st.header("Container Example")
with st.container():
    st.write("This content is inside a container.")
    st.line_chart({"data": [1, 3, 2, 4]})

    # --- Expander Section ---
with st.expander("Click to expand"):
    st.write("Here you can hide or show content dynamically.")

    # --- Tabs Example ---
st.header("Tabs Example")
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("This is content inside Tab 1.")
with tab2:
    st.write("This is content inside Tab 2.")