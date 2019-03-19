import numpy as np

if __name__ == "__main__":
    found = False
    n = 3
    p = 2

    while not found:
        A = np.identity(n)
        powers = []
        for a in range(0, p):
            for b in range(0, p):
                for c in range(0, p):
                    A[0, 1] = a
                    A[0, 2] = b
                    A[1, 2] = c
                    powers.append(np.array_equal(np.mod(np.linalg.matrix_power(A, 3), p), np.identity(n)))
        if all(powers):
            found = True
            print(p)
        p += 1
