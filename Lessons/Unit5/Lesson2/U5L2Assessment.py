# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-11-23

#2.
file = open("./rhyming.txt", "a")

file.write("\n5 6 pick up sticks\n7 8 programming’s great!")

file.close()

#3.
file = open("./numbers.txt", "r")
firstNum = float(file.readline())
secondNum = float(file.readline())
thirdNum = float(file.readline())
sum = open("./sum.txt", "w")
data = firstNum + secondNum + thirdNum
sum.write(str(data))
file.close()
sum.close()

#4.
sum = open("./sum.txt", "w")
sum.write("Haha! You’ve been overwritten!")
sum.close()

#5.
lyrics = open("./lyrics.txt")
searchFor = input("Enter a word or phrase you would like to search for: ")
searchFor = searchFor.lower()
counter = 0

for line in lyrics:
    line = line.lower()
    counter += line.count(searchFor)

print("The phrase: \"" + str(searchFor) + "\" appears", counter, "times")

#6.
def rewriteLyrics():
    """
    Function that rewrites lyrics.txt in the number of lines the user inputs.

    Parameters
    >none

    Returns
    >null
    """
    lyrics = open("./lyrics.txt", "w")
    lines = int(input("Enter how many lines the lyrics have: "))
    accumulator = ""
    for i in range(lines):
        inputAsk = "Enter the lyrics of line " + str(i+1) + ": "
        newLine = input(inputAsk)
        accumulator += newLine + "\n"
    lyrics.write(accumulator)
    lyrics.close

def replaceLyrics():
    toReplace = input("Enter what you want to replace: ")
    replaceTo = input("Enter what you want to replace to: ")
    toReplace = toReplace.lower()
    replaceTo = replaceTo.lower()
    lyrics = open("./lyrics.txt")
    accumulator = ""
    for line in lyrics:
        accumulator += line.replace(toReplace, replaceTo)
    lyrics.close()

    lyrics = open("./lyrics.txt", "w")
    lyrics.write(accumulator)
    lyrics.close()

print("Choose what you would like to do with the lyrics: \n1. Rewrite lyrics\n2.Replace lyrics")
choice = input("Type 1 or 2")
if choice == "1":
    rewriteLyrics()
elif choice == "2":
    replaceLyrics()