from unittest.mock import patch

from src.api_client import get_stock_prices, get_currency_rates


# @patch('requests.get')
# def test_get_currency_rates(mock_get):
#     mock_get.return_value.respons.json.return_value = {'Valute': {'USD': {'Value': 78.2267}, 'EUR': {'Value': 92.0938}}}
#
#     assert get_currency_rates(['Test']) == [{'currency': 'USD', 'rate': 78.23}, {'currency': 'EUR', 'rate': 92.09}]


# @patch('requests.get')
# def test_get_stock_prices(mock_get):
#     mock_get.return_value.json.return_value = {'Meta Data': {'3. Last Refreshed': '2025-12-31'},
#                                                'Time Series (Daily)': {'2025-12-31': {'4. close': '271.8600'}}}
#     assert get_stock_prices(['Test']) == '271.8600'