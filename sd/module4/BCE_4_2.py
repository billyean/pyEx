import sys

menus = (
    ('scones', 'quesadillas', 'veg lasagna'),
    ('oatmeal', 'veg burgers', 'veg chili'),
    ('pancakes', 'salad', 'veg curry'),
    ('croissants', 'burritos', 'pad thai'),
    ('waffles', 'calzones', 'pizza'),
    ('brownies', 'veg kabobs', 'broccoli quiche'),
    ('eggs', 'tortas', 'penne with pesto')
)

weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

meals = ['breakfast', 'lunch', 'dinner']

menu_dict = {weekdays[row[0]]: {meals[x[0]]: x[1] for x in enumerate(row[1])} for row in enumerate(menus)}


def main(argv):
    if len(argv) != 3:
        print("Usage python BCE_4.2.py Weekday meal")
        print(f"Weekday: {weekdays}")
        print(f"Meal: {meals}")
        return
    elif argv[1] not in weekdays or argv[2] not in meals:
        print('Please input correct weekday or meal')
        return

    special = menu_dict[argv[1]][argv[2]]
    print(f"The special for Friday dinner will be {special}.")


if __name__ == "__main__":
    main(sys.argv)

