import streamlit as st
import joblib

category_model = joblib.load('category_model.pkl')
priority_model = joblib.load('priority_model.pkl')

st.title("Support Ticket Classification System")

ticket = st.text_area("Enter Support Ticket")

if st.button("Predict"):

    category = category_model.predict([ticket])[0]
    priority = priority_model.predict([ticket])[0]

    st.success(f"Category: {category}")
    st.warning(f"Priority: {priority}")
