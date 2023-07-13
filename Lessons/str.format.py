# str.format() = optinal method that gives users
#                more control when displaying ouput

# animal = 'cow'
# item = 'moon'

# print('The ' + animal+' jumped over the '+item)
# print('The {} jumped over the {}'.format(animal,item))
# print('The {1} jumped over the {0}'.format(animal,item)) # positional argument
# print('The {animal} jumped over the {item}'.format(animal='cow',item='moon')) # keyword argument

# text = 'The {} jumperd over the {}'
# print(text.format(animal,item))

# name = 'Bro'
#
# print('Helo, my name is {}'.format(name))
# print('Helo, my name is {:10}. Nice to meet you'.format(name))
# print('Helo, my name is {:<10}. Nice to meet you'.format(name))
# print('Helo, my name is {:>10}. Nice to meet you'.format(name))
# print('Helo, my name is {:^10}. Nice to meet you'.format(name))

number = 1000

print('The number pi is {:.2f}'.format(number))
print('The number is {:,}'.format(number))
print('The number is {:b}'.format(number))
print('The number is {:o}'.format(number))
print('The number is {:x}'.format(number))
print('The number is {:e}'.format(number))