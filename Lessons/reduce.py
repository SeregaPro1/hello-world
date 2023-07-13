# reduce() = apply a function to an iterable and reduce it to a single cumulative value
#            performs function an first two elemets and repeats process until 1 value ramains
#
# reduce(function, iterable)

import functools

letters = ['H','B','D','L','L','O']
word = functools.reduce(lambda x, y: x + y,letters)
print(word)

factorial = [5,4,3,2,1]
results = functools.reduce(lambda x, y: x * y, factorial)
print(results)