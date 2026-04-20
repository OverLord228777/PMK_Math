import numpy as np

def SimpleIteration(A, b, x0=None, tau=0.1, tol=0.005, maxIter=1000):
    """
    Решение СЛАУ методом простых итераций:
        x_{k+1} = x_k - tau * (A x_k - b)

    :param A: матрица коэффициентов
    :param b: вектор правой части
    :param x0: начальное приближение
    :param tau: параметр сходимости (шаг)
    :param tol: допустимая погрешность (норма inf)
    :param maxIter: максимальное число итераций
    :return:
        x: вектор решения
        k+1: число итераций
    """
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    x = x0.copy().astype(float)

    for k in range(maxIter):
        residual = A @ x - b
        x_new = x - tau * residual

        diff = np.linalg.norm(x_new - x, ord=np.inf)
        if diff < tol:
            print(f"Итерация {k + 1}: x = {x_new}")
            return x_new, k + 1

        x = x_new

    return x, maxIter