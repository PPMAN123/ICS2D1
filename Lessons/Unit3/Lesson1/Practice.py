# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-10-25

#Minds On
try:
    numCopies = int(input("Enter the number of copies: "))

    if 0 <= numCopies <= 90:
        print("Price per copy: $0.30")
        print("The total price will be $%.2f" %(numCopies*0.30 ))
    elif 100 <= numCopies <= 499:
        print("Price per copy: $0.28")
        print("The total price will be $%.2f" %(numCopies*0.28 ))
    elif 500 <= numCopies <= 749:
        print("Price per copy: $0.27")
        print("The total price will be $%.2f" %(numCopies*0.27 ))
    elif 700 <= numCopies <= 1000:
        print("Price per copy: $0.26")
        print("The total price will be $%.2f" %(numCopies*0.26) )
    elif numCopies > 1000:
        print("Price per copy: $0.25")
        print("The total price will be $%.2f" %(numCopies*0.25) )
    else:
        print("ERROR: You need to input a valid value.")
except ValueError:
    print("ERROR: You need to input an integer.")
print()

#example 1
try:
    condition = "y"
    while condition == 'y' or condition == 'Y':
        condition = input("Do you wish to continue? (y/n): ")
    if condition != 'y' and condition != 'n' and condition != 'Y' and condition != 'N':
        print("ERROR: Please enter y or n")
    if condition == 'n' or condition == 'N':
        print("Goodbye")
except ValueError:
    print("ERROR: Please enter a valid letter")
print()

#example 2
counter = 1
while counter <= 10:
    print("Programming is fun")
    counter += 1
print()

#example 3
counter = 0
while counter <= 20:
    print(counter)
    counter += 2
print()

#example 4
counter = 0
total = 0
while counter <= 100:
    total += counter
    counter += 3
print(total)
print()

#example 5
try:
    number = 1
    acc = 0
    while number > 0:
        number = int(input("Enter a positive integer: "))
        if number > 0:
            acc += number
        if number < 0:
            print(acc)
            break
except ValueError:
    print("ERROR: Enter a valid integer")
print()