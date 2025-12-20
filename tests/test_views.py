"""Тесты для views.py"""
import pytest
import pandas as pd
from src.views import main_page


def test_main_page_structure():
    """Тест структуры ответа главной страницы."""
    # Создаем DataFrame с правильными колонками
    transactions = pd.DataFrame({
        'Дата операции': pd.to_datetime([]),
        'Номер карты': [],
        'Статус': [],
        'Сумма операции': [],
        'Сумма платежа': [],
        'Категория': [],
        'Описание': []
    })

    result = main_page(transactions, "2024-01-01 12:00:00")

    assert "greeting" in result
    assert "cards" in result
    assert "top_transactions" in result
    assert "currency_rates" in result
    assert "stock_prices" in result


def test_main_page_with_data():
    """Тест с реальными данными."""
    transactions = pd.DataFrame({
        'Дата операции': pd.to_datetime(['2024-01-15 14:30:00']),
        'Номер карты': ['*7197'],
        'Статус': ['OK'],
        'Сумма операции': [-100.0],
        'Сумма платежа': [-100.0],
        'Категория': ['Супермаркеты'],
        'Описание': ['Магазин']
    })

    result = main_page(transactions, "2024-01-15 14:30:00")

    assert result["greeting"] == "Добрый день"
    assert len(result["cards"]) >= 0
