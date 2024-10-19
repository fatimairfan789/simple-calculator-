import streamlit as st

# Define the calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Streamlit UI
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", step=1e-6, format="%.6f")
num2 = st.number_input("Enter second number", step=1e-6, format="%.6f")

# Dropdown menu for selecting operation
operation = st.selectbox("Choose operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the operation when button is clicked
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    
    st.write(f"Result: {result}")
