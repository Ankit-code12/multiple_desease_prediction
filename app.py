from flask import Flask, render_template, request
from disease_prediction import (
    predict_diabetes,
    predict_heart,
    predict_kidney,
    
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    disease = request.form.get("disease")

    try:
        # ---------------- DIABETES ----------------
        if disease == "diabetes":
            data = [
                int(request.form["pregnancies"]),
                float(request.form["glucose"]),
                float(request.form["bp"]),
                float(request.form["skin"]),
                float(request.form["insulin"]),
                float(request.form["bmi"]),
                float(request.form["dpf"]),
                int(request.form["age"])
            ]
            result = predict_diabetes(data)[0]

        # ---------------- HEART ----------------
        elif disease == "heart":
            data = [
                int(request.form["age"]),
                int(request.form["sex"]),
                int(request.form["cp"]),
                int(request.form["trestbps"]),
                int(request.form["chol"]),
                int(request.form["fbs"]),
                int(request.form["restecg"]),
                int(request.form["thalach"]),
                int(request.form["exang"]),
                float(request.form["oldpeak"]),
                int(request.form["slope"]),
                int(request.form["ca"]),
                int(request.form["thal"])
            ]
            result = predict_heart(data)[0]

        # ---------------- KIDNEY ----------------
        elif disease == "kidney":
            # 🔑 ID added as first column
            data = [
                0,  # id
                int(request.form["age"]),
                int(request.form["bp"]),
                float(request.form["sg"]),
                int(request.form["al"]),
                int(request.form["su"]),
                int(request.form["rbc"]),
                int(request.form["pc"]),
                int(request.form["pcc"]),
                int(request.form["ba"]),
                float(request.form["bgr"]),
                float(request.form["bu"]),
                float(request.form["sc"]),
                float(request.form["sod"]),
                float(request.form["pot"]),
                float(request.form["hemo"]),
                float(request.form["pcv"]),
                float(request.form["wc"]),
                float(request.form["rc"]),
                int(request.form["htn"]),
                int(request.form["dm"]),
                int(request.form["cad"]),
                int(request.form["appet"]),
                int(request.form["pe"]),
                int(request.form["ane"])
            ]
            result = predict_kidney(data)[0]

        else:
            result = "Invalid Selection"

        return render_template("result.html", result=result)

    except Exception as e:
        return render_template("result.html", result=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)

