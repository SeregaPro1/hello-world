# Python interpreter sets 'Special variables', one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

# 1. Module can be rus as a standalone program
#   or
# 2. Module can be imported and used by other modules

def main():
    print('Hello')


if __name__ == '__main__':
    main()
