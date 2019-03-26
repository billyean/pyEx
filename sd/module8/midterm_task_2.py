import time
import os


def main():
    lower = 0
    upper = 25
    n = 0
    while True:
        medium = (lower + upper) // 2
        c = chr(97 + medium)
        n += 1
        print(f'Computer guess {c}')
        answer = input('1. Right! 2. Too low 3. Too High! -  ')
        if answer == '1':
            print(f'Hooray for me!  I only took {n} guesses!')
            break
        if answer == '2':
            lower = medium + 1
        if answer == '3':
            upper = medium - 1
        time.sleep(1)
        os.system('clear')


if __name__ == "__main__":
    main()
