import math
from typing import List

def calculate_average(data: List[float]) -> float:
    """Возвращает среднее арифметическое списка чисел."""
    return sum(data) / len(data)

def absolute_error(true_value: float, approx_value: float) -> float:
    """
    Вычисляет абсолютную погрешность: |true_value - approx_value|.
    """
    return abs(true_value - approx_value)

def relative_error(true_value: float, approx_value: float) -> float:
    """
    Вычисляет относительную погрешность: |true_value - approx_value| / |true_value|.
    Если true_value == 0, возвращает math.inf.
    """
    if true_value == 0:
        return math.inf
    return abs(true_value - approx_value) / abs(true_value)