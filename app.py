import streamlit as st

# Set up the web page title and icon
st.set_page_page_config(page_title="Python Calculator", page_icon="🧮")
st.title("🧮 My Visual Python Calculator")

# 1. Visual Dropdown for the operator
operator = st.selectbox("Enter an operator:", ["+", "-", "*", "/"])

# 2. Visual Input Boxes for the numbers
num1 = st.number_input("Enter the 1st number:", value=0.0)
num2 = st.number_input("Enter the 2nd number:", value=0.0)

# 3. Calculation Logic (Fixed from your original video code)
if st.button("Calculate", type="primary"):
    if operator == "+":
        result = num1 + num2
        st.success(f"### Result: {round(result, 3)}")
        
    elif operator == "-":
        result = num1 - num2
        st.success(f"### Result: {round(result, 3)}")
        
    elif operator == "*":
        result = num1 * num2  # Fixed the 'resut' typo here
        st.success(f"### Result: {round(result, 3)}")
        
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            st.success(f"### Result: {round(result, 3)}")
        else:
            st.error("Error: You cannot divide by zero!")
