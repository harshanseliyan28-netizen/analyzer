import streamlit as st
from analyzer.bug_detector import analyze_folder, count_issues
from analyzer.security_scanner import run_bandit, count_security_issues
from analyzer.score import calculate_score

st.title("🧠 AI Codebase Health Analyzer")

folder_path = st.text_input("Enter folder path", ".")

if st.button("Analyze"):
    pylint_output = analyze_folder(folder_path)
    bug_issues = count_issues(pylint_output)

    bandit_output = run_bandit(folder_path)
    security_issues = count_security_issues(bandit_output)

    total_issues = bug_issues + (security_issues * 2)
    score = calculate_score(total_issues)

    st.subheader("Results")
    st.write("Bug Issues:", bug_issues)
    st.write("Security Issues:", security_issues)
    st.write("Health Score:", score)