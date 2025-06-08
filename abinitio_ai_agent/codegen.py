def generate_python_code(graph):
    return '''import pandas as pd

df = pd.read_csv("input.txt", delimiter="|")
df["age"] = df["age"] + 1
df.to_csv("output.txt", sep="|", index=False)
'''