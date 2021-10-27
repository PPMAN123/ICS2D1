# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-10-27

#3.
patternVersion = input("What pattern would you want? ")
numOfLines = int(input("Enter the number of lines you want: "))
print()
if patternVersion in "abcABC":
    if patternVersion == "a" or patternVersion == "A":
        for i in range(1,numOfLines + 1):
            for j in range(i):
                print("*", end="")
            print()
    elif patternVersion == "b" or patternVersion == "B":
        for i in range(numOfLines + 1, 1, -1):
            for j in range(i, 1, -1):
                print("*", end="")
            print()
    elif patternVersion == "c" or patternVersion == "C":
        numPerLine = numOfLines + numOfLines - 1
        numOfSpaces = numPerLine//2
        numOfStars = 1
        for i in range(1, numOfLines + 1):
            printOut = ""
            for j in range(numOfSpaces):
                printOut += " "
            printOut += numOfStars * "*"
            numOfStars += 2
            numOfSpaces -= 1
            print(printOut)
print()

#4.
currentFloor = 1
while currentFloor >= 1 and currentFloor <= 10:
    print("You are on floor", currentFloor)
    nextFloor = int(input("What floor would you like to go to? "))
    if nextFloor < 1 or nextFloor > 10:
        print("There is no floor", nextFloor, "Please exit the elevator")
        break
    else:
        if nextFloor > currentFloor:
            print("You will be going up", nextFloor - currentFloor, "floors.")
        elif nextFloor < currentFloor:
            print("You will be going down", currentFloor - nextFloor, "floors.")
        else:
            print("You are already on Floor", currentFloor)
        currentFloor = nextFloor
print()

#5.
