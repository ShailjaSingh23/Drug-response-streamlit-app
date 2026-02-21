import streamlit as st
import numpy as np
import joblib

#load the model
model=joblib.load('Drug Response.pkl')

st.title('Drug Response System')

Dosage = st.number_input('Drug Dosage')
Systolic Blood Pressure = st.number_input('Systolic Blood Pressure')
Heart Rate = st.number_input('Heart Rate')
Liver Toxicity Index = st.number_input('Liver Toxicity Index')
Blood Glucose Level = st.number_input('Blood Glucose Level')

if st.button('Predict'):
    data=np.array([[Dosage,Systolic Blood Pressure,Heart Rate,Liver Toxicity Index,Blood Glucose Level]])
    result=model.predict(data)

    if result[0]==1:
        st.error('Drug is responding to body')
    else:
        st.success('No effect of drug on body')