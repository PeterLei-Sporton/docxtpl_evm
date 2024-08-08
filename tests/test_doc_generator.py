from docxtplevm.CustomDocxTemplate import CustomDocxTemplate

tpl = CustomDocxTemplate("tests/test_file/test.docx")

context = {
    "A": [f"a{i+1}" for i in range(2)],
    "B": [f"b{i+1}" for i in range(3)],
    "C": [f"c{i+1}" for i in range(4)],
    "index_a": [i*3*4 for i in range(2)],
    "index_b": [i*4 for i in range(6)],
    "count_a": [0],
    "count_b": [0],
    "escape": "<>&"
}

tpl.render(context)
tpl.save("tests/test_file/test_output.docx")
