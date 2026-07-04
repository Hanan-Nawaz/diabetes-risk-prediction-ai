# 🩺 Diabetes Risk Prediction (Machine Learning Project)

A machine learning project that predicts the likelihood of diabetes based on patient health metrics using a modular ML pipeline architecture.

The system includes:
- Data preprocessing
- Model training
- Evaluation
- Feature importance analysis
- Model persistence
- FastAPI backend deployment (Hugging Face Spaces)
- Streamlit frontend interface

---

## Disclaimer

This project is for **educational and research purposes only**.

- It does NOT provide medical advice, diagnosis, or treatment
- It must NOT be used for real-world medical decisions
- It is not a certified healthcare system
- Always consult a qualified healthcare professional for medical concerns

---

## Live Demo

### FastAPI Backend (Hugging Face)

https://hanannawaz0-diabetes-risk-api.hf.space/predict

---

### Streamlit Frontend

https://diabetes-risk-prediction-tool.streamlit.app/

---

## Privacy & GDPR (DSGVO)

- No personal data is stored
- No user tracking or analytics
- No cookies used for identification
- No data is shared with third parties
- Inputs are processed only in real-time
- No user identification is performed

---

## Features

- End-to-end machine learning pipeline
- Exploratory Data Analysis (EDA)
- Data cleaning & preprocessing
- Classification model training
- Model evaluation (Accuracy, Precision, Recall, F1, ROC AUC)
- Feature importance analysis
- Model serialization with Joblib
- FastAPI backend deployment
- Streamlit interactive UI
- Managed with uv

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- FastAPI
- Streamlit
- Jupyter Notebook
- uv

---

## Project Structure

```text
diabetes-risk-prediction/
│
├── data/
│   └── diabetes.csv
│
├── ai_model/
│   └── diabetes_model.pkl
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── scripts/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── split_data.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── feature_importance.py
│   └── save_model.py
│
├── api/
│   ├── model/
│   │   ├── __init__.py
│   │   └── diabetes_model.py
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── results/
│   ├── classification_report.csv
│   ├── confusion_matrix.csv
│   ├── feature_importance.csv
│   └── model_metrics.csv
│
├── Dockerfile
├── main.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```
---

## Dataset

Pima Indians Diabetes Dataset

Features:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

Target:
0 → No Diabetes  
1 → Diabetes  

---

## Deployment

FastAPI Backend:
https://hanannawaz0-diabetes-risk-api.hf.space

Endpoint:
POST /predict

---

## Author

Abdul Hanan Nawaz

---

## Dataset Source

Kaggle: Pima Indians Diabetes Dataset