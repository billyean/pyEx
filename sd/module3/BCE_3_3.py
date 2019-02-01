#!/usr/bin/env python3


def menus():
    """
    :return: a dict for showing menu's title, corresponding answer and the flag that quit from the program if it's True
    """
    return {
        1: {
            'title': 'List the best musical group ever',
            'answer': 'The Beatles are the best ever',
            'quit': False
        },
        2: {
            'title': 'List the best sports team ever',
            'answer': 'The Cubs are the best ever',
            'quit': False
        },
        3: {
            'title': 'Quit',
            'answer': 'OK!  Hope you learned something.',
            'quit': True
        }
    }


def show_main_menu():
    """Showing main menu by menus"""
    showing_menus = menus()
    print('MAIN MENU')
    for i in range(1, len(showing_menus) + 1):
        title = showing_menus[i]['title']
        print(f'{i}. - {title}')


def main():
    show_main_menu()

    showing_menus = menus()
    while True:
        try:
            select = int(input('Enter the number for your choice:'))

            if select in showing_menus:
                answer = showing_menus[select]['answer']
                quit = showing_menus[select]['quit']
                print(answer)
                if quit:
                    break
            else:
                print('That’s not one of the choices. Try again.')
        except:
            print('That’s not one of the choices. Try again.')



if __name__ == "__main__":
    main()
