import pandas as pd
from unittest.mock import patch, mock_open
from src.utils import load_transactions, get_greeting, json_file_reader


@patch("pandas.read_excel")
def test_load_transactions(mock_excel):
    expected = pd.DataFrame({"Дата операции": ["15.01.2020 16:44:00", "14.01.2020 16:42:04"], "Номер карты": ["*7197", "*5814"]})  # pd.DataFrame()
    mock_excel.return_value = expected
    result = load_transactions("test_file")
    result["Дата операции"] = result["Дата операции"].astype(str)
    assert result["Дата операции"][0] == '2020-01-15 16:44:00'
    assert result["Номер карты"][0] == "*7197"


def test_get_greeting_morning():
    """Тест приветствия для утра."""
    assert get_greeting("2020-01-01 08:00:00") == "Доброе утро"


def test_get_greeting_day():
    """Тест приветствия для дня."""
    assert get_greeting("2020-01-01 14:00:00") == "Добрый день"


def test_get_greeting_night():
    """Тест приветствия для дня."""
    assert get_greeting("2020-01-01 01:15:43") == "Доброй ночи"


def test_get_greeting_evening():
    """Тест приветствия для дня."""
    assert get_greeting("2020-01-01 22:52:59") == "Добрый вечер"


@patch("json.load")
def test_json_file_reader(mock_load):
    with patch("builtins.open", mock_open()):
        mock_load.return_value = [{'test_1': 'test_data'}]
        result = json_file_reader("dummy data")
        expected = [{'test_1': 'test_data'}]
        assert result == expected
