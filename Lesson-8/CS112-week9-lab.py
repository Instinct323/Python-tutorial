import numpy as np


def Q1():
    # Create a 10x10 array of zeros
    array = np.zeros((10, 10), dtype=np.float16)

    # Add a border of ones around the array
    array[0, :] = 1  # Top row
    array[-1, :] = 1  # Bottom row
    array[:, 0] = 1  # Left column
    array[:, -1] = 1  # Right column

    # Print the result
    print(array)


def Q2():
    y = np.array([0., 1.3, 5., 10.9, 18.9, 28.7, 40.])
    t = np.array([0., 0.49, 1., 1.5, 2.08, 2.55, 3.2])

    # Calculate the average velocity between each time step
    velocity = np.diff(y) / np.diff(t)

    # Print the result
    print(velocity)


def Q3():
    # Create an 8x8 zero matrix
    checkerboard = np.zeros((8, 8), dtype=int)

    # Fill the matrix with a checkerboard pattern
    checkerboard[1::2, ::2] = 1  # Fill 1 at every other position in odd rows
    checkerboard[::2, 1::2] = 1  # Fill 1 at every other position in even rows

    # Print the result
    print(checkerboard)


if __name__ == '__main__':
    Q1()
