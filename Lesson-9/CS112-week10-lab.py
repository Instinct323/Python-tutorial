import numpy as np
import scipy


def Q1():
    # shape: (3, 5)
    # axis 0: 3
    # axis 1: 5
    x = np.random.rand(3, 5)
    print("array:\n", x)
    print("sum of all the entries: \tx.sum() =\t", x.sum())
    # axis=1: sum of each row (5 elements)
    print("sum of each row: \tx.sum(axis=1) =\t", x.sum(axis=1))
    # axis=0: sum of each column (3 elements)
    print("sum of each column: \tx.sum(axis=0) =\t", x.sum(axis=0))


def Q2_wrong():
    x = np.arange(5)
    print("x =\n", x)
    # transpose is not possible for 1D array
    print("x.T =\n", x.T)
    print("x + x.T =\n", x + x.T)

    print("\033[31m[WARNING] transpose is not possible for 1D array\033[0m")


def Q2():
    Q2_wrong()
    # create a 2D array
    # method 1
    x = np.arange(5)[None]
    # method 2
    x = np.arange(5).reshape(1, -1)

    print("x =\n", x)
    print("x.T =\n", x.T)
    print("x + x.T =\n", x + x.T)


def Q3():
    # From 2 numpy arrays, extract the indexes in which the elements in the 2 arrays match
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 3, 2, 4, 5])
    tmp = np.where(a == b)
    print(f"tmp: {type(tmp)} = {tmp}")
    # np.where returns a tuple, the first element is the result
    result = tmp[0]
    print(f"result: {type(result)} = {result}")


def Q4():
    # Write a program that can place 3 ones randomly into a 4x4 array of zeros
    x = np.zeros(16, dtype=np.float16)
    pos = np.random.choice(16, 3, replace=False)
    print("pos:", pos)
    x[pos] = 1
    print("result:\n", x.reshape(4, 4))


def Q5():
    A = np.array([[8, 3, -3],
                  [-2, -8, 5],
                  [3, 5, 10]])
    b = np.array([14, 5, -8])
    # method 1
    print("closed form:", np.linalg.inv(A) @ b)  # np.dot(np.linalg.inv(A), b)
    # method 2
    print("scipy.linalg.solve:", scipy.linalg.solve(A, b))
    # method 3
    print("np.linalg.solve:", np.linalg.solve(A, b))


if __name__ == '__main__':
    Q1()
