import streamlit as st
import os
import importlib.util

# Ensure outputs directory exists
os.makedirs("outputs", exist_ok=True)

st.title("🧠 Ab Initio MP → Python Agent")

uploaded_file = st.file_uploader("Upload an Ab Initio .mp file", type="mp")

if uploaded_file:
    # Save uploaded file
    mp_path = "outputs/input_graph.mp"
    with open(mp_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    st.success("✅ File uploaded successfully!")

    # Simulate parsing and Python code generation
    generated_code = '''
def some_function(x):
    return x * 2
'''

    # Save generated code
    gen_code_path = "outputs/generated_code.py"
    with open(gen_code_path, "w") as f:
        f.write(generated_code)

    # Generate a simple test file
    test_code = '''
def run_tests():
    from outputs.generated_code import some_function
    assert some_function(2) == 4
    assert some_function(3) != 10
'''

    test_path = "outputs/test_generated_code.py"
    with open(test_path, "w") as f:
        f.write(test_code)

    # Show code in UI
    st.subheader("🐍 Generated Python Code")
    st.code(generated_code, language="python")

    st.subheader("🧪 Generated Test Code")
    st.code(test_code, language="python")

    # Run tests directly
    st.subheader("🔁 Running Tests")
    try:
        spec = importlib.util.spec_from_file_location("test_generated_code", test_path)
        test_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_module)

        test_module.run_tests()
        st.success("✅ All tests passed!")
    except AssertionError as e:
        st.error("❌ Test failed.")
        st.exception(e)
    except Exception as ex:
        st.error("🚨 Unexpected error during test execution.")
        st.exception(ex)
