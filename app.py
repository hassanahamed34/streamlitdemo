import streamlit as st

st.title("Retail Business Dashboard")

st.header("Manager Input Section")

st.write("Please enter the monethly sales target and select the region.")

sales = st.number_input("Enter Monthly Sales Target (in USD):",
                        min_value = 0,
                        max_value = 0,
                        value=50000)
region = st.selectbox("Select Region:",
                     ["North", "South", "East", "West"])

if st.button("Submit"):
    st.success(f"""The sales target entered: {sales} USD.
                   The selected region: {region}""")
  if sales > 100000:
    st.write("Great! You have set an ambitious target!")
