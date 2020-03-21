import random

balance = 10


def printAmountOfNumbers(x):
    for i in range(x):
        sum = 0
        for ii in range(i + 1):
            sum += ii
        print(sum)

printAmountOfNumbers(10)