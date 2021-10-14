# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-10-14

#Minds On.
userInput = input("username or password: ")
correctName = "mswun"
correctEmail = "mswun@gmail.com"
password = input("password: ")
correctPassword = "abc"
print()

if (userInput == correctName or userInput == correctEmail) and password == correctPassword:
    print("Accessing")
else:
    print("Error")
print()

#Action:
try:
    number = int(input("Enter an integer pls"))
    print(number+1)
except ValueError:
    print("Enter an integer pls")
print()