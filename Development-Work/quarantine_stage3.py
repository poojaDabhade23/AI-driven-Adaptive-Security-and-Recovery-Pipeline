# Quarantine Stage: AI-Driven Prioritization and Isolation
# AI-driven decision-making for quarantining files using reinforcement learning or basic scoring.

import os
import shutil
import matplotlib.pyplot as plt
import pandas as pd

# Global log list
log_records = []

# Quarantine logic
def quarantine_file(file_path, quarantine_folder):
    if not os.path.exists(quarantine_folder):
        os.makedirs(quarantine_folder)
    shutil.move(file_path, quarantine_folder)
    print(f"Quarantined {file_path} to {quarantine_folder}")
    return os.path.join(quarantine_folder, os.path.basename(file_path))

# Enhanced scoring function with visual breakdown
def score_file_with_visual(features):
    file_size, mod_freq = features
    scores = {
        "Size Score": 50 if file_size > 10_000 else 0,
        "Modification Frequency Score": 20 if mod_freq > 1 else 0,
        "Custom Rule Score": 100 if file_size == 10_000_000 else 0
    }

    total_score = sum(scores.values())

    # Plot score breakdown
    plt.figure(figsize=(6, 4))
    plt.bar(scores.keys(), scores.values(), color='salmon')
    plt.title("File Risk Score Breakdown")
    plt.ylabel("Points")
    plt.ylim(0, 120)
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()

    return "Malicious" if total_score >= 20 else "Safe"

# Handle suspicious file
def handle_suspicious_file(file_path, quarantine_folder):
    file_size = os.path.getsize(file_path)
    mod_freq = 2  # Placeholder value
    features = [file_size, mod_freq]

    classification = score_file_with_visual(features)

    quarantined_path = ""
    if classification == "Malicious":
        quarantined_path = quarantine_file(file_path, quarantine_folder)
    else:
        print(f"File {file_path} is safe.")

    # Append to log
    log_records.append({
        "file_name": os.path.basename(file_path),
        "file_size": file_size,
        "mod_freq": mod_freq,
        "classification": classification,
        "quarantined_path": quarantined_path
    })

# Paths
input_file = "/kaggle/working/Application_files_Main/anomalous_file.txt"
quarantine_folder = "/kaggle/working/Quarantined_files"

# Execute
handle_suspicious_file(input_file, quarantine_folder)

# ✅ Save to CSV
df_log = pd.DataFrame(log_records)
df_log.to_csv("/kaggle/working/quarantine_log.csv", index=False)
print("✅ Quarantine log saved to quarantine_log.csv")

