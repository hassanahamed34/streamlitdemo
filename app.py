import streamlit as st

st.title("Retail Business Dashboard")

st.header("Manager Input Section")

st.write("Please provide your details below:")

age = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)
color = st.selectbox("Choose your favorite color:",
                     ["Red", "Blue", "Green"])

if st.button("Submit"):
    st.success(f"Thank you! Age: {age}, Favorite Color: {color}")
