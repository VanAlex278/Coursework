import json
import logging
from datetime import datetime
from json import JSONDecodeError

import pandas as pd


def setup_logging() -> None:
    """Настройка логирования."""
    logging.basicConfig(
        level=logging.INFO,
        filename="../data/app.log",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        encoding="utf-8",
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


def json_file_reader(path_to_file: str = "../data/user_settings.json") -> dict[str, list[str]]:
    """Функция чтения Json-файла возвращает список словарей с данными"""
    try:
        with open(path_to_file, encoding="utf-8") as f:
            list_json = json.load(f)
            logging.info(f"Файл загружен: {path_to_file}")
            return list_json
    except (FileNotFoundError, JSONDecodeError) as e:
        logging.error(f"Файл отсутствует или поврежден! {e}")
        return {"user_currencies": ["USD", "EUR"], "user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]}


if __name__ == "__main__":
    # print(get_greeting("2024-11-01 14:20:00"))
    # df = load_transactions()
    # print(df.shape)
    json_data = json_file_reader()
    print(json_data["user_currencies"])
    print(json_data["user_stocks"])
