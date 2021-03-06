import os
import time
import sys
from datetime import datetime


def main():
    # Converts the values from the file midterm_input.txt into a dictionary of lists, with each key being ID # and
    # each value being an in-date/out-date list.
    with open('midterm_input.txt', 'rt') as inputf:
        lines = inputf.readlines()
        split = [line.split() for line in lines]
        id2_in_out_date = {split_line[0]: [split_line[1], split_line[2]] for split_line in split}

    # Changes the in-date for ID # 003 to 2019/03/29
    id2_in_out_date['003'][0] = '2019/03/29'

    # Changes the out-date for ID # 002 to 2019/03/31
    id2_in_out_date['002'][1] = '2019/03/31'

    # Displays the prompt, ‘What is the customer’s ID?’, and then accepts a valid customer ID as input.  A valid
    # customer ID contains a 3-digit numeric value.  If the input is not valid, the prompt must be redisplayed, and new
    # input obtained.  If the input is ‘000’, the program exits, otherwise repeat this until a valid ID # is entered.
    while True:
        select = input('What is the customer’s ID?  ')
        if select == '000':
            time.sleep(3)
            os.system("clear")
            sys.exit()
            break

        # Displays the in-date and out-date for the ID # accepted in part e, above (with appropriate labels provided).
        # If the ID # is not in the dictionary, displays ‘ID # not found’.
        if select not in id2_in_out_date:
            print(f"ID {select} not found")
            time.sleep(1)
            os.system("clear")
        else:
            print(f"ID : {select}; In Date: {id2_in_out_date[select][0]}; Out Date: {id2_in_out_date[select][1]}")
            time.sleep(2)
            break
    print()

    # Displays the ID # (or ID #’s) for the longest period from in-date to out-date, inclusive, as well as the
    # length of the period (with appropriate labels provided).
    max_period = 0
    max_period_ids = []

    for idn in id2_in_out_date:
        (in_date, out_date) = id2_in_out_date[idn]
        p = (datetime.strptime(out_date, '%Y/%m/%d') - datetime.strptime(in_date, '%Y/%m/%d')).days + 1
        if p > max_period:
            max_period = p
            max_period_ids = [idn]
        elif p == max_period:
            max_period_ids.append(idn)

    for max_period_id in max_period_ids:
        (in_date, out_date) = id2_in_out_date[max_period_id]
        print(f"ID: {max_period_id}; In Date: {in_date}; Out Date: {out_date} has longest period {max_period} days")
    print()

    # Adds a new entry to the dictionary key = 005, value = [2019/03/24, 2019/04/04]
    id2_in_out_date['005'] = ['2019/03/24', '2019/04/04']

    # Displays all the values in the dictionary (with appropriate labels provided)
    for idn in id2_in_out_date:
        print(f"ID : {idn}; In Date: {id2_in_out_date[idn][0]}; Out Date: {id2_in_out_date[idn][1]}")

    # Writes the values in the dictionary to the file midterm_output.txt.
    with open('midterm_output.txt', 'wt') as outputf:
        for idn in id2_in_out_date:
            print(f"{idn}\t{id2_in_out_date[idn][0]}\t{id2_in_out_date[idn][1]}", file=outputf)


if __name__ == "__main__":
    main()
