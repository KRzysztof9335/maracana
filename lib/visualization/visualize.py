"""Module responsible for creating visualization of data"""
from lib.visualization.html_templates import MAIN_PAGE
from lib.visualization.html_utils import SimpleTable, SimpleTableRow
from lib.consts import RADIATOR_PAGE
from lib.db import get_matches_previous
from lib.utils.node_handler import create_file

HTML_NEWLINE = "<br>"

COLUMNS = ["Date", "Country", "League", "Home", "Away", "Probability", "Event", "Course", "Expected", "Real"]

def create_table_predictions_previous() -> SimpleTable:
    header = SimpleTableRow(COLUMNS, True)
    table = SimpleTable(header)
    for last_match in get_matches_previous():
        for prediction in last_match.predictions:
            row = SimpleTableRow([last_match.date,
                                  last_match.country,
                                  last_match.league,
                                  last_match.team_home,
                                  last_match.team_away,
                                  str(prediction.probability),
                                  prediction.name.name,
                                  str(prediction.course),
                                  str(prediction.expected),
                                  str(prediction.real)])
            table.add_row(row)

    return table


def create_table_predictions_current() -> SimpleTable:
    header = SimpleTableRow(COLUMNS, True)
    table = SimpleTable(header)
    return table


def create_visualization_page():
    table_predictions_current = create_table_predictions_current()
    table_predictions_previous = ""
    content = table_predictions_current.__str__() + HTML_NEWLINE +\
              table_predictions_previous.__str__()
    page_content = MAIN_PAGE.format(content=content)
    create_file(RADIATOR_PAGE, page_content)
    print(f"Visualization page located at: {RADIATOR_PAGE}")