# map() = applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function, iterable)

store = [('shirt', 20.00),
         ('pants', 25.00),
         ('jacket', 50.00),
         ('socks', 10.00)]


def to_euros(data):
    return data[0], data[1] * 0.82


store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)


def sort1_abc(abc):
    return abc[0]


def sort2_price(price):
    return price[1]


with open('D:\\map.txt', 'a') as file:
    store_euros.sort(key=sort1_abc)
    file.write(str(store_euros))
    store_euros.sort(key=sort2_price)
    file.write(str(store_euros))
