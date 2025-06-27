# ❤️ Heart Disease Prediction Web App

A Flask-based machine learning web application that predicts the presence of heart disease based on various clinical health metrics such as cholesterol, CRP, blood pressure, and more.

---

## 📊 Dataset & Model

- **Dataset Source**: Not explicitly mentioned (assumed to be a heart health dataset containing patient clinical information).
- **Model Used**: Trained and saved as `heart_model.pkl` using a suitable classification algorithm (e.g., Random Forest, Logistic Regression, etc.).
- **Target Output**: Binary classification — `Heart Disease Detected` or `No Heart Disease`.

---

## ⚙️ Input Features

The application uses the following patient health metrics as inputs:

| Feature              | Description                            |
|----------------------|----------------------------------------|
| Cholesterol Level     | Numeric value (e.g., mg/dL)            |
| Smoking              | Yes/No                                 |
| Diabetes             | Yes/No                                 |
| Age                  | Numeric (years)                        |
| High Blood Pressure  | Yes/No                                 |
| Triglyceride Level   | Numeric value                          |
| CRP Level            | C-Reactive Protein level (mg/L)        |

---

## 💻 Web Application Features

- A user-friendly form to enter patient data
- Predicts and displays if heart disease is likely
- Handles input errors gracefully
- Simple and fast deployment with Flask

---

## 🗂️ Project Structure

```

heart-disease-prediction/
├── app.py                      # Flask application file
├── heart\_model.pkl             # Trained machine learning model
├── templates/
│   ├── index.html              # Input form template
│   └── result.html             # Result display template
├── static/                     # (Optional) Styling assets
└── README.md                   # Project overview

````

---

## 🚀 How to Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction
````

### 2. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

> If you don't have a `requirements.txt`, you can install manually:

```bash
pip install Flask pandas numpy scikit-learn joblib
```

### 3. Ensure Model File Exists

Make sure `heart_model.pkl` is in the project directory.

### 4. Run the App

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📷 Screenshots

| Home Form                     | Result Output                     |
| ----------------------------- | --------------------------------- |
| ![image](https://github.com/user-attachments/assets/9dd7c5c1-4bb9-46fd-b14a-8ee0ea86263f)| ![image](https://github.com/user-attachments/assets/80700683-ac44-4b41-b04c-98715973ef49)
---

## ✅ Example Inputs

* Cholesterol Level: `210`
* Smoking: `Yes`
* Diabetes: `No`
* Age: `52`
* High Blood Pressure: `Yes`
* Triglyceride Level: `180`
* CRP Level: `4.3`

---

## ✍️ Author

**Kartik Sharma**
GitHub: [@kartik10sharma](https://github.com/kartik10sharma)

---

## 📄 License

This project is for educational use only. Model and dataset assumptions are based on synthetic or academic purposes. Please consult real clinical data and professional advice for medical use cases.

---


