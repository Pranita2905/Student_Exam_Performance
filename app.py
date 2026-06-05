import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Student Performance Predictor")

hours_studied = st.number_input("Hours Studied")
previous_scores = st.number_input("Previous Scores")
sleep_hours = st.number_input("Sleep Hours")
sample_papers = st.number_input("Sample Question Papers Practiced")

if st.button("Predict"):

    features = pd.DataFrame({
        'Hours Studied': [hours_studied],
        'Previous Scores': [previous_scores],
        'Sleep Hours': [sleep_hours],
        'Sample Question Papers Practiced': [sample_papers]
    })

    prediction = model.predict(features)[0]

    st.success(f"Predicted Performance Index: {prediction:.2f}")
