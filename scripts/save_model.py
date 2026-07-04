import joblib

def save_model(model):
    joblib.dump(model, "ai_model/diabetes_model.pkl")