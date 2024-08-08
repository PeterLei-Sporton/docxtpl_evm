# docxtpl_evm
This package is a quick and dirty way to make vertical merge in nested table possible in docxtpl.<br>
While [docxtpl_dynamic_vertical_merging](https://github.com/tsy19900929/docxtpl_dynamic_vertical_merging) exists, its approach messed up the document xml and make all chars that need to escape (`>`, `<`, `&`) dissappear.
<br>

# How to use
In docx template, use extended vertical merge tag: `{% evm <start_row_index_list> <counter> %}` in the table cell.
* `<start_row_index_list>` is the list of row indexes merged cell starts.
* `<counter>` is the row counter.
<br>

In python, add items for `<start_row_index_list>` and `<counter>` into your document context, for example:
```
context = {
    "A": [f"a{i+1}" for i in range(2)],
    "B": [f"b{i+1}" for i in range(3)],
    "C": [f"c{i+1}" for i in range(4)],
    "index_a": [i*3*4 for i in range(2)], # row index list for A
    "index_b": [i*4 for i in range(6)],   # row index list for B
    "count_a": [0],                       # counter for A
    "count_b": [0],                       # counter for B
    "escape": "<>&"
}
```
Notice that the counter should be a list contain the counter, this approach is due to jinja2 scoping rules, check [this](https://stackoverflow.com/questions/7537439/how-to-increment-a-variable-on-a-for-loop-in-jinja-template/32700975#32700975) for more information.

# Example
* context
```
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
```

* template
<img src="https://github.com/PeterLei-Sporton/docxtpl_evm/blob/main/template.png" />

* output
<img src="https://github.com/PeterLei-Sporton/docxtpl_evm/blob/main/output.png" />