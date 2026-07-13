import streamlit as st
import joblib
import numpy as np
import pandas as pd
st.header('Student Stress Prediction')
st.subheader('Enter the following details')
student_type = st.selectbox(
    "Student Type",
    ['school', 'college', 'working_student']
)
sleep = st.number_input(' Total Sleep Hours')
study = st.number_input('Total Study Hours')
social_media = st.number_input('Total Time spent for Social Media(in Hrs)')
attendance = st.number_input('Enter the attendance(in %)')
exam_pressure = st.number_input('Rate your Exam Pressure on a scale of 1 to 10')
family_support = st.number_input('Rate your Family_support on a scale of 1-10')
model = joblib.load("stress_model.pkl")

if st.button('Predict'):
    test = pd.DataFrame(np.array([student_type, sleep, study, social_media, attendance, exam_pressure, family_support]).reshape(1, 7), columns=['Student_Type', 'Sleep_Hours', 'Study_Hours', 'Social_Media_Hours', 'Attendance', 'Exam_Pressure', 'Family_Support'])
    prediction = model.predict(test)
    if st.success(prediction[0]) == 0:
        st.text('Low Stress')
    else:
        st.text('High Stress')
    