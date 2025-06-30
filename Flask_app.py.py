import subprocess

# List of your Python scripts
scripts = ["cropData.py", "organicfarming_feedback.py"]

# List to hold the subprocess.Popen objects
processes = []

# Start each script as a separate process
for script in scripts:
    process = subprocess.Popen(["python", script])
    processes.append(process)

# Optionally, wait for all processes to complete
for process in processes:
    process.wait()