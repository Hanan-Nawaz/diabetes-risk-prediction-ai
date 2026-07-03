import streamlit as st
import requests as req

st.set_page_config(page_title="Diabetes Risk Prediction", layout="wide")

st.subheader("Diabetes Risk Prediction Tool")
st.markdown("---")

col1, col2, col3 = st.columns([1, 1, 1], gap="large")

with col1:
    preg = st.number_input("Pregnancies")
    skin_thick = st.number_input("Skin Thickness")
    dia_ped_func = st.number_input("Diabetes Pedigree Function")

with col2:
    glu = st.number_input("Glucose")
    insul = st.number_input("Insulin")
    age = st.number_input("Age")

with col3:
    bp = st.number_input("Blood Pressure")    
    bmi = st.number_input("BMI")

btn = st.button("Check")    

if btn:

    if (preg == 0 or skin_thick == 0 or dia_ped_func == 0 or glu == 0 or
        insul == 0 or age == 0 or bp == 0 or bmi == 0):
        st.warning("Please fill all details")
    else:
        st.success("Success!")


