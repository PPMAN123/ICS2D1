# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-10-14

import random

#1.
try:
    firstInteger = int(input("Enter an integer: "))
    secondInteger = int(input("Enter a second integer: "))
    if firstInteger > secondInteger:
        print("Larger")
    if firstInteger < secondInteger:
        print("Smaller")
    if firstInteger == secondInteger:
        print("Equals")
except ValueError:
    print("Enter a valid integer pls")
print()

#2.
try:
    messageLength = int(input("How many words are in your message? "))
    price = 0.0
    if messageLength < 0:
        print("Message Length has to be positive")
    else:
        if messageLength <= 10:
            print("$1.35")
        else:
            price += 1.35
            messageLength -= 10
            price += messageLength * 0.09
            print("$" + "%.2f" %price)
except ValueError:
    print("Enter a valid integer pls")
print()

#3.
try:
    number = int(input("Enter an integer pls: "))
    if number <= 0:
        print("Negative")
    elif number <= 10:
        print("1")
    elif number <= 20:
        print("2")
    elif number <= 30:
        print("3")
    elif number <= 40:
        print("4")
    elif number <= 50:
        print("5")
    elif number <= 60:
        print("6")
    elif number <= 70:
        print("7")
    elif number <= 80:
        print("8")
    elif number <= 90:
        print("9")
    elif number <= 100:
        print("10")
    else:
        print("Too big!")
except ValueError:
    print("Enter a valid integer pls")
print()

#4.
try:
    check = float(input("Enter the payment: "))
    tip = check*.15
    if check < 1.00:
        print("Error: check must be over $1.00")
    else:
        print("$" + "%.2f" %tip)
except ValueError:
    print("Enter a valid float pls")
print()

#5.
try:
    cost = float(input("Enter your meal price: "))
    if cost < 0:
        print("cost has to be positive")
    else:
        if cost < 4:
            print("$" + "%.2f" %cost)
        else:
            cost *= 1.07
            print("$" + "%.2f" %cost)
except ValueError:
    print("Enter a valid cost pls")
print()

#6.
try:
    weight = int(input("Enter the weight of your package (kg): "))
    length, width, height = input("Enter the dimensions of your package (cm) (l,w,h): ").split(",")
    length = int(length)
    width = int(width)
    height = int(height)
    volume = length*height*width
    if weight < 27:
        if volume < 100000:
            print("your package is ok")
        else:
            print("Too Large")
    else:
        print("Too heavy")
except ValueError:
    print("Check your values")
print()

#7.
try:
    guess = int(input("Enter a number between 1 and 20: "))
    if guess < 1 or guess > 20:
        print("Error: That is not a valid number.")
    else:
        compNumber = random.randint(1,20)
        if guess == compNumber:
            print("You won!")
        else:
            print("Better luck next time!")
except ValueError:
    print("Enter a valid integer pls")
print("***")