# Monitoring Stage: AI-Powered Anomaly Detection

import os
import pandas as pd
from sklearn.ensemble import IsolationForest

print("Monitoring Stage: AI-Powered Anomaly Detection...")

def extract_file_features(directory):
    data = []
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            stats = os.stat(file_path)
            data.append({
                "file_name": file,
                "size": stats.st_size,
                "modification_time": stats.st_mtime,
                "creation_time": stats.st_ctime,
            })
    return pd.DataFrame(data)

features = extract_file_features("/kaggle/working/anomalous_files")  # Extract features as a DataFrame

# Select features for the model
X_train = features[["size", "modification_time", "creation_time"]]

# Train the Isolation Forest
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X_train)

# Predict anomalies
# Use the same feature DataFrame format
features["anomaly"] = model.predict(X_train)

# Filter anomalies (-1 indicates anomaly)
anomalies = features[features["anomaly"] == -1]
print(anomalies)
print("Monitoring Stage: AI-Powered Anomaly Detection done...")