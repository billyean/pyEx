import random
import time
import os


def random_char():
    # random pick a character between 'a' to 'z'
    # chr function will return a character which ascii number is given integer.
    p = random.randrange(26)
    return chr(97 + p)


def main():
    select = random_char()
    max_tries = 9
    tries = 0
    while True:
        guess = input("Please guess what the letter is : ")
        if guess == "quit":
            print("OK, bye!")
            break

        tries += 1
        if guess == select:
            print(f"You guessed it in only {tries} tries!")
            break

        if tries == max_tries:
            print(f"Sorry, you didn’t guess it in {max_tries} tries.  The letter was {select}.")
            break

        print(f"That’s not it, try again!  You have {max_tries - tries} guesses left.")
        time.sleep(1)
        os.system('clear')


if __name__ == "__main__":
    main()
