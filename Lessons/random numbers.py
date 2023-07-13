import random

x = random.randint(1,100) # random integer number
y = random.random() # random 0 to 1 float

myList = ['rock','paper','scissors']
z = random.choice(myList) # random to need list

cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']

random.shuffle(cards) # radom pozition in a list

print(z)