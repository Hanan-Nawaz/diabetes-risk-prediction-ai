import streamlit as st
import requests as req
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("url")

st.set_page_config(page_title="Diabetes Risk Prediction", layout="wide")

st.subheader("Diabetes Risk Prediction Tool")
st.caption("""
Disclaimer: This tool is for educational and research purposes only.
It is not intended for clinical or medical use.
""")
st.markdown("---")

st.warning("""
⚠️ Educational Project Only

This application is developed for learning and demonstration purposes only.

- It does NOT provide medical advice, diagnosis, or treatment
- Results should NOT be used for real medical decisions
- Always consult a qualified healthcare professional
""")

st.info("""
🔒 Data Privacy (GDPR / DSGVO)

- No personal data is stored
- No data is shared with third parties
- Inputs are processed only for real-time prediction
- No user tracking or analytics are used
""")
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

agree = st.checkbox("I understand this is not a medical diagnosis tool")

if not agree:
    st.stop()
btn = st.button("Check")    

if btn:

    if (preg == 0 or skin_thick == 0 or dia_ped_func == 0 or glu == 0 or
        insul == 0 or age == 0 or bp == 0 or bmi == 0):
        st.warning("Please fill all details")
    else:
        response = req.post(
            url,
            json={
                "Pregnancies": preg,
                "Glucose": glu,
                "BloodPressure": bp,
                "SkinThickness": skin_thick,
                "Insulin": insul,
                "BMI": bmi,
                "DiabetesPedigreeFunction": dia_ped_func,
                "Age": age
            }
        )

        data = response.json()
        if response.status_code == 200:
            st.success("Prediction completed (educational output)")
            st.markdown("---")
            col1, col2, col3 = st.columns([1, 1, 1], gap="large")

            with col1:
                st.write("Risk")
                risk = data["risk"]

                color = "green"
                if risk == "Medium":
                    color = "orange"
                elif risk == "High":
                    color = "red"

                html = f"""
                <div style="
                    background-color: {color};
                    padding:20px;
                    border-radius:10px;
                    font-size: 20px;
                    width:100%;
                    color:white;
                    text-align: center;
                ">
                    <p>{data["risk"]}</p>
                </div>
                """

                st.markdown(html, unsafe_allow_html=True)
            
            with col2:
                st.write("Probability")
                html = f"""
                <div style="
                    background-color: #262730;
                    padding:20px;
                    border-radius:10px;
                    font-size: 20px;
                    width:100%;
                    color:white;
                    text-align: center;
                ">
                    <p>{data["probability"]}</p>
                </div>
                """

                st.markdown(html, unsafe_allow_html=True)
            
            with col3:
                st.write("Model Output")
                html = f"""
                <div style="
                    background-color:#262730;
                    padding:20px;
                    border-radius:10px;
                    font-size: 20px;
                    width:100%;
                    color:white;
                    text-align: center;
                ">
                    <p>{data["prediction"]}</p>
                </div>
                """

                st.markdown(html, unsafe_allow_html=True)
        else:
            st.warning("An error occured! Request failed.")


