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
max = sys.maxsize
min = -sys.maxsize - 1
firstSum = random.randint(0, 5)
print(firstSum)
answerStr = input("Question 1) ")
firstAnswerStr, secondAnswerStr = answerStr.split("+")
firstNumber  = int(firstAnswerStr)
secondNumber = int(secondAnswerStr)
firstAnswer = firstNumber + secondNumber
print(firstAnswerStr, "+", secondAnswerStr, "=", firstSum, "is", str(firstSum==firstAnswer) + ".")
print()

secondSum = random.randint(0, 5)
print(secondSum)
answerStr = input("Question 1) ")
firstAnswerStr, secondAnswerStr = answerStr.split("+")
firstNumber  = int(firstAnswerStr)
secondNumber = int(secondAnswerStr)
firstAnswer = firstNumber + secondNumber
print(firstAnswerStr, "+", secondAnswerStr, "=", secondSum, "is", str(secondSum==firstAnswer) + ".")