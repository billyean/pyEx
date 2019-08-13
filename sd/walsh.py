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

        except ValueError as err:
            print("Please input a negative integers")


if __name__ == '__main__':
    main()