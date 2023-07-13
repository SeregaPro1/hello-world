# set = collection which is unordered, unindexed. No duplcate values

utensils = {'fork', 'spoon', 'knife'}
dishes = {'bowl', 'plate', 'cup', 'knife'}

utensils.add('napkin')
utensils.remove('fork')
utensils.clear()
dishes.update(utensils)  # .update = updates the dataset in set
dinner_table = utensils.union(dishes)  # .union = updates the dataset in variable

print(dishes.difference(utensils))  # .difference = remove indentical items in set
print(utensils.intersection(dishes))  # . intersection = show indentical intems in set

for x in dinner_table:
    print(x)
    