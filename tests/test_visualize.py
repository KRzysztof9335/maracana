from lib.visualization.visualize import create_table_predictions_previous


def disable_create_table_predictions_previous():
    out = create_table_predictions_previous()
    assert out.__str__() == ""

