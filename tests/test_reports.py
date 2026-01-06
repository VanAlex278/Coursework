# import pandas as pd
# import datetime
from src.reports import spending_by_category


def test_spending_by_category(test_sample_data):
    transaction = spending_by_category(test_sample_data, "Транспорт", "2020-01-20")
    transaction["Дата операции"] = transaction["Дата операции"].astype(str)
    transaction["Дата платежа"] = transaction["Дата платежа"].astype(str)
    data = transaction.to_dict('records')
    assert data[0]['Дата операции'] == '2020-01-09 18:30:00'
    assert data[0]["Категория"] == "Транспорт"