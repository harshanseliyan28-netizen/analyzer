import subprocess

def run_bandit(folder_path):
    result = subprocess.run(
        ["python", "-m", "bandit", "-r", folder_path],
        capture_output=True,
        text=True
    )
    return result.stdout


def count_security_issues(bandit_output):
    issues = 0
    for line in bandit_output.split("\n"):
        if "issue:" in line.lower():
            issues += 1
    return issues