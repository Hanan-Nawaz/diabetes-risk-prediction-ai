from fastapi import FastAPI
from scripts.load_model import load_model
from api.model.diabetes_model import DiabetesModel
import numpy as np
import pandas as pd

app = FastAPI()

@app.post("/predict")
def predict_diabetes(data: DiabetesModel):
    features = pd.DataFrame([{
        "Pregnancies": data.Pregnancies,
        "Glucose": data.Glucose,
        "BloodPressure": data.BloodPressure,
        "SkinThickness": data.SkinThickness,
        "Insulin": data.Insulin,
        "BMI": data.BMI,
        "DiabetesPedigreeFunction": data.DiabetesPedigreeFunction,
        "Age": data.Age
    }])

    model = load_model("ai_model/diabetes_model.pkl")
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    if probability < 0.3:
        risk = "Low"
    elif probability < 0.7:
        risk = "Medium"
    else:
        risk = "High"

    return {
        "risk": risk,
        "probability": round(float(probability), 3),
        "prediction": int(prediction)
    }