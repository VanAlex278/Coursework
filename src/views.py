import logging
from datetime import datetime
from typing import Any, Dict
from src.utils import json_file_reader
import pandas as pd

from src.api_client import get_currency_rates, get_stock_prices
from src.utils import load_transactions, get_greeting


def main_page(transactions: pd.DataFrame, date_time: str) -> Dict[str, Any]:
    """
    Генерирует JSON для главной страницы.

    Args:
        transactions: DataFrame с транзакциями
        date_time: Дата и время в формате 'YYYY-MM-DD HH:MM:SS'

    Returns:
        JSON данные для главной страницы
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Генерация главной страницы для {date_time}")

    try:
        # Приветствие
        greeting = get_greeting(date_time)

        # Фильтрация транзакций за текущий месяц
        target_date = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
        start_of_month = target_date.replace(day=1, hour=0, minute=0, second=0)

        monthly_transactions = transactions[
            (transactions["Дата операции"] >= start_of_month)
            & (transactions["Дата операции"] <= target_date)
            & (transactions["Статус"] == "OK")
            & (transactions["Номер карты"].notna())
        ]

        # Расчет по картам
        cards_data = []
        for card in monthly_transactions["Номер карты"].unique():
            if pd.isna(card):
                continue
            card_transactions = monthly_transactions[monthly_transactions["Номер карты"] == card]
            total_spent = abs(card_transactions[card_transactions["Сумма операции"] < 0]["Сумма операции"].sum())
            cashback = total_spent * 0.01  # 1% кешбэк

            cards_data.append(
                {
                    "last_digits": str(card).replace("*", "")[-4:],
                    "total_spent": round(float(total_spent), 2),
                    "cashback": round(float(cashback), 2),
                }
            )

        # Топ-5 транзакций по сумме платежа
        top_transactions = monthly_transactions.nlargest(5, "Сумма платежа")[
            ["Дата операции", "Сумма платежа", "Категория", "Описание"]
        ]
        top_transactions_list = []
        for _, transaction in top_transactions.iterrows():
            top_transactions_list.append(
                {
                    "date": transaction["Дата операции"].strftime("%d.%m.%Y"),
                    "amount": round(float(transaction["Сумма платежа"]), 2),
                    "category": transaction["Категория"],
                    "description": transaction["Описание"],
                }
            )

        # API данные
        json_data = json_file_reader()
        currency_rates = get_currency_rates(json_data['user_currencies'])
        stock_prices = get_stock_prices(json_data['user_stocks'])

        page_main = {
            "greeting": greeting,
            "cards": cards_data,
            "top_transactions": top_transactions_list,
            "currency_rates": currency_rates,
            "stock_prices": stock_prices
        }
        return page_main
    except Exception as e:
        logger.error(f"Ошибка генерации главной страницы: {e}")
        raise

if __name__ == "__main__":
    df = load_transactions()
    data_tran = main_page(df, "2021-11-28 14:20:00")
    print(data_tran)
