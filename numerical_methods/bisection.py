import math
from typing import List

def evaluate(expr: str, x: float) -> float:
    """
    Безопасное вычисление математического выражения с переменной x.
    Доступны все функции модуля math и арифметические операции.
    """
    allowed = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    allowed["x"] = x
    # Запрещаем встроенные функции и конструкции Python
    return eval(expr, {"__builtins__": {}}, allowed)


def bisection(expr: str, epsilon: float,
              start: float = -50.0, end: float = 50.0,
              step: float = 0.5) -> List[float]:
    """
    Находит корни функции на интервале [start, end] с шагом step,
    затем уточняет их методом бисекции с точностью epsilon.
    Возвращает список корней.
    """
    roots: List[float] = []
    intervals: List[tuple[float, float]] = []

    # Поиск интервалов со сменой знака
    prev_x = start
    prev_f = evaluate(expr, prev_x)

    x = start + step
    while x <= end:
        curr_f = evaluate(expr, x)
        if prev_f * curr_f <= 0:
            intervals.append((prev_x, x))
        prev_x, prev_f = x, curr_f
        x += step

    # Уточнение корней на каждом интервале
    for a, b in intervals:
        fa = evaluate(expr, a)
        fb = evaluate(expr, b)

        if fa == 0.0:
            roots.append(a)
            continue
        if fb == 0.0:
            roots.append(b)
            continue
        if fa * fb > 0:
            continue  # нет гарантии корня (защита от ошибок)

        # Метод бисекции
        c = (a + b) / 2.0
        fc = evaluate(expr, c)

        while abs(b - a) > epsilon and abs(fc) > epsilon:
            if fc == 0.0:
                break
            if fa * fc > 0:
                a, fa = c, fc
            else:
                b, fb = c, fc
            c = (a + b) / 2.0
            fc = evaluate(expr, c)

        roots.append(c)

    return roots