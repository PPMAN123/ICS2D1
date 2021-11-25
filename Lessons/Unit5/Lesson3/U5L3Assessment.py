# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-11-23

#1.
from typing import Counter


width = int(input("Enter the width of the diamond: "))
symbol = input("Enter the symbol you want the diamond to be made out of: ")

if width % 2 == 0:
    for i in range(0, width*2, 2):
        if i <= width:
            numSpaces = (width - i)//2
            numSymbols = i
            print(" "*numSpaces + symbol*numSymbols)
        else:
            numSpaces = (i - width)//2
            numSymbols = 2*width - i
            print(" "*numSpaces + symbol*numSymbols)
else:
    for i in range(1, 2*width+1, 2):
        if i <= width:
            numSpaces = (width - i)//2
            numSymbols = i
            print(" "*numSpaces + symbol*numSymbols)
        else:
            numSpaces = (i - width)//2
            numSymbols = 2*width - i
            print(" "*numSpaces + symbol*numSymbols)
print()

#2.
def addDigit(number: int):
    """
    Function that adds the last digit of the sum of the number to the last digit of the number

    Parameters
    >number: int

    Returns
    >int
        number with an extra digit added to it through calculations
    """
    counter = 0
    for char in number:
        counter += int(char)
    number += str(counter)[-1]
    return int(number)
number = input("Enter a number to process: ")
print(addDigit(number))
print()


#3.
number = input("Enter a number to convert to binary: ")
numbers = []
extraCounter = 0
sum = 0
for i in range(len(number)-1, -1,-1):
    appending = int(number[i])
    numbers.append(appending*(2**extraCounter))
    extraCounter += 1
for number in numbers:
    sum += number
print(sum, "base 10")
print()

#4.
number = input("Enter a number to convert: ")
temp = number.split(" ")
number = temp[0]
base = temp[2]
numbers = []
extraCounter = 0
sum = 0
for i in range(len(number)-1, -1,-1):
    appending = int(number[i])
    numbers.append(appending*(int(base)**extraCounter))
    extraCounter += 1
for number in numbers:
    sum += number
print(sum, "base 10")
print()

#5.
poem = open("./poem.txt")
acc = ""
for line in poem:
    acc += line.upper()
poem.close()

poem = open("./poem.txt", "w")
poem.write(acc)
poem.close()

#6.
hours = open("./hours.txt")
for employee in hours:
    stats = employee.split(" ")
    name = stats[0]
    hoursWorked = stats[1:]
    hourCounter = 0
    for num in hoursWorked:
        hourCounter += float(num)
    print(name, hourCounter)
hours.close()
print()

#7.
names = open("./names.txt")
counter = 0
for name in names:
    counter += 1
print(counter)
print()
names.close()

#8.
numbers = open("./numbers.txt")
counter = 0
sumCounter = 0
for number in numbers:
    counter += 1
    sumCounter += float(number)
print(sumCounter/counter)
print()

#9.
employeeHours = open("./hours.txt", "a")
keepGoing = "y"
while keepGoing == "y":
    employeeWorkHours = ""
    employeeWithHours = ""
    name = input("Enter the employee name")
    hours = ""
    while hours != "x":
        hours = input("How many hours did this person work for (press x to stop entering work hours): ")
        if hours == "x":
            break
        else:
            employeeWorkHours += hours + " "
    employeeWithHours = "\n" + name + " " + employeeWorkHours
    employeeHours.write(employeeWithHours)
    keepGoing = input("Do you wish to keep going? (y/n)")
print("Thank you!\n")