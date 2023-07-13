# filter() = creates a collection of elements from an iretable for which a function returns true
#
# fulter(function, iterable)

friends = [('Rachel', 19),
           ('Monica', 18),
           ('Phoebe', 17),
           ('Joey', 16),
           ('Chandler', 21),
           ('Ross', 20)]


def age(data):
    return data[1] >= 18


drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)