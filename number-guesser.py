import random

LowNumber = 1
HighNumber = 10

def IsInteger(x):
    return int(x) == x 

number = random.randint(LowNumber, HighNumber)
yournumber = None
while (yournumber != number):
    try: 
        yournumber = float(input("Choose a number between {} and {}. ".format(LowNumber, HighNumber)))
        if not IsInteger(yournumber):
            print("Please enter an integer.")
        elif yournumber == number:
            print("Good job, you won!")
        elif yournumber > HighNumber or yournumber < LowNumber:
            print("Please enter a number between", LowNumber, "and", HighNumber, ".")
        else:
            print("Nope, try again!")
    except:
        print("Please enter a number.")