# Detection Stage: AI-Powered Threat Classification

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np
import matplotlib.pyplot as plt

print("Detection Stage: AI-Powered Threat Classification...")

# Training data
data = {
    "file_name": ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt", "file6.txt"],
    "size": [2000, 4000, 6000, 2500, 5500, 3000],
    "modification_time": [
        1.735270e+09, 1.735271e+09, 1.735272e+09,
        1.735273e+09, 1.735274e+09, 1.735269e+09
    ],
    "creation_time": [
        1.735269e+09, 1.735269e+09, 1.735270e+09,
        1.735270e+09, 1.735271e+09, 1.735268e+09
    ],
    "threat": ["benign", "ransomware", "phishing", "benign", "ransomware", "phishing"]
}

df = pd.DataFrame(data)
label_encoder = LabelEncoder()
df['threat_label'] = label_encoder.fit_transform(df['threat'])

features = ["size", "modification_time", "creation_time"]
X_train = df[features]
y_train = df['threat_label']

model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# Test input
anomalous_data = pd.DataFrame({
    "file_name": ["anomalous_file.txt"],
    "size": [5000],
    "modification_time": [1.735275e+09],
    "creation_time": [1.735275e+09]
})
X_test = anomalous_data[features]
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)

predicted_label = label_encoder.inverse_transform(predictions)[0]
confidence = np.max(probabilities) * 100
file_name = anomalous_data['file_name'][0]

# Display results
print(f"File: {file_name}")
print(f"Predicted Threat: {predicted_label}")
print(f"Confidence: {confidence:.2f}%")

# 📊 PLOT: Show class probabilities
class_labels = label_encoder.classes_
plt.figure(figsize=(6, 4))
plt.bar(class_labels, probabilities[0], color='skyblue')
plt.title("Threat Classification Probabilities")
plt.ylabel("Probability")
plt.xlabel("Threat Type")
plt.ylim(0, 1)
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()

# ✅ Save to CSV
output_df = pd.DataFrame({
    "file_name": [file_name],
    "predicted_threat": [predicted_label],
    "confidence": [confidence]
})
output_df.to_csv("/kaggle/working/detection_log.csv", index=False)
print("✅ Detection log saved to detection_log.csv")

print("Detection Stage: AI-Powered Threat Classification done...")
