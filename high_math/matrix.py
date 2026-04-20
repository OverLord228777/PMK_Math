import numpy as np

# Исходные данные
A = np.array([[1, 2, 3],
              [2,  -1, 1],
              [3, 4, -2]], dtype=float);
B = np.array([12, 9, -6], dtype=float);

def obratnaya_matrica():
    # Метод обратной матрицы
    A_inv = np.linalg.inv(A);
    X_inv = A_inv @ B;
    print(f"Метод обратной матрицы:\nx={X_inv[0]:.2f}, y={X_inv[1]:.2f}, z={X_inv[2]:.2f}");

def kramer():
    # Метод Крамера
    det_A = np.linalg.det(A);
    X_cramer = [];
    for i in range(3):
        Ai = A.copy();
        Ai[:, i] = B;
        X_cramer.append(np.linalg.det(Ai) / det_A);
    print(f"Метод Крамера:\nx={X_cramer[0]:.2f}, y={X_cramer[1]:.2f}, z={X_cramer[2]:.2f}");