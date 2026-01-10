import json
import logging
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

import pandas as pd


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """
    Траты по категории за последние 3 месяца.

    Args:
        transactions: DataFrame с транзакций
        category: Название категории
        date: Дата отсчета (опционально)

    Returns:
        DataFrame с тратами по категории
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Отчет по категории: {category} для даты {date}")

    try:
        # Если дата не указана - берем текущую
        if date is None:
            target_date = datetime.now()
        else:
            target_date = datetime.strptime(date, "%Y-%m-%d")

        # Расчет периода (3 месяца назад)
        start_date = target_date - timedelta(days=90)

        # Фильтрация транзакций
        filtered_data = transactions[
            (transactions["Дата операции"] >= start_date)
            & (transactions["Дата операции"] <= target_date)
            & (transactions["Категория"] == category)
            & (transactions["Сумма операции"] < 0)  # Только расходы
        ]

        return filtered_data

    except Exception as e:
        logger.error(f"Ошибка формирования отчета: {e}")
        raise


def writer_json(filename: str = "../data/report.json") -> Any:
    """Декоратор записывает работу функции в JSON-файл."""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "w", encoding="utf-8") as file:
                file.write(result)
            return result

        return wrapper

    return my_decorator


@writer_json()
def json_report(report_list: pd.DataFrame) -> str:
    """Формирует JSON данные для отчетов"""
    data_list = report_list.to_dict(orient="records")
    for i in data_list:
        i["Дата операции"] = str(i["Дата операции"])
        i["Дата платежа"] = str(i["Дата платежа"])

    json_list = json.dumps(data_list)
    return json_list
