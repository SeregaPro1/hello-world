# labda function = function written in 1 line using lambda keyword
#                  accepts any number of arguments,but only has one expression
#                  (think of it as a shortcut)
#                  (useful if needed for a short period of time, throw-away)
#
# labda parameters:expression

def double(x):
    return x * 2


print(double(5))

double_2 = lambda y: y * 2

print(double_2(4))
