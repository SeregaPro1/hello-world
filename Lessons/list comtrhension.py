# list comprehension =  a way to create a new with less syntax
#                       can mimic certain lambda functions, easier to read


students = [100, 90, 80, 70, 60, 50, 40, 30, 0]


def score(x):
    if x >= 60:
        return 1
    else:
        print('Failed')


passed_students1 = list(filter(score, students))

passed_students2 = [i if i >= 60 else 'F' for i in students]

passed_students3 = [i for i in students if i >= 60]

print(passed_students1)
print(passed_students2)
print(passed_students3)