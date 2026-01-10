import pandas as pd
from datetime import datetime

import json
from src.reports import spending_by_category, writer_json, json_report


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


@writer_json("data/test.json")
def test_writer_fson():
    test_list = {'test1': [50, 21], 'test2': [131, 2]}
    test_list_json = json.dumps(test_list)
    return test_list_json




def test_json_report(test_sample_data):
    data_list = json.loads(json_report(test_sample_data))
    for data in data_list:
        data["Дата операции"] = datetime.strptime(data["Дата операции"], "%Y-%m-%d %H:%M:%S")
        data["Дата платежа"] = datetime.strptime(data["Дата платежа"], "%Y-%m-%d %H:%M:%S")

    data_df = pd.DataFrame(data_list)
    assert pd.DataFrame(data_df).equals(test_sample_data)
