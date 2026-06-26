import streamlit as st
import numpy as np
import pandas as pd
import joblib

model_rf = joblib.load("model_rf.pkl")
std_scaler = joblib.load("std_scaler.pkl")
exp_cols = joblib.load("exp_cols.pkl")

st.title("🫀 Heart Disease Prediction System")
st.markdown(" > Enter the clinical details of the patient and click on predict")

age = st.slider("Age", 15, 120, 35)
sex = st.selectbox("Sex", ['M', 'F'])
resting_bp = st.number_input("Resting Blood-Pressure (mm/Hg)", min_value = 50, max_value =  250, value = 120)
chol = st.number_input("Total Cholesterol (mg/dL)", min_value = 60, max_value = 700, value = 230)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", ['Y', 'N'])
max_hr = st.number_input("Maximum Heart-Rate Achieved", min_value = 40, max_value = 250, value = 100)
ex_ang = st.selectbox("Exercise Induced Angina", ['Y', 'N'])
old_peak = st.number_input("Old-peak", min_value = 0.0, max_value = 10.0, value = 1.0, step = 0.1)
cp_type = st.selectbox("Chest Pain Type", ['ATA', 'NAP', 'TA', 'ASY'])
rest_ecg = st.selectbox("Resting ECG", ['Normal', 'ST', 'LVH'])
st_slope = st.selectbox("ST Slope", ['Up', 'Flat', 'Down'])

if st.button("PREDICT") :
    Is_male = 1 if sex.upper() == 'M' else 0
    f_BS = 1 if fasting_bs.upper() == 'Y' else 0
    ExerciseAngina = 1 if ex_ang.upper() == 'Y' else 0
    raw_inp = {
        'Age' : age,
        'Is_male' : Is_male,
        'RestingBP' : resting_bp,
        'Cholesterol' : chol,
        'f_BS' : f_BS,
        'MaxHR' : max_hr,
        'ExerciseAngina' : ExerciseAngina,
        'Oldpeak' : old_peak,
        'CP_type_' + cp_type : 1,
        'r_ECG_' + rest_ecg : 1,
        'ST_Slope_' + st_slope : 1
    }

    input_df = pd.DataFrame(raw_inp, index = [0])
    for col in exp_cols :
        if col not in input_df.columns.to_list() :
            input_df[col] = 0
        else :
            continue
    
    input_df = input_df[exp_cols]
    
    cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
    input_df[cols] = std_scaler.fit_transform(input_df[cols])

    prediction = model_rf.predict(input_df)

    if int(prediction[0]) == 1 :
        st.error("⚠️ RISK OF HEART DISEASE")
    else :
        st.success("✅ NO RISK OF HEART DISEASE")



    


