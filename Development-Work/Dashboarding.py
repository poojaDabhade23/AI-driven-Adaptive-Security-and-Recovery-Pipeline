# Dashboard creation of all the phases output

import pandas as pd
import matplotlib.pyplot as plt
import os

print("📊 AI-Driven Security Pipeline - Static Dashboard (Kaggle Compatible)")

# Load CSV logs
def load_log(file_path):
    if os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
            if df.empty:
                print(f"⚠️ {file_path} is empty.")
            return df
        except pd.errors.EmptyDataError:
            print(f"⚠️ {file_path} is empty or corrupted.")
            return pd.DataFrame()
    else:
        return pd.DataFrame()

monitor_df = load_log("/kaggle/working/monitoring_log.csv")
detect_df = load_log("/kaggle/working/detection_log.csv")
quarantine_df = load_log("/kaggle/working/quarantine_log.csv")
resolution_df = load_log("/kaggle/working/resolution_log.csv")

# --- MONITORING PHASE ---
print("\n🔍 Monitoring Phase")
if not monitor_df.empty:
    print(monitor_df.head())
    monitor_df['anomaly'].value_counts().plot(kind='bar', color=['green', 'red'], title="Anomaly Detection Count")
    plt.xlabel("Anomaly Flag")
    plt.ylabel("Number of Files")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("Monitoring log not found.")

# --- DETECTION PHASE ---
print("\n⚠️ Detection Phase")
if not detect_df.empty:
    print(detect_df.head())
    plt.figure(figsize=(10, 4))
    plt.bar(detect_df['file_name'], detect_df['confidence'], color='skyblue')
    plt.title("Detection Confidence by File")
    plt.xlabel("File Name")
    plt.ylabel("Confidence %")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
else:
    print("Detection log not found.")

# --- QUARANTINE PHASE ---
print("\n🚫 Quarantine Phase")
if not quarantine_df.empty:
    print(quarantine_df.head())
    quarantine_df['classification'].value_counts().plot(kind='bar', color='orange')
    plt.title("File Classification in Quarantine")
    plt.xlabel("Classification")
    plt.ylabel("File Count")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("Quarantine log not found.")

# --- RESOLUTION PHASE ---
print("\n🔧 Resolution Phase")
if not resolution_df.empty:
    print(resolution_df.head())
    resolution_df['action'].value_counts().plot(kind='pie', autopct='%1.1f%%', title="Recovery Actions")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()
else:
    print("Resolution log not found.")