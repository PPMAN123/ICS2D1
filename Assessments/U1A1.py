#Ethan Zhou
#ICS2O1
#Mrs Wun
#2021-09-30

#1.
#getting inputs
price = float(input("Enter price of item from 25 cents to a dollar, in 5-cent increments): "))
reverse = 100-price
#quarter counter
i = 0
#dime counter
j = 0
#nickel counter
k = 0
#quarter check
while reverse >= 25:
    reverse -= 25
    i += 1
#dime check
while reverse >= 10:
    reverse -= 10
    j += 1
#nickel check
while reverse >= 5:
    reverse -= 5
    k += 1
#outputs
print("You bought an item for", price, "cents and gave me a dollar, so your change is: \n")
print(i, "quarters")
print(j, "dimes")
print(k, "nickels")

#2.
#getting inputs
print("----------------------------------")
itemOne = input("Input name of item 1: ")
quantityOne = int(input("Input quantity of item 1: "))
priceOne = float(input("Input price of item 1: "))
print("----------------------------------")
itemTwo = input("Input name of item 2: ")
quantityTwo = int(input("Input quantity of item 2: "))
priceTwo = float(input("Input price of item 2: "))
print("----------------------------------")
itemThree = input("Input name of item 3: ")
quantityThree = int(input("Input quantity of item 3: "))
priceThree = float(input("Input price of item 3: "))
print()

#style prices and managing variables
tempOne = priceOne*quantityOne
totalOne = "%.2f" %tempOne
tempTwo = priceTwo*quantityTwo
totalTwo = "%.2f" %tempTwo
tempThree = priceThree*quantityThree
totalThree = "%.2f" %tempThree
tempSubtotal = tempOne + tempTwo + tempThree
subtotal = "%.2f" %tempSubtotal
tempTax = tempSubtotal * 0.0625
tax = "%.2f" %tempTax
tempTotal = tempSubtotal + tempTax
total = "%.2f" %tempTotal

priceOne = "%.2f" %priceOne
priceTwo = "%.2f" %priceTwo
priceThree = "%.2f" %priceThree

#Output
print("Your Bill:")
print("------------------------------------------------------------")
print(f"{'Item' :<20} {'Quantity' :<20} {'Price' :<10} {'Total' :<10} ")
print(f"{itemOne :<20} {quantityOne :<20} {priceOne :<10} {totalOne :<10} ")
print(f"{itemTwo :<20} {quantityTwo :<20} {priceTwo :<10} {totalTwo :<10} ")
print(f"{itemThree :<20} {quantityThree :<20} {priceThree :<10} {totalThree :<10} ")
print("------------------------------------------------------------")
print(f"{'Subtotal' :<50} {subtotal :>8}")
print(f"{'6.25% sales tax' :<50} {tax :>8}")
print(f"{'Total' :<50} {total :>8}")
print()

#3.
nameOne = input("Name of exercise 1: ")
scoreOne = int(input("Score received for exercise 1: "))
pointsOne = int(input("Total points possible for exercise 1: "))
print()
nameTwo = input("Name of exercise 2: ")
scoreTwo = int(input("Score received for exercise 2: "))
pointsTwo = int(input("Total points possible for exercise 2: "))
print()
nameThree = input("Name of exercise 3: ")
scoreThree = int(input("Score received for exercise 3: "))
pointsThree = int(input("Total points possible for exercise 3: "))
print()

#managing some variables
total = scoreOne + scoreTwo + scoreThree
totalPossible = pointsOne + pointsTwo + pointsThree

#outputting
print(f"{'Exercise' :<20} {'Score' :<20} {'Total Possible' :<20} ")
print(f"{nameOne :<20} {scoreOne :<20} {pointsOne :<20} ")
print(f"{nameTwo :<20} {scoreTwo :<20} {pointsTwo :<20} ")
print(f"{nameThree :<20} {scoreThree :<20} {pointsThree :<20} ")
print()
print("Your total is", total, "out of", totalPossible, "or", str(round((total/totalPossible)*100, 2)) + "%")
print()

#4.
#getting inputs
print("Please enter your test grades.")
print()
testOne = float(input("Test 1: "))
testTwo = float(input("Test 2: "))
print()
print("Please enter you quiz grades.")
quizOne = float(input("Quiz 1: "))
quizTwo = float(input("Quiz 2: "))
quizThree = float(input("Quiz 3: "))
print()
print("Please enter your homework grades.")

#calculations
homework = float(input("Homework: "))
print()
testAverage = (testOne+testTwo)/2
quizAverage = (quizOne+quizTwo+quizThree)/3
finalGrade = ((testAverage*50)+(quizAverage*30)+(homework*20))/100
print("Test average:", round(testAverage,2))
print("Quiz Average:", round(quizAverage,2))
print("Final Grade:", round(finalGrade,2))