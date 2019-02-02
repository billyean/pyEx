#!/usr/bin/env python3
import re


def exchange(currency_value, rate):
    """Return corresponding currency value by given currency number and exchange rate"""
    return currency_value * rate


# Task 1 Answer
# How much us dollars worth as same as 1,000,000 Venezuelan Bolivars.
bolivars_value = 1000000
us_dollar_value_per_bolivar = 0.016
us_dollars_value = exchange(bolivars_value, us_dollar_value_per_bolivar)
print(f"{bolivars_value} Venezuelan Bolivars has same value as {us_dollars_value:.2f} us dollars.")

# Task 2 Answer
# How many Bolivars you would need to have today to live for the next 3 years if you require $12,060 (US) per year.
living_standard = 12060
period = 3
bolivars_required = exchange(living_standard * period, 1.0 / us_dollar_value_per_bolivar)
print(f"You need {bolivars_required:2f} Venezuelan Bolivars for three years when you live with {living_standard} us dollars a year.")

# Task 3 Answer
# How many minutes there will be in the next 3 years, if there are 365.2425 days in a year. Calculate how many Bolivars
# you would spend per minute, on average
days_per_year = 365.2425
minutes_pre_day = 24 * 60
years = 3
total_minutes = years * days_per_year * minutes_pre_day
print(f"{years} years has {total_minutes:.0f} minutes.")

bolivars_per_minute = bolivars_required / total_minutes
print(f"You need {bolivars_per_minute:.2f} Venezuelan bolivars to survive for every minute.")

# Task 4 Answer
# Create the variable, bloody_vikings, containing the value ‘Wonderful Spam! Glorious Spam!’.
bloody_vikings = 'Wonderful Spam! Glorious Spam!'

# Task 5 Answer
# Create a variable, viking_exclamations, containing a two-item list of the values of the two exclamations in bloody_
# vikings.
exclamation_expr = r'[^!]*!'
viking_exclamations = [x.strip() for x in re.findall(exclamation_expr, bloody_vikings)]
print(viking_exclamations)

# Task 6 Answer
# Create a variable, viking_exaggeration, containing the second value in the list assigned to viking_exclamations.
viking_exaggeration = viking_exclamations[1]
print(viking_exaggeration)

# Task 7 Answer
# Create a variable, upper_exaggeration, containing the completely capitalized (not just the first letter) version of
# the contents of viking_exaggeration.
upper_exaggeration = viking_exaggeration.upper()
print(upper_exaggeration)

# Task 8 Answer
# Create a variable, partial_exaggeration, containing the 4th through 8th characters of the string assigned to
# viking_exaggeration.
partial_exaggeration = upper_exaggeration[3:8]
print(partial_exaggeration)
