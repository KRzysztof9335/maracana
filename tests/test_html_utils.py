import lib.visualization.html_utils

def test_simple_table_cell_header():

    inst = lib.visualization.html_utils.SimpleTableCell("AAA", True)
    assert inst.__str__() == "<th>AAA</th>"

def test_simple_table_cell_not_header():
    inst = lib.visualization.html_utils.SimpleTableCell("AAA")
    assert inst.__str__() == "<td>AAA</td>"