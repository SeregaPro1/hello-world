# dictioncary comprehension = create dictionaries using an expression
#                             can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}

import math

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

cities_in_C = {key: ((value - 32) * 5 / 9).__ceil__() for (key, value) in cities_in_F.items()}
print(cities_in_C)

# ----------------------------------
weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'clody'}

weather_2 = {key: value for (key, value) in weather.items() if value == 'sunny'}
print(weather_2)


def check_temp(value):
    if value >= 70:
        return 'Hot'
    elif 69 >= value >= 40:
        return 'Warm'
    else:
        return 'Cold'


cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)
