# Monitoring Stage: AI-Powered Anomaly Detection

import os
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

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

# Extract features from the directory
features = extract_file_features("/kaggle/working/Application_files_Main")

# Select features for the model
X_train = features[["size", "modification_time", "creation_time"]]

# Train the Isolation Forest
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X_train)

# Predict anomalies
features["anomaly"] = model.predict(X_train)

# Print anomaly details
anomalies = features[features["anomaly"] == -1]
print(anomalies)

# PLOT: Anomaly Detection Result
plt.figure(figsize=(8, 6))
colors = features["anomaly"].map({1: "blue", -1: "red"})
plt.scatter(features["size"], features["modification_time"], c=colors)

# Annotate file names
for i, row in features.iterrows():
    plt.annotate(row["file_name"], (row["size"], row["modification_time"]), fontsize=8)

plt.title("Anomaly Detection: File Size vs. Modification Time")
plt.xlabel("File Size (bytes)")
plt.ylabel("Modification Time")
plt.grid(True)
plt.legend(["Normal (Blue)", "Anomaly (Red)"])
plt.tight_layout()
plt.show()

print("Monitoring Stage: AI-Powered Anomaly Detection done...")