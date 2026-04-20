from typing import Callable, Union

def derivative(func: Callable[[float], float],
               x: float,
               method: str = 'central',
               h: float = 1e-6) -> float:
    """
    Численное вычисление первой производной функции func в точке x.

    Параметры:
        func: функция одного аргумента.
        x: точка, в которой вычисляется производная.
        method: метод аппроксимации:
            'forward'  - разностная производная вперёд (O(h));
            'backward' - разностная производная назад (O(h));
            'central'  - центральная разностная производная (O(h^2)).
        h: шаг дифференцирования.

    Возвращает:
        Приближённое значение f'(x).
    """
    if method == 'forward':
        return (func(x + h) - func(x)) / h
    elif method == 'backward':
        return (func(x) - func(x - h)) / h
    elif method == 'central':
        return (func(x + h) - func(x - h)) / (2 * h)
    else:
        raise ValueError("method должен быть 'forward', 'backward' или 'central'")

def second_derivative(func: Callable[[float], float],
                      x: float,
                      h: float = 1e-4) -> float:
    """
    Численное вычисление второй производной функции func в точке x.
    Используется центральная разностная формула второго порядка: (f(x+h) - 2f(x) + f(x-h)) / h^2.
    """
    return (func(x + h) - 2 * func(x) + func(x - h)) / (h * h)

def partial_derivative(func: Callable[..., float],
                       point: list,
                       index: int,
                       h: float = 1e-6) -> float:
    """
    Численное вычисление частной производной функции нескольких переменных
    по аргументу с индексом index в точке point.

    Параметры:
        func: функция, принимающая список (или кортеж) аргументов.
        point: список координат точки.
        index: индекс переменной, по которой берётся производная.
        h: шаг дифференцирования.

    Возвращает:
        Приближённое значение ∂f/∂x_index в точке point.
    """
    point_plus = point[:]
    point_minus = point[:]
    point_plus[index] += h
    point_minus[index] -= h
    return (func(*point_plus) - func(*point_minus)) / (2 * h)