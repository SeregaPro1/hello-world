import os

source = 'test2.txt'
destination = 'D:\\test2.txt'

try:
    if os.path.exists(destination):
        print('There is already a file there')
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source + ' was not found')
