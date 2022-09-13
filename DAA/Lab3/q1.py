import numpy as np


def strassen_algorithm(x, y):
    if x.size == 1 or y.size == 1:
        return x * y

    n = x.shape[0]

    if n % 2 == 1:
        x = np.pad(x, (0, 1), mode='constant')
        y = np.pad(y, (0, 1), mode='constant')

    m = int(np.ceil(n / 2))
    a = x[:m, :m]
    b = x[:m, m:]
    c = x[m:, :m]
    d = x[m:, m:]
    e = y[:m, :m]
    f = y[:m, m:]
    g = y[m:, :m]
    h = y[m:, m:]
    p1 = strassen_algorithm(a, f - h)
    p2 = strassen_algorithm(a + b, h)
    p3 = strassen_algorithm(c + d, e)
    p4 = strassen_algorithm(d, g - e)
    p5 = strassen_algorithm(a + d, e + h)
    p6 = strassen_algorithm(b - d, g + h)
    p7 = strassen_algorithm(a - c, e + f)
    result = np.zeros((2 * m, 2 * m), dtype=np.int32)
    result[:m, :m] = p5 + p4 - p2 + p6
    result[:m, m:] = p1 + p2
    result[m:, :m] = p3 + p4
    result[m:, m:] = p1 + p5 - p3 - p7

    return result[:n, :n]


if __name__ == "__main__":

    x = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    y = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])
    print('Matrix multiplication result: ')
    print(strassen_algorithm(x, y))

"""
    -Divide matrix A and matrix B in 4 sub-matrices of size N/2 x N/2 as shown in the above diagram.
    -Calculate the 7 matrix multiplications recursively.
    -Compute the submatrices of C.
    -Combine these submatricies into our new matrix C
    ==================================================
    The time complexity using the Master Theorem.

    T(n) = 7T(n/2) + O(n^2) = O(n^log(7)) runtime.

    Approximately O(n^2.8074) which is better than O(n^3)
    ===================================================
    Worst case time complexity: Θ(n^2.8074)
    Best case time complexity: Θ(1)
    Space complexity: Θ(logn)
"""