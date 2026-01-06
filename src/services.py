import logging
from typing import Any, Dict, List
from src.utils import load_transactions


def investment_bank(month: str, transactions: List[Dict[str, Any]], limit: int) -> float:
    """
    Расчет суммы для Инвесткопилки через округление трат.

    Args:
        month: Месяц в формате 'YYYY-MM'
        transactions: Список транзакций
        limit: Лимит округления (10, 50, 100)

    Returns:
        Сумма для инвесткопилки
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Расчет инвесткопилки для {month} с лимитом {limit}")

    try:
        total_rounding = 0.0

        for transaction in transactions:
            # Дата уже в datetime формате

            trans_date = transaction["Дата операции"]
            if trans_date.strftime("%Y-%m") != month:
                continue

            # Берем только расходы (отрицательные суммы)
            amount = transaction["Сумма операции"]
            if amount >= 0:
                continue

            # Округляем до ближайшего кратного limit
            rounded_amount = round(abs(amount) / limit) * limit
            rounding_diff = rounded_amount - abs(amount)

            if rounding_diff > 0:
                total_rounding += rounding_diff

        logger.info(f"Сумма для инвесткопилки: {total_rounding:.2f}")
        return round(total_rounding, 2)

    except Exception as e:
        logger.error(f"Ошибка расчета инвесткопилки: {e}")
        raise
