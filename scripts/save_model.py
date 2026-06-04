import joblib

def save_model(model):
    joblib.dump(model, "model/diabetes_model.pkl")