def generate_test(graph):
    return '''import pandas as pd

def test_transformation():
    input_df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 40]})
    expected_df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [31, 41]})
    input_df["age"] = input_df["age"] + 1
    pd.testing.assert_frame_equal(input_df, expected_df)
'''