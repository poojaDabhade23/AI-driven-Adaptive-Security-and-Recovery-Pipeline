# Detection Stage: AI-Powered Threat Classification

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np

print("Detection Stage: AI-Powered Threat Classification...")
# Example training data
data = {
    "file_name": ["file1.txt", "file2.txt", "file3.txt"],
    "size": [2000, 4000, 6000],
    "modification_time": [1.735270e+09, 1.735271e+09, 1.735272e+09],
    "creation_time": [1.735269e+09, 1.735269e+09, 1.735270e+09],
    "threat": ["benign", "ransomware", "phishing"]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Encode labels for threats
label_encoder = LabelEncoder()
df['threat_label'] = label_encoder.fit_transform(df['threat'])

# Training the Random Forest Classifier
features = ["size", "modification_time", "creation_time"]
X_train = df[features]
y_train = df['threat_label']

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Input anomaly data from Monitoring Stage
anomalous_data = pd.DataFrame({
    "file_name": ["anomalous_file.txt"],
    "size": [5000],
    "modification_time": [1.735275e+09],
    "creation_time": [1.735275e+09]
})

# Predict threat and confidence
X_test = anomalous_data[features]
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)

# Get predicted threat and confidence
predicted_label = label_encoder.inverse_transform(predictions)[0]
confidence = np.max(probabilities) * 100

# Output results in the desired format
file_name = anomalous_data['file_name'][0]
print(f"File: {file_name}")
print(f"Predicted Threat: {predicted_label}")
print(f"Confidence: {confidence:.2f}%")

print("Detection Stage: AI-Powered Threat Classification done...")