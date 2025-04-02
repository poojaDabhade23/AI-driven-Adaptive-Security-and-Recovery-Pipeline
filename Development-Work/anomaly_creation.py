# Introduce Anomaly in working directory

import os
import time
import stat
import shutil

# Define directories
base_directory = "/kaggle/working"
app_dir = os.path.join(base_directory, "Application_files_Main")
sandbox_dir = os.path.join(base_directory, "Application_files_sandboxed")
anomalous_file_name = "anomalous_file.txt"
anomalous_file_path = os.path.join(app_dir, anomalous_file_name)

# Clean up base directory
for filename in os.listdir(base_directory):
    file_path = os.path.join(base_directory, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print(f"Failed to delete {file_path}. Reason: {e}")

# Recreate application and sandbox directories
os.makedirs(app_dir, exist_ok=True)
os.makedirs(sandbox_dir, exist_ok=True)


# Step 1: Create 500 clean files in application_files
for i in range(1, 501):
    file_name = f"file{i}.txt"
    file_path = os.path.join(app_dir, file_name)
    with open(file_path, "w") as file:
        file.write(f"This is file {i}")

print(f"✅ Main application files present in a directory: {app_dir}")

# Step 2: Copy clean files to sandbox before adding anomaly
for file_name in os.listdir(app_dir):
    src = os.path.join(app_dir, file_name)
    dest = os.path.join(sandbox_dir, file_name)
    shutil.copy(src, dest)

print(f"✅ Backed up original files in a sandboxing directory: {sandbox_dir}")

# Step 3: Introduce the anomalous file (after sandbox copy)
print("⚠️ Introducing anomaly in: anomalous_file.txt")
with open(anomalous_file_path, "w") as file:
    file.write("A" * 10_000_000)  # 10MB junk
    file.write("\x00\xFF\xAA" * 1000)

# Set future timestamps
future_time = time.mktime((2030, 1, 1, 0, 0, 0, 0, 0, 0))
os.utime(anomalous_file_path, (future_time, future_time))

# Set to executable-only
os.chmod(anomalous_file_path, stat.S_IXUSR)

print(f"✅ Anomalous file is now added to: {anomalous_file_path}")
