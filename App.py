import streamlit as st
import joblib
import pandas as pd
import numpy as np
# streamlit run "C:\Users\Jeevabharathi\Desktop\LoanPrediction Project\App.py"

model = joblib.load("C:/Users/Jeevabharathi/Desktop/LoanPrediction Project/model.joblib")

st.title("Loan Approval Prediction")
st.write("Please Provide the Following Data Carefully")

gender = st.selectbox("Gender:", ['Male', 'Female', 'Other'])
married = st.selectbox("Marital Status:", ['Yes', 'No'])
dependents = st.selectbox("Number of Dependents:", ['0', '1', '2', '3+', 'Other'])
education = st.selectbox("Education:", ['Graduate', 'Not Graduate'])
self_employed = st.selectbox("Self Employed:", ['No', 'Yes'])
applicant_income = st.number_input("Applicant's Annual Income(eg:50000):", min_value=0)
coapplicant_income = st.number_input("Coapplicant's Annual Income(eg:50000):", min_value=0)
loan_amount = st.number_input("Loan Amount(eg:50000):", min_value=0)
loan_amount_term = st.number_input("Loan Amount Term (in months):", min_value=0)
credit_history = st.selectbox("Credit History:", ["No", "Yes"]) 
property_area = st.selectbox("Property Area:", ['Urban', 'Semiurban', 'Rural'])

applicant_income /= 10
coapplicant_income /= 10
loan_amount /= 10
loan_amount_term *= 30

if st.button("Predict Loan Approval"):
    user_data = pd.DataFrame({
        'Gender': [gender],
        'Married': [married],
        'Dependents': [dependents],
        'Education': [education],
        'Self_Employed': [self_employed],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_amount_term],
        'Credit_History': [credit_history],
        'Property_Area': [property_area]
    })

    user_data.replace({
        'Gender':{'Male': 1, 'Female': 0, 'Other': 2},
        'Married':{'Yes': 1, 'No': 0},
        'Dependents':{'0': 0, '1': 1, '2': 2, '3+': 3, 'Other': 4},
        'Education':{'Graduate': 0, 'Not Graduate': 1},
        'Self_Employed':{'No': 0, 'Yes': 1},
        'Credit_History':{'No': 0, 'Yes': 1},
        'Property_Area':{'Urban':2,'Semiurban':1,'Rural':0},

    },inplace=True)

    prediction = model.predict(user_data)
    st.subheader("Prediction:")
    if prediction[0] == 1:
        st.success("Congratulations! The loan is likely to be approved.")
    else:
        st.error("Sorry, the loan is likely to be rejected.")

# print(user_data)