import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.title('🩺 Patient Health Prediction App')
st.write('Enter patient vital signs below to predict derived health parameters and risk category.')

# Inputs
heart_rate = st.number_input('Heart Rate (bpm)')
respiratory_rate = st.number_input('Respiratory Rate (breaths/min)')
body_temperature = st.number_input('Body Temperature (°C)')
oxygen_saturation = st.number_input('Oxygen Saturation (%)')
systolic_bp = st.number_input('Systolic Blood Pressure (mm Hg)')
diastolic_bp = st.number_input('Diastolic Blood Pressure (mm Hg)')
age = st.number_input('Age (years)')
gender = st.selectbox('Gender', ['Male', 'Female'])
weight = st.number_input('Weight (kg)')
height = st.number_input('Height (m)')

# Gender encoding
gender_numeric = 1 if gender == 'Male' else 0

# Predict button
if st.button('Predict'):
    # Prepare input
    input_data = np.array([[heart_rate, respiratory_rate, body_temperature,
                            oxygen_saturation, systolic_bp, diastolic_bp,
                            age, gender_numeric, weight, height]])
    
    # Predict
    prediction = model.predict(input_data)
    
    # Assuming model gives 5 outputs: HRV, Pulse Pressure, BMI, MAP, Risk Category
    derived_hrv = prediction[0][0]
    derived_pulse_pressure = prediction[0][1]
    derived_bmi = prediction[0][2]
    derived_map = prediction[0][3]
    risk_category = prediction[0][4]
    
    # Display outputs
    st.subheader('Predicted Results:')
    st.write(f'🧬 Derived HRV: {derived_hrv:.2f}')
    st.write(f'🫀 Derived Pulse Pressure: {derived_pulse_pressure:.2f}')
    st.write(f'⚖️ Derived BMI: {derived_bmi:.2f}')
    st.write(f'💉 Derived MAP: {derived_map:.2f}')
    st.success(f'🏥 Risk Category: {risk_category}')
