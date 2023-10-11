from typing import List


class SimpleTableCell():
    """A table class to create table cells."""

    def __init__(self, text: str, header: bool = False):
        """Table cell constructor."""
        self.text = text
        self.header = header

    def __str__(self):
        """Return the HTML code for the table cell."""
        if self.header:
            return f'<th>{self.text}</th>'
        else:
            return f'<td>{self.text}</td>'


class SimpleTableRow():
    """A table class to create table rows, populated by table cells"""
    def __init__(self, cells: List[str] = [], header: bool = False):
        """Table row constructor."""
        self.cells: List[SimpleTableCell] = [SimpleTableCell(cell, header=header) for cell in cells]
        self.header = header

    def __str__(self):
        """Return the HTML code for the table row and its cells as a string."""
        row: List[str] = []

        row.append('<tr>')

        for cell in self.cells:
            row.append(str(cell))

        row.append('</tr>')

        return '\n'.join(row)

    def add_cell(self, cell: SimpleTableCell):
        """Add a SimpleTableCell object to the list of cells."""
        self.cells.append(cell)


class SimpleTable():
    """A table class to create HTML tables, populated by HTML table rows."""

    def __init__(self, header_row: SimpleTableRow, rows: List[SimpleTableRow] = [], css_class: str = ""):
        """Table constructor.
        """
        self.rows = rows
        self.header_row = header_row
        self.css_class = css_class

    def __str__(self):
        """Return the HTML code for the table as a string."""
        table: List[str] = []

        table.append(f'<table class={self.css_class}>')

        if self.header_row:
            table.append(str(self.header_row))

        for row in self.rows:
            table.append(str(row))

        table.append('</table>')

        return '\n'.join(table)

    def add_row(self, row: SimpleTableRow):
        """Add a SimpleTableRow object to the list of rows."""
        self.rows.append(row)

    def add_rows(self, rows: List[SimpleTableRow]):
        """Add a list of SimpleTableRow objects to the list of rows."""
        for row in rows:
            self.rows.append(row)


# table1 = SimpleTable(SimpleTableRow(["H1"]), [SimpleTableRow(["c1", "c2"])])

# a = table1.__str__()

# table1 = SimpleTable([['Header1', 'Header2', 'Header3'] ,['Hello,', 'world!'], ['How', 'are', 'you?']], css_class='mytable')
# table2 = SimpleTable([['Testing', 'this'], ['table', 'here']],
#         css_class='mytable')

# pass