# Ethan Zhou
# ICS2D1
# Mrs Cruceanu
# Sept 17 2021

import math

#Minds On
miles = 100
kilometers = miles*1.61
print(kilometers)
print()

#Action
#1.
print("What is your name?")
name = input()
print("Hello", name)
print()

#2.
radius = input("The radius of the circle is: ")
radius = float(radius)
pi = 3.1415926
print("The area of the circle is:", pi*radius*radius)
print()

#Assessment
#1.
firstNumber = float(input("The first number is:"))
secondNumber = float(input("The second number is:"))
thirdNumber = float(input("The third number is:"))
print("The average of the numbers is:",(firstNumber+secondNumber+thirdNumber)/3)
print()

#2.
celsius = float(input("Enter temperature in Celsius scale:"))
farenheit = ((celsius/5)*9)+32
print(celsius, "degrees Celsius =", farenheit, "degrees farenheit")
print()

#3.
length = float(input("Length:"))
width = float(input("Width:"))
print(length*width)
print((2*width)+(2*length))
print()

#4.
print("a b a**b")
for i in range(1,6):
  b = i+1
  print(i, b, i**b)
print()

#5.
s = float(input("Enter the side:"))
area = ((s**2)/2)*(3*math.sqrt(3))
print(area)
print()

#6.
investmentAmount = float(input("Enter investment amount: "))
interestRate = float(input("Enter annual interest rate: "))/100
numOfYears = float(input("Enter number of years: "))
print(investmentAmount*(1+interestRate)**(numOfYears))