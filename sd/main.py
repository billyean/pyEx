import sqlite3
import time
import os
from schedule.scheduler import Scheduler
from datetime import datetime, date, timedelta


def show_main_menu():
    """Showing main menu by menus"""
    os.system('clear')
    print('\tMAIN MENU')
    print('\n\t---------------------------------------------------\n')
    print('\t1. Create a customer.')
    print('\t2. Look up customer''s amount due.')
    print('\t3. Look up next available service time.')
    print('\t4. Make an appointment. ')
    print('\t5. Display customers. ')
    print('\n\t0. Quit to system. \n')


def customer_due(scheduler):
    os.system('clear')

    while True:
        customer_name = input('Please input customer name here : ')
        customer_name = ' '.join([x.capitalize() for x in customer_name.split(' ')])
        customer = scheduler.lookup_customer(customer_name)
        if customer is not None:
            break
        print("No customer found, please try again.")
    amount_due = scheduler.amount_due(customer)

    print('\n\t---------------------------------------------------')
    print(f'\t{customer_name} has total ${amount_due} on due.')
    print('\t---------------------------------------------------\n')


def availability(scheduler):
    time.sleep(1)
    os.system('clear')
    available_time = scheduler.available()

    if len(available_time) == 0:
        print("No available service in next two weeks, please check back later.")
    else:
        wash_service = available_time[0]
        print(f"Next available wash service is {wash_service[0]} at {wash_service[1]}")
        cut_service = available_time[1]
        print(f"Next available cut service is {cut_service[0]} at {cut_service[1]}")


def make_appointment(scheduler):
    os.system('clear')
    while True:
        customer_name = input('Please input customer name here : ')
        customer = scheduler.lookup_customer(customer_name)
        if customer is not None:
            break
        print("No customer found, please try again.")

    while True:
        wash_service_choice = input('Please select wash service you want to have(1. fancy 2. no nonsense) : ')
        if wash_service_choice == '1':
            wash_service = 'fancy'
            break
        if wash_service_choice == '2':
            wash_service = 'no nonsense'
            break
        print("Invalid input for wash service, please try again.")

    while True:
        wash_service_time = input('Please input the date time you want to have wash service(yyyy-mm-dd hh:mm) : ')
        try:
            wash_datetime = datetime.strptime(wash_service_time, '%Y-%m-%d %H:%M')
            wash_date = wash_datetime.date()
            wash_time = wash_datetime.time()

            if wash_date.weekday() > 4:
                raise ValueError("You have choose a service date at weekend")

            if wash_time.hour < 8 or wash_time.hour > 16 or wash_time.hour == 12:
                raise ValueError("You have choose a non-working hour")

            if wash_time.minute != 0 and wash_time.minute != 30:
                raise ValueError("Service time must be 30 minutes each")

            today = date.today()
            if today.weekday() == 4:
                next_week_day = today + timedelta(days=3)
            else:
                next_week_day = today + timedelta(days=1)
            service_day_diff = (wash_date - next_week_day).days

            if service_day_diff < 0 or service_day_diff >= 14:
                raise ValueError("You can only make an appointment in next 2 weeks")
            break
        except ValueError as err:
            print(f"{err} - Invalid wash time format, please try again.")

    while True:
        cut_service_choice = input('Please select cut service (1.teddy 2.lion 3.summer 4.weed whacker) : ')
        if cut_service_choice == '1':
            cut_service = 'teddy'
            break
        if cut_service_choice == '2':
            cut_service = 'lion'
            break
        if cut_service_choice == '3':
            cut_service = 'summer'
            break
        if cut_service_choice == '4':
            cut_service = 'weed whacker'
            break
        print("Invalid input for cut service, please try again.")

    while True:
        cut_service_time = input('Please input the date time you want to have cut service(yyyy-mm-dd hh:mm) : ')
        try:
            cut_datetime = datetime.strptime(cut_service_time, '%Y-%m-%d %H:%M')
            cut_date = cut_datetime.date()
            cut_time = cut_datetime.time()

            if cut_date.weekday() > 4:
                raise ValueError("You have choose a service date at weekend")

            if cut_time.hour < 8 or cut_time.hour > 16 or cut_time.hour == 12:

                raise ValueError("You have choose a non-working hour")

            if cut_time.minute != 0 and cut_time.minute != 30:
                raise ValueError("Service time must be 30 minutes each")

            today = date.today()
            if today.weekday() == 4:
                next_week_day = today + timedelta(days=3)
            else:
                next_week_day = today + timedelta(days=1)
            service_day_diff = (cut_date - next_week_day).days
            if service_day_diff < 0 or service_day_diff >= 14:
                raise ValueError("You can only make an appointment in next 2 weeks.")
            break
        except ValueError as err:
            print(f"Invalid cut time format {err}, please try again.")

    try:
        scheduler.make_appointment(customer, wash_datetime, wash_service, cut_datetime, cut_service)
    except ValueError as err:
        print(f'{err}, please try another time.')


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
        security_code = input('Credit card security code:  ')
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
    conn = sqlite3.connect('db.sqlite3', detect_types=sqlite3.PARSE_DECLTYPES)
    scheduler = Scheduler(conn)

    try:
        while True:
            show_main_menu()
            choice = input('Enter the number for your choice:')

            if choice == '0':
                print('Quit to scheduler...')
                break
            elif choice == '1':
                add_customer(scheduler)
            elif choice == '2':
                customer_due(scheduler)
            elif choice == '3':
                availability(scheduler)
            elif choice == '4':
                make_appointment(scheduler)
            elif choice == '5':
                make_appointment(scheduler)
            print('Invalid choice on menu, please try again.')
    except EOFError as err:
        print("You chose to quit the system")
    finally:
        conn.commit()
        conn.close()


if __name__ == "__main__":
    main()
