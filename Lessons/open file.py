
# try:
#     with open('D:\\test.txt') as file:
#         a = 'You best in the world!'
#         file.write(a)
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found :(")

text = "  "

with open('D:\\test.txt', 'a') as file:
    print(file.write(text))
with open('D:\\test.txt') as file:
    print(file.read())