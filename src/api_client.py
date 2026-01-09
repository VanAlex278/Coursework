import os
import logging
import time
from typing import Dict, List
from dotenv import load_dotenv
import requests


def get_currency_rates(currencies: List[str]) -> List[Dict[str, float]]:
    """
    Получает курсы валют от ЦБ РФ.

    Args:
        currencies: Список валют ['USD', 'EUR']

    Returns:
        Список словарей с валютами и курсами
    """
    logger = logging.getLogger(__name__)

    try:
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js", timeout=10)
        response.raise_for_status()

        data = response.json()
        rates = []

        for currency in currencies:
            if currency in data["Valute"]:
                rate = data["Valute"][currency]["Value"]
                rates.append({"currency": currency, "rate": round(rate, 2)})

        logger.info(f"Получены курсы для {len(rates)} валют")
        return rates

    except Exception as e:
        logger.error(f"Ошибка получения курсов валют: {e}")
        return []


def get_stock_prices(stocks: List[str]) -> List[Dict[str, float]]:
    """
    Получает цены акций.

    Args:
        stocks: Список акций ['AAPL', 'GOOGL']

    Returns:
        Список словарей с акциями и ценами
    """
    logger = logging.getLogger(__name__)
    prices = []
    load_dotenv()
    apikey = os.getenv('Alpha_Vantage_API')

    for stock in stocks:
        try:
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey={apikey}'
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()
        except Exception as e:
            logger.error(f"Ошибка получения цен акций: {e}")
            return prices
        time.sleep(1)
        date_of_operation = data['Meta Data']['3. Last Refreshed']
        prices.append({"stock": stock, "price": round(float(data['Time Series (Daily)'][date_of_operation]['4. close']), 2)})

    logger.info(f"Получены цены для {len(prices)} акций")
    return prices



if __name__ == "__main__":
    currency_list = get_currency_rates(['USD', 'EUR'])
    print(currency_list)
    stock_list = get_stock_prices(['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TSLA'])
    print(stock_list)
