#Ethan Zhou
#ICS2O1
#Ms Wun
#2021-10-28
#i tried harder to error trap this time, it is supposed to ask again if you enter something wrong, except when you enter nothing at all and just press enter, which just skips everything i don't know why

import random

#1.
#making sure i loop the program if the user writes 'y'
runAgain = 'Y'
while runAgain == 'Y' or runAgain == 'y':
    currentNumber = 1
    evenNumbers = 0
    oddNumbers = 0
    while currentNumber != 0:
        #error catching so user can't spam
        try:
            currentNumber = int(input("Enter a positive or negative integer. Type 0 to stop: "))
        except ValueError:
            pass
        if currentNumber % 2 == 0:
            evenNumbers += currentNumber
        else:
            oddNumbers += currentNumber
    print("\nThe sum of all the even numbers is", evenNumbers, "and the sum of all the odd numbers is", str(oddNumbers) + ".\n")
    runAgain = input("Would you like to run the program again? (Y/N): ")
    while runAgain not in 'yYnN' and len(runAgain) != 1:
        runAgain = input("Would you like to run the program again? (Y/N): ")

#2.

playAgain = 'Y'

print("Welcome to Rock, Paper, Scissors!\n\nINSTRUCTIONS: Enter R - Rock, P - Paper, S - Scissors\n\nReady? Go!\n\n")
#making sure I loop the program if the user writes 'y'
while playAgain == 'Y' or playAgain == 'y':
    #initializing and resetting variables in beginning of loop
    currentRandom = ''
    currentUserChoice = ''
    computerWins = 0
    computerLosses = 0
    for i in range(3):
        print("Round", i+1)
        #random number for assigning rock paper scissors
        randomNumber = random.randint(1,3)
        if randomNumber == 1:
            currentRandom = 'R'
        elif randomNumber == 2:
            currentRandom = 'P'
        elif randomNumber == 3:
            currentRandom = 'S'
        
        currentUserChoice = input("User’s move (R/P/S): ")

        while currentUserChoice not in 'RPS':
            currentUserChoice = input("User’s move (R/P/S): ")
        
        print("Computer's move:", currentRandom)

        #hardcoding the rock paper scissors game
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
    #win conditions
    if computerWins > computerLosses:
        print("After 3 rounds, the ultimate winner is the Computer!")
    elif computerLosses > computerWins:
        print("After 3 rounds, the ultimate winner is the User!")
    elif computerLosses != 0 and computerWins != 0 and computerLosses == computerWins:
        print("After 3 rounds, the game is tied!")
    else:
        break
    print()
    #repeating y or n algorithm i will not comment the other programs with this cuz it's basically the same algorithm control c + v
    playAgain = input("Would you like to play again? (Y/N): ")
    while playAgain not in 'yYnN' and len(playAgain) != 1:
        playAgain = input("Would you like to play again? (Y/N): ")
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
        #match is true when 3 T's or H's happen
        flips = []
        #list of all the flip results (could've used a string because python strings work as lists)
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
                    #goes through the list to see if i get 3 consecutive T's or H's
                    if flips[j] == flips[j-1] and flips[j-1] == flips[j-2] and flips[j] == flips[j-2]:
                        match = True
        #iterating through the array to print out the values
        for j in range(len(flips)):
            print(flips[j], '', end='')
        print("(" + str(len(flips)) + " flips)")
        print()
        averageHolder += float(len(flips))

    print("After 10 simulations, on average,", averageHolder/10, "flips were needed.")

    toContinue = input("Would you like to run the simulations again? (Y/N): ")
    while toContinue not in 'yYnN' and len(toContinue) != 1:
        toContinue = input("Would you like to run the simulations again? (Y/N): ")
print("Thank you! Good Bye!\n")

#4.
playAgain = 'y'
#i found a better way to check for a character input using len()
while playAgain in 'yY' and len(playAgain) == 1:
    playerGuess = 0
    #error trapping to avoid spam
    while playerGuess > 1000 or playerGuess < 100:
        try:
            playerGuess = int(input("Guess a 3-digit number: "))
        except ValueError:
            pass
    lotteryNumber = str(random.randint(100,999))
    print("Lottery number:", lotteryNumber)
    playerGuess = str(playerGuess)
    if playerGuess == lotteryNumber:
        print("You guess all three digits correctly in the correct order.")
        print("You won: $1000000")
    else:
        digitsCorrect = 0
        #a counter for how many digits i guessed right
        for i in range(3):
            #the moment when i figured out you can iterate through a string
            if playerGuess[i] in lotteryNumber:
                digitsCorrect += 1
        #hard coding the results
        if digitsCorrect == 0:
            print("No matches.")
            print("You won: $0\n")
        elif digitsCorrect == 1:
            print("You guessed one digit correctly.")
            print("You won: $10\n")
        elif digitsCorrect == 2:
            print("You guessed two digits correctly.")
            print("You won: $100\n")
        elif digitsCorrect == 3:
            print("You guessed all three digits correctly but not in the correct order.")
            print("You won: $1000\n")
    
    playAgain = input("Would you like to play again(y/n)?: ")
    while playAgain not in 'yYnN' and len(playAgain) != 1:
        playAgain = input("Would you like to play again(y/n)?: ")
    if playAgain in 'yY':
        print("\n***\n")
print("Thank you for playing!")