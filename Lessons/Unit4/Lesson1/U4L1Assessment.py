# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-11-08

#2.
name = input("Give a name: ")
while not name.strip(" ").isalpha():
    name = input("Give a name: ")
    if name.strip(" ").isalpha():
        break
accumulator = ""

for i in range(len(name)):
    if name[i] == " ":
        accumulator += name[i+1]
    elif i == 0:
        accumulator += name[i]
for i in range(len(accumulator)):
    if i < len(accumulator) -1:
        print(accumulator[i] + ". ", end="")
    else:
        print(accumulator[i] + ".", end="")
print("\n")

#3.
number = input("Enter a number: ")
while not number.isnumeric():
    number = input("Enter a number: ")
    if number.isnumeric():
        break
counter = 0
for i in range(len(number)):
    counter += int(number[i])
print(counter, "\n")

#4.
mmddyyyy = input("Enter mm/dd/yyyy: ")
while not mmddyyyy.replace("/", "").isnumeric() or len(mmddyyyy) != 10 or int(mmddyyyy[0:2].strip("0")) > 12 or int(mmddyyyy[0:2].strip("0")) < 1:
    mmddyyyy = input("Enter mm/dd/yyyy: ")
    if mmddyyyy.replace("/", "").isnumeric() or len(mmddyyyy) == 10 or int(mmddyyyy[0:2].strip("0")) < 13 or int(mmddyyyy[0:2].strip("0")) > 0:
        break
month = mmddyyyy[0:2]
day = mmddyyyy[3:5]
year = mmddyyyy[6:]
month = month.strip("0")
day = day.strip("0")
month = int(month)
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(months[month-1], day + "," , year)
print()

#5.
morseCodeMapping = {
    " ": "/",
    ",": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "...",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": ".--.",
    "y": "-.-",
    "z": "--.."
}
phrase = input("Enter a sentence: ")
for i in range(len(phrase)):
    if i < len(phrase) - 1:
        print(morseCodeMapping[phrase[i].lower()] + " ", end="")
    else:
        print(morseCodeMapping[phrase[i].lower()], end="")