
import streamlit as st
import pickle
import numpy as np

# Load model
with open('credit_card_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction details")

feature_names = [
    'Time','V1','V2','V3','V4','V5','V6','V7','V8','V9',
    'V10','V11','V12','V13','V14','V15','V16','V17','V18','V19',
    'V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount'
]

input_data = []

for feature in feature_names:
    value = st.number_input(feature, value=0.0)
    input_data.append(value)

if st.button("Predict"):

    prediction = model.predict([input_data])

    if prediction[0] == 0:
        st.success("✅ Legitimate Transaction")
    else:
        st.error("⚠️ Fraudulent Transaction")
