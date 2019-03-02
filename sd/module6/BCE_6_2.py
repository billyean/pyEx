import datetime


def main():
    start = datetime.datetime.now()
    today = datetime.date.today()

    with open('hiring_data.txt', 'rt', encoding='utf-8') as hirind_data_f:
        hiring_data_lines = [line for line in hirind_data_f]

        with open('BCE_6_2_out.txt', 'wt', encoding='utf-8') as output_f:
            print(f'{start} Start execution', file=output_f)
            print(file=output_f)
            print('Id     Days', file=output_f)

            number_before_operation = 0
            for line in hiring_data_lines:
                data = line.split(' ')
                id = data[0]
                hire_date = datetime.date.fromisoformat(data[1])
                how_many = datetime.date.today() - hire_date
                print(f'{id:6} {how_many.days:4}', file=output_f)

                if hire_date < datetime.date.fromisoformat('2018-02-01'):
                    number_before_operation = number_before_operation + 1

            print(file=output_f)
            line = f'There are {number_before_operation} people who joined before the date that the organization started operations'
            print(line, file=output_f)
            cost_time = datetime.datetime.now() - start
            print(f'Total execution takes {cost_time.seconds}.{cost_time.microseconds} seconds', file=output_f)


if __name__ == "__main__":
    main()