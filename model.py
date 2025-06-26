import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib
# Load dataset
data = pd.read_csv('heart_disease.csv')
# Convert categorical columns to numerical
data['Smoking'] = data['Smoking'].map({'Yes': 1, 'No': 0})
data['High Blood Pressure'] = data['High Blood Pressure'].map({'Yes': 1, 'No': 0})
data['Diabetes'] = data['Diabetes'].map({'Yes': 1, 'No': 0})
data['Heart Disease Status'] = data['Heart Disease Status'].map({'Yes': 1, 'No': 0})
# Select features and target
features = ['Cholesterol Level', 'Smoking', 'Diabetes', 'Age',
'High Blood Pressure', 'Triglyceride Level', 'CRP Level']
X = data[features]
y = data['Heart Disease Status']
# Check for and report missing values
missing = X.isnull().sum()
print("Missing values in each feature:\n", missing)
# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)
# Create pipeline: Imputation → Scaling → Logistic Regression
model = Pipeline(steps=[
("imputer", SimpleImputer(strategy="mean")),
("scaler", StandardScaler()),
("classifier", LogisticRegression(max_iter=1000)) # Logistic Regression
])

# Train the model
model.fit(X_train, y_train)
# Save the trained model
joblib.dump(model, 'heart_model.pkl')
print(" Model trained and saved as heart_model.pkl")