from analyzer.bug_detector import analyze_folder, count_issues
from analyzer.security_scanner import run_bandit, count_security_issues
from analyzer.score import calculate_score
from analyzer.ai_suggester import get_ai_suggestions
import os

# Input folder
folder_path = input("Enter folder path: ")

# -------- BUG ANALYSIS --------
pylint_output = analyze_folder(folder_path)
bug_issues = count_issues(pylint_output)

# -------- SECURITY ANALYSIS --------
bandit_output = run_bandit(folder_path)
security_issues = count_security_issues(bandit_output)

# -------- SCORE CALCULATION --------
total_issues = bug_issues + (security_issues * 2)
score = calculate_score(total_issues)

# -------- AI ANALYSIS (pick one file to analyze) --------
sample_file = None

# Find first Python file in folder
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".py"):
            sample_file = os.path.join(root, file)
            break
    if sample_file:
        break

# Read code for AI
if sample_file:
    with open(sample_file, "r", encoding="utf-8") as f:
        code_sample = f.read()

    ai_feedback = get_ai_suggestions(code_sample)
else:
    ai_feedback = "No Python files found for AI analysis."

# -------- OUTPUT --------
print("\n----- AI Codebase Health Analyzer -----")
print("Folder:", folder_path)
print("Bug Issues:", bug_issues)
print("Security Issues:", security_issues)
print("Health Score:", score)

print("\n--- AI Suggestions (from sample file) ---")
print(ai_feedback)