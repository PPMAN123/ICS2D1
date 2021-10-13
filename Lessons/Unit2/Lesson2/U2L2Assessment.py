# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-10-13

#3.
rangeInt = int(input("How many scores do you have? "))
testScores = []
for i in range(rangeInt):
    message = "Enter your score for Test " + str(i+1) + ": "
    testScores.append(float(input(message)))
average = 0
for i in range(len(testScores)):
    average += testScores[i]
average /= len(testScores)
print()
print("Your average score is", str(round(average,1)) + "%")
if average > 80:
    print("Well done! Keep it up!")
elif average > 50:
    print("Good efforts!")
elif average < 50:
    print("Keep working at it!")

#4.
integer = int(input("Enter an integer: "))
if integer % 5 == 0:
    print("This number is divisible by 5")
else:
    print("This number is not divisible by 5")
print()

#5.
vowels = ["a", "e", "i", "o", "u"]
letter = input("Enter a letter: ")
if letter in vowels:
    print(letter, "is a vowel")
else:
    print(letter, "is a consonant")
print()

#6.
sides = int(input("Enter the number of sides in the shape: "))
if sides <= 2:
    print("No closed shape can be created with that number of sides.")
if sides == 3:
    print("That is a triangle")
if sides == 4:
    print("That is a quadrilateral")
if sides == 5:
    print("That is a pentagon")
if sides == 6:
    print("That is a hexagon")
if sides == 7:
    print("That is a heptagon")
if sides == 8:
    print("That is an octagon")
if sides == 9:
    print("That is a nonagon")
if sides == 10:
    print("That is a decagon")
if sides > 10:
    print("That is a " + str(sides) + "-gon")
print()

#7.
a,b,c = input("Enter the 3 side lengths: ").split(",")
a = int(a)
b = int(b)
c = int(c)
if a + b > c or a + c > b or b + c > a:
    if a == b == c:
        print("That is an equilateral triangle")
    elif a == b:
        print("That is an isosceles")
    else: 
        print("That is a scalene triangle")
else:
    print("No triangle can be created")