import streamlit as st
import requests

st.set_page_config(page_title="Currency Converter", page_icon="💱")

st.title(" Currency Converter")

# Input Fields
amount = st.number_input("Enter amount", min_value=0.0, format="%.2f")
from_currency = st.text_input("From Currency (e.g., USD, INR, EUR)").upper()
to_currency = st.text_input("To Currency (e.g., USD, INR, EUR)").upper()

if st.button("Convert"):
    if not from_currency or not to_currency:
        st.error("Please enter valid currency codes.")
    else:
        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            result = data.get("result")
            if result is not None:
                st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
            else:
                st.error("Invalid conversion. Please check currency codes.")
        else:
            st.error("Failed to fetch data. Try again later.")
