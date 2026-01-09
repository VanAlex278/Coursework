# import pandas as pd
# import datetime
from src.reports import spending_by_category


def test_spending_by_category(test_sample_data):
    transaction = spending_by_category(test_sample_data, "Транспорт", "2020-01-20")
    transaction["Дата операции"] = transaction["Дата операции"].astype(str)
    transaction["Дата платежа"] = transaction["Дата платежа"].astype(str)
    data = transaction.to_dict('records')
    assert data == [{'Дата операции': '2020-01-09 18:30:00', 'Дата платежа': '2020-01-09', 'Номер карты': '*7197',
                     'Статус': 'OK', 'Сумма операции': -200.5, 'Валюта операции': 'RUB', 'Сумма платежа': -200.5,
                     'Валюта платежа': 'RUB', 'Кэшбэк': 2.0, 'Категория': 'Транспорт', 'MCC': 4121, 'Описание': 'Такси',
                     'Бонусы (включая кэшбэк)': 2.0, 'Округление на инвесткопилку': 0.0,
                     'Сумма операции с округлением': 200.5}]
