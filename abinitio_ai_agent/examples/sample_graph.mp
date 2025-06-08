graph
  name "SampleGraph"
  component "input" type "input_table"
    parameters:
      file: "input_data.txt"
  component "transform" type "reformat"
    parameters:
      expression: "age = age + 1"
  component "output" type "output_table"
    parameters:
      file: "output_data.txt"
  flow "input" -> "transform"
  flow "transform" -> "output"