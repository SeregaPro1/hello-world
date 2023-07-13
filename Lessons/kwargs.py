# **kwargs =    paremeter that will all arguments into a dictionary
#               useful so that a function cac accept a varying amont of keyword argumets

def hello(**kwargs):
    # print('Hello ' + kwargs['first'] + ' ' + kwargs['last'])
    print('Hello', end=' ')
    for key,value in kwargs.items():
        print(value, end=' ')

hello(title='Mr.',first='Bro',middle='Dude',last='Code')