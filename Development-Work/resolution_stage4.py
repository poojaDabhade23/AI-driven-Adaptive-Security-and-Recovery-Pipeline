# Resolution stage

import os
import shutil
import random

print("🛠️ Resolution Stage: AI-Powered Recovery & Validation")

# Define paths
main_dir = "/kaggle/working/Application_files_Main"
sandbox_dir = "/kaggle/working/Application_files_sandboxed"
quarantine_dir = "/kaggle/working/Quarantined_files"
recovery_log = []

# 1. AI-style decision engine
def ai_recovery_decision(file_name, confidence):
    threat_type = "ransomware" if "anomalous" in file_name else "unknown"
    score = 0
    if threat_type == "ransomware":
        score += 60
    if confidence > 80:
        score += 30
    elif confidence > 50:
        score += 15

    if score >= 70:
        return "full_restore"
    elif score >= 40:
        return "replace_and_restart"
    else:
        return "replace_only"

# 2. Simulated post-recovery validation
def validate_recovery(file_name):
    return random.choice([True, True, True, False])  # 75% success rate

# 3. Recover files
for file_name in os.listdir(quarantine_dir):
    sandboxed_file = os.path.join(sandbox_dir, file_name)
    restore_path = os.path.join(main_dir, file_name)

    if not os.path.exists(sandboxed_file):
        print(f"⚠️ Clean version missing for {file_name}, skipping...")
        continue

    # Simulate AI model decision
    confidence = 85 if "anomalous" in file_name else 50
    action = ai_recovery_decision(file_name, confidence)

    # Restore the file
    shutil.copy(sandboxed_file, restore_path)
    print(f"✅ Restored {file_name} to Application_files_Main")

    # Simulate validation
    validation_passed = validate_recovery(file_name)
    validation_msg = "✔️ Passed" if validation_passed else "❌ Failed - alert admin"

    # Log result
    recovery_log.append({
        "file": file_name,
        "confidence": confidence,
        "action": action,
        "validation": validation_msg
    })

# 4. Print recovery summary
print("\n📋 Recovery Summary:")
for entry in recovery_log:
    print(f"{entry['file']} → {entry['action']} | Confidence: {entry['confidence']}% | Validation: {entry['validation']}")

print("\n✅ Resolution Stage Completed.")

