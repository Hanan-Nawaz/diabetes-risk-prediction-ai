from fastapi import FastAPI
from scripts.load_model import load_model
from model.diabetes_model import DiabetesModel
import numpy as np

app = FastAPI()

@app.post("/predict")
def predict_diabetes(data: DiabetesModel):
    features = np.array([
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Insulin
    ])

    model = load_model("../model/diabetes_model.pkl")
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    if probability < 0.3:
        risk = "Low"
    elif probability < 0.7:
        risk = "Medium"
    else:
        risk = "High"

    return{
        risk: risk,
        probability: round(float(probability), 3),
        prediction: int(prediction)
    }