# if statement = a block of code that will execute if it's condition is true

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You ate an adult!")
elif age < 0:
    print("You haven't benn born yet!")
else:
    print("You are a child!")