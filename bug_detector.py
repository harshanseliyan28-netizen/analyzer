import subprocess
import os

def run_pylint_on_file(file_path):
    result = subprocess.run(
        ["python", "-m", "pylint", file_path],
        capture_output=True,
        text=True
    )
    return result.stdout


def analyze_folder(folder_path):
    total_output = ""

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"Analyzing: {file_path}")
                output = run_pylint_on_file(file_path)
                total_output += output

    return total_output


def count_issues(pylint_output):
    issues = 0
    for line in pylint_output.split("\n"):
        if "error" in line.lower() or "warning" in line.lower():
            issues += 1
    return issues