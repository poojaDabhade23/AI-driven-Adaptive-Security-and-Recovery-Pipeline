# Pipeline

import subprocess
import os

# List of your stage scripts in order
pipeline_scripts = [
    "anomaly_creation.py",
    "monitoring_stage1.py",
    "detection_stage2.py",
    "quarantine_stage3.py",
    "resolution_stage4.py",
    "Dashboarding.py",
    "Web-Dashboarding.py"  # Optional: This launches the Streamlit app
]

def run_script(script):
    print(f"\n▶️ Running: {script}")
    if script == "Web-Dashboarding.py":
        print("📊 Opening Streamlit Dashboard in browser...")
        subprocess.run(["streamlit", "run", script])
    else:
        result = subprocess.run(["python", script])
        if result.returncode != 0:
            print(f"❌ Failed: {script}")
        else:
            print(f"✅ Completed: {script}")

if __name__ == "__main__":
    for script in pipeline_scripts:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"⚠️ Script not found: {script}")
