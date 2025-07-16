import streamlit as st
import requests

st.set_page_config(page_title="Currency Converter", page_icon="💱")

st.title("💱 Currency Converter")

# Input Fields
amount = st.number_input("Enter amount", min_value=0.0, format="%.2f")
from_currency = st.text_input("From Currency (e.g., USD, INR, EUR)").upper()
to_currency = st.text_input("To Currency (e.g., USD, INR, EUR)").upper()

if st.button("Convert"):
    if not from_currency or not to_currency:
        st.error("⚠️ Please enter valid currency codes.")
    else:
        try:
            url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
            response = requests.get(url)
            data = response.json()

            if "result" in data and data["result"] is not None:
                converted = data["result"]
                st.success(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
            else:
                st.error("❌ Invalid conversion. Check currency codes.")
                st.caption(f"Debug info: {data}")
        except Exception as e:
            st.error(f"⚠️ API error occurred: {e}")
