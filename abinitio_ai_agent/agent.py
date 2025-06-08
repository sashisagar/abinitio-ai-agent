def agent_review(code, test_result):
    # Basic mock AI suggestion
    if "KeyError" in test_result:
        return code.replace("df[\"age\"]", "df.get(\"age\", 0)")
    return code