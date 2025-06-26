from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

# Initialize app
app = Flask(__name__)

# Load heart disease model
model = joblib.load("heart_model.pkl")

# Home route to render form
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.form  # Get form data

        # Prepare input data
        input_data = {
            "Cholesterol Level": [float(data.get("cholesterol", 0))],
            "Smoking": [1 if data.get("smoking", "No") == "Yes" else 0],
            "Diabetes": [1 if data.get("diabetes", "No") == "Yes" else 0],
            "Age": [int(data.get("age", 0))],
            "High Blood Pressure": [1 if data.get("high_bp", "No") == "Yes" else 0],
            "Triglyceride Level": [float(data.get("triglyceride", 0))],
            "CRP Level": [float(data.get("crp", 0))]
        }

        # Create DataFrame and predict
        input_df = pd.DataFrame(input_data)
        prediction = model.predict(input_df)

        # Interpretation
        result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"
        return render_template('result.html', result=result)
    
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
