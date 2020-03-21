import random

def IsInteger(x):
    return int(x) == x 

number = random.randint(1, 6)
print(number)
yournumber = 0
while (yournumber != number):
    try: 
        yournumber = float(input("Choose a number between 1 and 6. "))
        if not IsInteger(yournumber):
            print("Please enter an integer.")
        elif yournumber == number:
            print("Good job, you won!")
        elif yournumber > 6 or yournumber < 1:
            print("Please enter a number between 1 and 6.")
        else:
            print("Nope, try again!")
    except:
        print("Please enter a number.")