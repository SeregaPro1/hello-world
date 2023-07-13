# scope = the region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and lacally scope versions of a variable can be created.

name = 'Bro' # global scope(avaible inside and outside functions)

def display_name():
    name = 'Code'    # local scope (available only inside this function)
    print(name)

display_name()
print(name)