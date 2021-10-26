# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-10-25

#2.
i = 0
sum = 0
while i < 1001:
    sum += i
    i+=1
print(sum)
print()

#3.
sum = 0
for i in range(1,10000):
    sum += i
print(sum)
print()

#5.
testPasses = 0
for i in range(100,1001):
    if i % 5 == 0 and i % 6 == 0:
        print(i, '', end = '')
        testPasses += 1
        if testPasses % 10 == 0:
            print()
print()

#6.
try:
    scores = []
    rangeNum = 1
    while rangeNum <= 2:
        rangeNum = int(input("Enter the number of students in the class: "))
    print()
    for i in range(rangeNum):
        inputMessage = "Student " + str(i+1) + "'s score: "
        newScore = int(input(inputMessage))
        if newScore > 100 or newScore <= 0:
            print("ERROR: You need to enter a percentage under 100")
            break
        scores.append(newScore)
    scores.sort()
    if newScore <= 100 or newScore >= 0:
        print("\nThe highest mark in the class is", str(scores[len(scores)-1]) + "% and the second highest score in the class is", str(scores[len(scores)-2]) + "%.")
        print()
except ValueError:
    print("ERROR: You need to type in integers")
print()

#7.
print("  x  |  y  ")
print("-----------")
for x in range(-15,40,3):
    y = (-1*(x**2)) + (3*x) - 2
    print(f"{x :< 5}" + "|" + f"{y :< 5}")