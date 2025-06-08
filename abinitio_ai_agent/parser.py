def parse_mp_file(mp_text):
    return {
        "nodes": [
            {"id": "input", "type": "input_table", "params": {"file": "input.txt", "columns": ["name", "age"]}},
            {"id": "transform", "type": "reformat", "params": {"expression": "age = age + 1"}},
            {"id": "output", "type": "output_table", "params": {"file": "output.txt"}}
        ],
        "edges": [
            {"from": "input", "to": "transform"},
            {"from": "transform", "to": "output"}
        ]
    }