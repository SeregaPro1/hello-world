# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression
import os

# slice1 = slice(2, -3)

# foods = list()
# while True:
#     food = input('What food do you like?: ').capitalize()
#     if food == 'Quit':
#         break
#     foods.append(food)
#     print(foods)
#     with open('D:\\test3.txt', 'w') as file:
#         print(file.write(str(foods)), end='')

foods = list()
while food := input('What food do you like?: ') != 'quit':
    foods.append(food)
