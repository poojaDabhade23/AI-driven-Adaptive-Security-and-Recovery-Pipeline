# Introduce Anomaly in a file
import os
import time
import stat
import shutil

# Directory to store anomalous files
output_directory = "/kaggle/working/anomalous_files"

# Clean the output directory if it exists
if os.path.exists(output_directory):
    shutil.rmtree(output_directory)  # Remove all contents of the directory
    
os.makedirs(output_directory, exist_ok=True)

print("Introduce Anomaly in a file...")

# Create the anomalous file
anomalous_file_path = os.path.join(output_directory, "anomalous_file.txt")
with open(anomalous_file_path, "w") as file:
    file.write("A" * 10_000_000)  # Create a file with 10 MB size.

# Set future modification and creation time
future_time = time.mktime((2030, 1, 1, 0, 0, 0, 0, 0, 0))  # Future date: 2030
os.utime(anomalous_file_path, (future_time, future_time))

# Add binary garbage data to the anomalous file
with open(anomalous_file_path, "w") as file:
    file.write("\x00\xFF\xAA" * 1000)  # Add binary garbage data.

# Create duplicate files with the same content
for i in range(100):
    duplicate_file_path = os.path.join(output_directory, f"duplicate_{i}.txt")
    with open(duplicate_file_path, "w") as file:
        file.write("Duplicate content")

# Change permissions of the anomalous file to make it executable only
os.chmod(anomalous_file_path, stat.S_IXUSR)  # Make it executable only.

print(f"Introducing Anomaly in a file done. Files are stored in: {output_directory}")