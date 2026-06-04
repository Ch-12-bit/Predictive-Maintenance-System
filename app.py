import streamlit as st
import numpy as np
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("model.pkl")

# Page title
st.title("🔧 Predictive Maintenance System")
st.write("Predict whether a machine is likely to fail based on sensor readings.")

# Input fields
air_temp = st.number_input(
    "Air Temperature [K]",
    min_value=290.0,
    max_value=310.0,
    value=298.0
)

process_temp = st.number_input(
    "Process Temperature [K]",
    min_value=300.0,
    max_value=320.0,
    value=308.0
)

rpm = st.number_input(
    "Rotational Speed [rpm]",
    min_value=1000,
    max_value=3000,
    value=1500
)

torque = st.number_input(
    "Torque [Nm]",
    min_value=0.0,
    max_value=100.0,
    value=40.0
)

tool_wear = st.number_input(
    "Tool Wear [min]",
    min_value=0,
    max_value=300,
    value=10
)

chart_df = pd.DataFrame({
    "Feature": [
        "Air Temp",
        "Process Temp",
        "RPM",
        "Torque",
        "Tool Wear"
    ],
    "Value": [
        air_temp,
        process_temp,
        rpm,
        torque,
        tool_wear
    ]
})

st.subheader("Sensor Readings")
st.bar_chart(chart_df.set_index("Feature"))

# Predict button
if st.button("Predict Machine Status"):

    data = np.array([
        [
            air_temp,
            process_temp,
            rpm,
            torque,
            tool_wear
        ]
    ])

    prediction = model.predict(data)
    probability = model.predict_proba(data)

    failure_prob = probability[0][1] * 100

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error(
            f"⚠️ Machine Failure Likely\n\nFailure Probability: {failure_prob:.2f}%"
        )
    else:
        st.success(
            f"✅ Machine Operating Normally\n\nFailure Probability: {failure_prob:.2f}%"
        )

# Sidebar
st.sidebar.header("About Project")
st.sidebar.write("""
This Predictive Maintenance System uses a
Random Forest Machine Learning model trained
on the AI4I 2020 Predictive Maintenance Dataset.

Features Used:
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear
""")