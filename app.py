import streamlit as st

st.title("Retail Business Dashboard")

st.header("Manager Input Section")

st.write("Please enter the monethly sales target and select the region.")

sales = st.number_input("Enter Monthly Sales Target (in USD):",
                        min_value = 0,
                        max_value = 50000,
                        value=50000)
st.write("The sales target entered: {sales} USD.")

region = st.selectbox("Select Region:",
                     ["North", "South", "East", "West"])
st.write("The selected region: {region}")

if st.button("Submit"):
    st.success(f"Dashboard updated successfully!")

