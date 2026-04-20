import math
from typing import Optional

def factorial(n: int) -> int:
    """Возвращает факториал числа n (n!)."""
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных целых чисел.")
    return math.factorial(n)

def permutation(n: int, k: Optional[int] = None) -> int:
    """
    Возвращает количество перестановок.
    Если k не указано: P(n) = n!
    Если k указано: P(n, k) = n! / (n - k)! (размещения без повторений).
    """
    if k is None:
        return factorial(n)
    if k < 0 or k > n:
        raise ValueError("k должно быть в диапазоне 0 <= k <= n")
    return factorial(n) // factorial(n - k)

def combination(n: int, k: int) -> int:
    """
    Возвращает количество сочетаний: C(n, k) = n! / (k! * (n - k)!).
    """
    if k < 0 or k > n:
        raise ValueError("k должно быть в диапазоне 0 <= k <= n")
    return factorial(n) // (factorial(k) * factorial(n - k))

def placement(n: int, k: int) -> int:
    """
    Возвращает количество размещений без повторений: A(n, k) = n! / (n - k)!.
    (Синоним permutation(n, k)).
    """
    return permutation(n, k)