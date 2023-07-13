# sort() method =   used with lists
# sort() function = used with iterables

students = [('Squidwad', 'F', 60),
            ('Sandy', 'A', 33),
            ('Patrick', 'D', 36),
            ('Spoongebob', 'B', 20),
            ('Mr.Krabs', 'C', 78)]

# def grade(grades):
#     return grades[2]


def age(age_id):
    return age_id[2]


students.sort(key=age)


# sorted_students = sorted(students, key=grade, reverse=False)

for i in students:
    print(i)