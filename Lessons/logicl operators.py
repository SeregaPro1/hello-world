# logical operators (and,or,not) = used to check if two ot more conditional statement
temp = int(input("What is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today!")
    print("stay inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("go outside!")

