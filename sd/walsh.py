import numpy as np


def main():
    while True:
        s = input('Please input station number : ')

        if s == 'quit':
            break;
        try:
            num_of_stations = int(s)

            if num_of_stations <= 0:
                print("Please input a negative integers")

            n = 1
            matrix = np.array([1])

            while n < num_of_stations:
                c = np.hstack((matrix, matrix))
                d = np.hstack((matrix, -matrix))
                matrix = np.vstack((c, d))
                n *= 2

            print("The sequence of stations are ")
            for x in matrix:
                print(x)

            if is_orthogonal(matrix):
                print("Matrix is orthogonal")
        except ValueError as err:
            print("Please input a negative integers")


def is_orthogonal(matrix):
    d = matrix.shape[0]

    for i in range(d):
        for j in range(i + 1, d):
            if np.dot(matrix[i], matrix[i + 1]) != 0:
                return False

    return True


if __name__ == '__main__':
    main()