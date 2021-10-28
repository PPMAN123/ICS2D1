#Ethan Zhou
#ICS2O1
#Ms Wun
#2021-10-28

import random

#1.
currentNumber = 1
evenNumbers = 0
oddNumbers = 0
runAgain = 'Y'
while runAgain == 'Y' or runAgain == 'y':
    while currentNumber != 0:
        try:
            currentNumber = int(input("Enter a positive or negative integer. Type 0 to stop: "))
        except ValueError:
            print("ERROR: Enter an integer please")
        if currentNumber % 2 == 0:
            evenNumbers += currentNumber
        else:
            oddNumbers += currentNumber
    print("\nThe sum of all the even numbers is", evenNumbers, "and the sum of all the odd numbers is", str(oddNumbers) + ".\n")
    runAgain = input("Would you like to run the program again? (Y/N): ")
    if runAgain != 'Y' or runAgain != 'N' or runAgain != 'y' or runAgain != 'n':
        print("\nERROR: You must enter Y or N")
if runAgain in 'YN':
    print("Thank You! Goodbye!")
print()

#2.
currentRandom = ''
currentUserChoice = ''
computerWins = 0
computerLosses = 0
playAgain = 'Y'

print("Welcome to Rock, Paper, Scissors!\n\nINSTRUCTIONS: Enter R - Rock, P - Paper, S - Scissors\n\nReady? Go!\n\n")

while playAgain == 'Y' or playAgain == 'y':
    for i in range(3):
        print("Round", i+1)
        randomNumber = random.randint(1,3)
        if randomNumber == 1:
            currentRandom = 'R'
        elif randomNumber == 2:
            currentRandom = 'P'
        elif randomNumber == 3:
            currentRandom = 'S'
        currentUserChoice = input("User’s move (R/P/S): ")
        print("Computer's move:", currentRandom)
        if currentUserChoice == 'R' and currentRandom == 'S':
            computerLosses += 1
            print("User Wins!")
        elif currentUserChoice == 'P' and currentRandom == 'R':
            computerLosses += 1
            print("User Wins!")
        elif currentUserChoice == 'S' and currentRandom == 'P':
            computerLosses += 1
            print("User Wins!")
        elif currentRandom == 'R' and currentUserChoice == 'S':
            computerWins += 1
            print("Computer Wins!")
        elif currentRandom == 'P' and currentUserChoice == 'R':
            computerWins += 1
            print("Computer Wins!")
        elif currentRandom == 'S' and currentUserChoice == 'P':
            computerWins += 1
            print("Computer Wins!")
        elif currentRandom == currentUserChoice:
            print("It's a tie!")
        else:
            print("\nERROR: You must enter a valid value")
            break
    if computerWins > computerLosses:
        print("After 3 rounds, the ultimate winner is the Computer!")
    elif computerLosses > computerWins:
        print("After 3 rounds, the ultimate winner is the User!")
    elif computerLosses != 0 and computerWins != 0 and computerLosses == computerWins:
        print("After 3 rounds, the game is tied!")
    else:
        break
    print()
    playAgain = input("Would you like to play again? (Y/N): ")
    if playAgain not in 'yYnN' and len(playAgain) != 1:
        print("\nYou must enter Y or N")
if playAgain == 'N' or playAgain == 'n':
    print("Thank You for playing!")
print()

#3.
toContinue = 'y'
while toContinue == 'y' or toContinue == 'Y':
    print("Simulations:")
    averageHolder = 0.0
    for i in range(10):
        match = False
        flips = []
        while match == False:
            currentFlip = ''
            currentSim = random.randint(1,2)
            if currentSim == 1:
                currentFlip = 'H'
            elif currentSim == 2:
                currentFlip = 'T'
            flips.append(currentFlip)
            if len(flips) >= 3:
                for j in range(2,len(flips)):
                    if flips[j] == flips[j-1] and flips[j-1] == flips[j-2] and flips[j] == flips[j-2]:
                        match = True
        for j in range(len(flips)):
            print(flips[j], '', end='')
        print("(" + str(len(flips)) + " flips)")
        print()
        averageHolder += float(len(flips))
    print("After 10 simulations, on average,", averageHolder/10, "flips were needed.")
    toContinue = input("Would you like to run the simulations again? (Y/N): ")
    if toContinue not in 'yYnN' and len(toContinue) != 1:
        print("ERROR: You must enter Y or N")
        break