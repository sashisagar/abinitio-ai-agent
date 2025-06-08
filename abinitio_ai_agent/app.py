import streamlit as st
from parser import parse_mp_file
from codegen import generate_python_code
from testgen import generate_test
from agent import agent_review
import os

st.title("Ab Initio .mp to Python Agent")

uploaded_file = st.file_uploader("Upload Ab Initio .mp file", type=["mp"])

if uploaded_file:
    mp_content = uploaded_file.read().decode("utf-8")
    st.subheader("📄 .mp File Content")
    st.code(mp_content, language="plaintext")

    st.subheader("🔍 Parsed Graph")
    graph_ir = parse_mp_file(mp_content)
    st.json(graph_ir)

    st.subheader("🐍 Generated Python Code")
    python_code = generate_python_code(graph_ir)
    st.code(python_code, language="python")

    st.subheader("✅ Generated Test Code")
    test_code = generate_test(graph_ir)
    st.code(test_code, language="python")

    # Save files for testing
    with open("outputs/generated_code.py", "w") as f:
        f.write(python_code)
    with open("outputs/test_generated.py", "w") as f:
        f.write(test_code)

    st.subheader("⚙️ Running Test...")
    test_result = os.popen("pytest outputs/test_generated.py --tb=short").read()
    st.text(test_result)

    if "FAILED" in test_result:
        st.subheader("🧠 Agent Suggestions")
        improved_code = agent_review(python_code, test_result)
        st.code(improved_code, language="python")