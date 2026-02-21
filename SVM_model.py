import streamlit as st
import numpy as np
import joblib

#load the model
model=joblib.load('Drug Response.pkl')

st.title('Drug Response System')

Dosage = st.number_input('Drug Dosage')
Systolic_bp = st.number_input('Systolic Blood Pressure')
Heart_rate = st.number_input('Heart Rate')
Liver_TI = st.number_input('Liver Toxicity Index')
Blood_GL = st.number_input('Blood Glucose Level')

if st.button('Predict'):
    data=np.array([[Dosage,Systolic_bp,Heart_rate,Liver_TI,Blood_GL]])
    result=model.predict(data)

    if result[0]==1:
        st.error('Drug is responding to body')
    else:
        st.success('No effect of drug on body')
