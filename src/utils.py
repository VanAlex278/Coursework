import logging
from datetime import datetime

import pandas as pd


def setup_logging() -> None:
    """Настройка логирования."""
    logging.basicConfig(
        level=logging.INFO,
        filename="../data/app.log",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )


def load_transactions(file_path: str = "../data/operations.xlsx") -> pd.DataFrame:
    """
    Загрузка транзакций из Excel файла.
    """
    try:
        df = pd.read_excel(file_path)
        df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
        df["Номер карты"] = df["Номер карты"].astype(str)
        logging.info(f"Успешно загружено {len(df)} транзакций")
        return df
    except Exception as e:
        logging.error(f"Ошибка загрузки файла {file_path}: {e}")
        # ВОЗВРАЩАЕМ ПУСТОЙ DATAFRAME ВМЕСТО None
        return pd.DataFrame()


def get_greeting(time_str: str) -> str:
    """
    Определение приветствия по времени.

    Args:
        time_str: Время в формате 'YYYY-MM-DD HH:MM:SS'

    Returns:
        Приветствие: Доброе утро/день/вечер/ночь
    """
    time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    hour = time.hour

    if 5 <= hour < 10:
        return "Доброе утро"
    elif 10 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"

if __name__ == "__main__":
    print(get_greeting("2024-11-01 14:20:00"))
    print(load_transactions)