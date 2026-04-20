class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def Lagrange(l0: Point, l1: Point, l2: Point) -> str:
    final_expr: str = ""
    denominator0: float = (l0.x - l1.x) * (l0.x - l2.x)
    denominator1: float = (l1.x - l0.x) * (l1.x - l2.x)
    denominator2: float = (l2.x - l0.x) * (l2.x - l1.x)

    sum0: float = l1.x + l2.x
    mul0: float = l1.x * l2.x

    sum1: float = l0.x + l2.x
    mul1: float = l0.x * l2.x

    sum2: float = l0.x + l1.x
    mul2: float = l0.x * l1.x

    x2: float = l0.y / denominator0 + \
                l1.y / denominator1 + \
                l2.y / denominator2
    x: float = l0.y / denominator0 * sum0 + \
               l1.y / denominator1 * sum1 + \
               l2.y / denominator2 * sum2
    c: float = l0.y / denominator0 * mul0 + \
               l1.y / denominator1 * mul1 + \
               l2.y / denominator2 * mul2

    final_expr = f"{x2}x^2 + {x}x + {c}"

    return final_expr