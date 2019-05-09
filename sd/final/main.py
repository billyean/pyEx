import sqlite3
import time
import os
from final.scheduler import Scheduler


def prepare_data(conn):
    curs = conn.cursor()

    try:
        services = [("fancy", True, 45),
                    ("no nonsense", True, 20),
                    ("teddy", False, 45),
                    ("lion", False, 45),
                    ("summer", False, 35),
                    ("weed whacker", False, 20)]
        curs.executemany('INSERT INTO schedule_service(name, wash, rate) VALUES (?)', services)

        conn.commit()
    except sqlite3.Error as err:
        print(err)
        conn.rollback()


def menus():
    """
    :return: a dict for showing menu's title, corresponding answer and the flag that quit from the program if it's True
    """
    return {
        1: {
            'function': 'New Customer',
            'quit': False,
            'query': False
        },
        2: {
            'function': 'Available Appointment',
            'quit': False,
            'query': True,
        },
        3: {
            'function': 'Make Appointment',
            'quit': False,
            'query': True
        },
        3: {
            'function': 'Amount Due',
            'quit': False,
            'query': True
        },
        5: {
            'function': 'Quit',
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


def customer_due(scheduler):
    time.sleep(1)
    os.system('clear')
    print('Please input customer name: ')


def customer_due(scheduler):
    time.sleep(1)
    os.system('clear')
    print('Please input customer name: ')



def add_customer(scheduler):
    """
    :param scheduler: schedul
    :return:
    """
    time.sleep(1)
    os.system('clear')
    print('Please input customer info here: ')
    customer_name = input('Customer name     :  ')
    customer_pet = input('Customer pet name :  ')

    while True:
        credit_card = input('Credit card number:  ')
        try:
            int_card = int(credit_card)
            if len(credit_card) != 16:
                raise ValueError('Credit card number should be 16 digits')
            break
        except ValueError as err:
            print('Invalid card number, please try again')

    name_on_card = input('Name on the card  :  ')
    while True:
        expired_date_year = input('Expired Year  :  ')
        try:
            int_year = int(expired_date_year)
            if int_year < 2018 or int_year > 2100:
                raise ValueError('Expired year should between [2018, 2100]')
            break
        except ValueError as err:
            print('Invalid expired year')

    while True:
        expired_date_month = input('Expired Month :  ')
        try:
            int_month = int(expired_date_month)
            if int_month < 1 or int_month > 12:
                raise ValueError('Expired month should between [1, 12]')
            break
        except ValueError as err:
            print('Invalid expired month')

    while True:
        security_code = input('Credit card number:  ')
        try:
            int_code = int(security_code)
            if len(security_code) != 4 and len(security_code) != 3:
                raise ValueError('Security code should be 3 digits or 4 digits')
            break
        except ValueError as err:
            print('Invalid security code, please try again')

    scheduler.add_customer(customer_name, customer_pet, credit_card, name_on_card, expired_date_year + expired_date_month,
                           security_code)


def main():
    conn = sqlite3.connect('db.sqlite3')
    prepare_data(conn)

    scheduler = Scheduler(conn)

    while True:
        select = input('Enter the number for your choice:')



if __name__ == "__main__":
    main()