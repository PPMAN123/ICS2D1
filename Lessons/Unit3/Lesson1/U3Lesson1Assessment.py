# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-10-25

#4.
x = -10
print("  x  |  y  ")
print("-----------")
while x <= 12:
    y = (2*(x**3)) - (11*(x**2)) + 3
    print(f"{x :< 5}" + "|" + f"{y :< 5}")
    x += 2
print()

#5.
try:
    toContinue = "y"
    while toContinue == "y" or toContinue == "Y":
        dependents = float(input("Enter number of dependents: "))
        income = float(input("Enter annual income ($): "))
        print()
        if dependents > 0:
            if dependents == 0:
                print("Your tax rate is 30%." , "Your tax bill is $%.2f" %(income*0.3))
            elif dependents == 1:
                print("Your tax rate is 25%." , "Your tax bill is $%.2f" %(income*0.25))
            elif dependents == 2:
                print("Your tax rate is 18%." ,  "Your tax bill is $%.2f" %(income*0.18))
            elif dependents >= 3:
                print("Your tax rate is 10%." , "Your tax bill is $%.2f" %(income*0.1))
        else:
            print("ERROR: That is an invalid number of dependents. Please try again.")
        print()
        toContinue = input("Would you like to quit the program? (y/n): ")
        if toContinue not in 'yYnN':
            print("ERROR: You must enter y or n")
            break
        print()
except ValueError:
    print("\nERROR: Please check your values")
print()

#6.
correctPassword = "earlhaig"
userInput = ""
guessesLeft = 5
while userInput != correctPassword or guessesLeft > 0:
    userInput = input("Enter your password: ")
    guessesLeft -= 1
    if userInput == correctPassword:
        print("Access granted")
        break
    if guessesLeft == 0:
        print("You are locked out. Please try again in 24 hours.")
        break
    print("Invalid password. You have", guessesLeft, "more attempts")