import math
from typing import Callable, Optional, Union


def lim(func: Callable[[float], float],
        x0: float,
        direction: str = 'both',
        epsilon: float = 1e-6,
        delta: float = 1e-5) -> Optional[float]:
    """
    Численное вычисление предела функции func(x) при x -> x0.

    Параметры:
        func: функция одного аргумента.
        x0: точка, к которой стремится x.
        direction: направление подхода:
            'both'   - двусторонний предел (если односторонние совпадают);
            'left'   - предел слева;
            'right'  - предел справа.
        epsilon: требуемая точность оценки предела.
        delta: начальный шаг приближения к x0.

    Возвращает:
        Значение предела или None, если двусторонний предел не существует.
    """

    def approach(step_sign: int) -> Optional[float]:
        """Вычисление одностороннего предела с заданным знаком шага."""
        x = x0 + step_sign * delta
        prev_value = func(x)
        while True:
            delta_step = delta
            while True:
                x = x0 + step_sign * delta_step
                curr_value = func(x)
                if abs(curr_value - prev_value) < epsilon:
                    # Достигнута стабилизация с текущим шагом
                    break
                prev_value = curr_value
                delta_step /= 2.0
                if delta_step < 1e-12:
                    break
            if delta_step < 1e-12 or abs(curr_value - prev_value) < epsilon:
                return curr_value
            delta = delta_step
            prev_value = curr_value

    if direction == 'left':
        return approach(-1)
    elif direction == 'right':
        return approach(1)
    elif direction == 'both':
        left = approach(-1)
        right = approach(1)
        if left is not None and right is not None and math.isclose(left, right, rel_tol=epsilon):
            return (left + right) / 2.0
        else:
            return None  # двусторонний предел не существует
    else:
        raise ValueError("direction должен быть 'left', 'right' или 'both'")