
from unittest.mock import patch
from src.csv_parser import parse_csv_line


@patch(
    "src.csv_parser.csv.reader",
    return_value=iter([["Pérez, Juan", "20"]])
)
def test_parse_csv_line_usa_lector_csv(mock_reader):
    linea = '"Pérez, Juan",20'

    resultado = parse_csv_line(linea)

    assert resultado == ["Pérez, Juan", "20"]
    mock_reader.assert_called_once_with([linea])

