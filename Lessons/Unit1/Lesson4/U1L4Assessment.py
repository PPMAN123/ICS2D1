# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-09-29

#5.
feet = float(input("Enter a value for feet: "))
print(feet, "feet is", feet*0.305, "meters")
print()

#6.
pounds = float(input("Input a value in pounds: "))
print(pounds, "pounds is", pounds*0.454, "kilograms")
print()

#7.
subtotal, gratituity = input("Enter a subtotal and a gratituity rate: ").split(",")
subtotal = float(subtotal)
gratituity = float(gratituity)
gratituityAmount = subtotal*(gratituity/100)
total = subtotal+gratituityAmount
print("The gratituity is", "%.2f" %gratituityAmount, "and the total is", "%.2f" %total)
print()

#8.
weight = float(input("Enter amount of water in kilograms: "))
initialTemperature = float(input("Enter the initial temperature: "))
finalTemperature = float(input("Enter the final temperature: "))
print("The energy needed is", weight*((finalTemperature-initialTemperature)*4184))