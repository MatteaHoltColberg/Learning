import math

# Asks the user for the two numbers.
x = int(input("Enter number x: "))
y = int(input("Enter number y: "))

# Tells the user the value of the first number raised to the second.
print("x**y = {}".format(pow(x, y)))
# Tells the user the log base 2 value of the first number.
print("log(x) = {}".format(math.log(x, 2)))
