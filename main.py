"""
Полномасштабный проект, где есть много мат функций
"""

from numerical_methods.lagrange import Point, Lagrange

l0: Point = Point(0, 3)
l1: Point = Point(5, 1)
l2: Point = Point(2, 4)


expr: str = Lagrange(l0, l1, l2)
print(expr)