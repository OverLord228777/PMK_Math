import numpy as np

def Seidel(A, b, x0=None, tol=0.005, maxIter=1000):
    """
    Решение СЛАУ методом Гаусса–Зейделя.

    :param A: матрица коэффициентов (квадратная)
    :param b: вектор правой части
    :param x0: начальное приближение (если None — нулевой вектор)
    :param tol: допустимая погрешность (по норме inf)
    :param maxIter: максимальное число итераций
    :return:
        x: вектор решения
        k+1: количество выполненных итераций
    """
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    x = x0.copy().astype(float)

    if np.any(np.diag(A) == 0):
        raise ValueError("Метод Зейделя требует ненулевых диагональных элементов")

    for k in range(maxIter):
        x_new = x.copy()
        for i in range(n):
            # Сумма произведений уже обновлённых (j < i) и старых (j > i) компонент
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        diff = np.linalg.norm(x_new - x, ord=np.inf)
        if diff < tol:
            print(f"Итерация {k + 1}: x = {x_new}")
            return x_new, k + 1

        x = x_new

    return x, maxIter