# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-10-12

import random
import sys

#Question 9
#a)
rNum = random.randint(0,20)
#b)
rNum = random.randint(10,20)
#c)
rNum = random.randint(10,50)
#d)
rNum = random.randint(0,1)

#Question 10
firstNumber = random.randint(0,5)
secondNumber = random.randint(0,5)
sum = firstNumber + secondNumber
print("Question 1)", firstNumber, "+", secondNumber)
userInput = int(input("= "))
print(firstNumber, "+", secondNumber, "=", userInput, "is", str(userInput==sum) + ".")
print()

firstNumber = random.randint(0,5)
secondNumber = random.randint(0,5)
sum = firstNumber + secondNumber
print("Question 2)", firstNumber, "+", secondNumber)
userInput = int(input("= "))
print(firstNumber, "+", secondNumber, "=", userInput, "is", str(userInput==sum) + ".")
print()
