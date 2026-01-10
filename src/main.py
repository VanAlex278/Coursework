import logging

from src.reports import json_report, spending_by_category
from src.services import investment_bank
from src.utils import load_transactions, setup_logging
from src.views import json_answer, main_page


def main() -> None:
    """Основная функция приложения."""
    print("=== ЗАПУСК ПРОГРАММЫ ===")
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        # 1. Создаем или загружаем данные
        print("1. Подготовка данных...")
        transactions = load_transactions()
        print(f"   Загружено транзакций: {len(transactions)}")

        # 2. Главная страница
        print("2. Генерация главной страницы...")
        result = main_page(transactions, "2020-01-15 14:30:00")
        print(f"   Приветствие: {result['greeting']}")
        print(f"   Карт обработано: {len(result['cards'])}")
        print(f"   Топ транзакций: {len(result['top_transactions'])}")
        print(f"   Курсы валют: {len(result['currency_rates'])}")
        print(f"   Цены акций: {len(result['stock_prices'])}")
        # Передача JSON-ответа на веб-сайт
        json_answer(result)

        # 3. Сервис Инвесткопилка
        print("3. Расчет инвесткопилки...")
        invest_amount = investment_bank(month="2020-01", transactions=transactions.to_dict("records"), limit=50)
        print(f"   Сумма для инвесткопилки: {invest_amount} руб.")

        # 4. Отчет по категории
        print("4. Формирование отчета...")
        category_report = spending_by_category(transactions=transactions, category="Супермаркеты", date="2020-01-15")
        print(f"   Найдено транзакций: {len(category_report)}")
        print(category_report)
        # Передача JSON-ответа на веб-сайт
        json_report(category_report)
        print("=== ПРОГРАММА УСПЕШНО ЗАВЕРШЕНА ===")

    except Exception as e:
        print(f"!!! ОШИБКА: {e}")
        logger.error(f"Ошибка в приложении: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
