# Diabetes Risk Prediction

A machine learning project that predicts the likelihood of diabetes based on patient health metrics. The project follows a modular ML pipeline architecture, including data loading, preprocessing, model training, evaluation, feature importance analysis, and model persistence.

> Educational project only. This application is not intended for medical diagnosis or treatment.

## Features

* End-to-end machine learning pipeline
* Exploratory Data Analysis (EDA) notebook
* Data cleaning and preprocessing
* Model training and evaluation
* Feature importance analysis
* Model serialization with Joblib
* FastAPI-ready backend model
* Managed with `uv`

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Jupyter Notebook
* FastAPI
* Streamlit
* uv

## Project Structure

```text
diabetes-risk-prediction/
│
├── data/
│   └── diabetes.csv
│
├── model/
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
├── main.py
│
├── pyproject.toml
├── uv.lock
└── README.md
```

## Dataset

The project uses the Pima Indians Diabetes Dataset.

### Features

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

### Target

```text
Outcome
```

```text
0 = No Diabetes
1 = Diabetes
```

## Exploratory Data Analysis

The notebook:

```text
notebooks/01_eda.ipynb
```

contains:

* Dataset overview
* Missing value analysis
* Feature distributions
* Correlation analysis
* Target class distribution
* Initial insights for model development

## Machine Learning Pipeline

The project is organized into reusable pipeline stages:

### 1. Load Data

```text
scripts/load_data.py
```

Loads the dataset into memory.

### 2. Clean Data

```text
scripts/clean_data.py
```

Handles invalid values and preprocessing.

### 3. Split Data

```text
scripts/split_data.py
```

Creates training and testing datasets.

### 4. Train Model

```text
scripts/train_model.py
```

Trains the machine learning model.

### 5. Evaluate Model

```text
scripts/evaluate_model.py
```

Calculates performance metrics such as:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC AUC
* Confusion Matrix

### 6. Feature Importance

```text
scripts/feature_importance.py
```

Identifies the most influential features used by the model.

### 7. Save Model

```text
scripts/save_model.py
```

Stores the trained model for future inference.

## Installation

Clone the repository:

```bash
git clone https://github.com/hanan-nawaz/diabetes-risk-prediction-ai.git
cd diabetes-risk-prediction-ai
```

Install dependencies:

```bash
uv sync
```

If uv is not installed:

```bash
pip install uv
```

## Run the Full Pipeline

The complete workflow can be executed through:

```bash
uv run main.py
```

This will:

1. Load the dataset
2. Clean and preprocess data
3. Split train/test sets
4. Train the model
5. Evaluate performance
6. Generate feature importance results
7. Save the trained model

## Model Output

After training, the serialized model is stored in:

```text
model/diabetes_model.pkl
```

This model can later be served through a FastAPI API or integrated into a Streamlit application.

## Future Improvements

* Hyperparameter tuning
* SHAP explainability
* Model comparison experiments
* Docker containerization
* CI/CD pipeline
* FastAPI deployment
* Streamlit dashboard
* Prediction logging

## Learning Objectives

This project demonstrates:

* Data preprocessing
* Exploratory data analysis
* Classification modeling
* Model evaluation
* Feature importance analysis
* Project modularization
* Reproducible ML workflows

## Author

Abdul Hanan Nawaz

## Reference

- Dataset is downloaded from kaggle
