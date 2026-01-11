import joblib
import numpy as np

# ========== Load models & scalers ==========
diabetes_model = joblib.load("models/diabetes_rf_model.pkl")
diabetes_scaler = joblib.load("models/diabetes_scaler.pkl")

heart_model = joblib.load("models/heart_rf_model.pkl")
heart_scaler = joblib.load("models/heart_scaler.pkl")

kidney_model = joblib.load("models/kidney_rf_model.pkl")
kidney_scaler = joblib.load("models/kidney_scaler.pkl")

# ========== Helper function ==========
def prepare_data(patient_data):
    data = np.array(patient_data)
    if data.ndim == 1:
        data = data.reshape(1, -1)
    return data

# ========== Individual prediction functions ==========
def predict_diabetes(patient_data):
    data = prepare_data(patient_data)
    scaled = diabetes_scaler.transform(data)
    preds = diabetes_model.predict(scaled)
    return ["Diabetes Detected" if p==1 else "No Diabetes" for p in preds]

def predict_heart(patient_data):
    data = prepare_data(patient_data)
    scaled = heart_scaler.transform(data)
    preds = heart_model.predict(scaled)
    return ["Heart Disease Detected" if p==1 else "No Heart Disease" for p in preds]

def predict_kidney(patient_data):
    data = prepare_data(patient_data)
    scaled = kidney_scaler.transform(data)
    preds = kidney_model.predict(scaled)
    return ["Kidney Disease Detected" if p==1 else "No Kidney Disease" for p in preds]
