#Ethan Zhou
#ICS2O1
#Ms Wun
#2021-11-25

#1.
def getPentagonalNumber(n: int):
    """
    Function that returns a pentagonal number according to n

    Parameters
    >n: int

    Returns
    >int
        pentagonal number
    """

    return (n*((3*n)-1))/2

for i in range(1, 51):
    print(int(getPentagonalNumber(i)), "", end="")
    if i % 10 == 0:
        print()
print()

#2.
def nthChar(fileName: str, n : int):
    """
    File that returns the nth character on the first line of a text file

    Parameters
    >fileName: str
    >n: int

    Returns
    >none
    """

    file = open(fileName)
    for line in file:
        if len(line) > n:
            print(line[n-1])
        else:
            print("The line is not long enough")
    file.close()

fileName = input("Enter the file name: ")
n = int(input("Which letter do you want to print out: "))

nthChar(fileName, n)
print()

#3.
def questionThree():
    """
    Function that has the entire algorithm of question #3
    -Andrew Yao reminded me to put the question into a function

    Parameters
    >none

    Returns
    >none
    """
    marks = open("studentMarks.txt")
    replacement = ""
    for mark in marks:
        student = mark.split(" ")
        grades = []
        for individualMark in student:
            if individualMark.strip("\n").isnumeric():
                grades.append(int(individualMark))
        grades.sort()
        counter = 0
        for i in range(2, len(grades)):
            counter += grades[i]
        replacement += mark.strip("\n") + " Top6Avg: " + str(round(counter/6, 1)) + "\n"
    marks.close()

    marks = open("studentMarks.txt", "w")
    marks.write(replacement)
    marks.close()

questionThree()