import logging
from datetime import datetime, timedelta
from typing import Optional

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
