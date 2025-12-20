from src.utils import get_greeting


def test_get_greeting_morning():
    """Тест приветствия для утра."""
    assert get_greeting("2020-01-01 08:00:00") == "Доброе утро"


def test_get_greeting_day():
    """Тест приветствия для дня."""
    assert get_greeting("2020-01-01 14:00:00") == "Добрый день"
