#Ethan Zhou
#ICS2O1
#Ms Wun
#2021-11-12

#Question 3
runAgain = "Y"
#a dictionary (js object) to map out all the corresponding numbers
phoneNumberMapping = {
    "_": '1',
    ".": "1",
    "@": "1",
    "a": '2',
    "b": "2",
    "c": "2",
    "d": "3",
    "e": "3",
    "f": "3",
    "g": "4",
    "h": "4",
    "i": "4",
    "j": "5",
    "k": "5",
    "l": "5",
    "m": "6",
    "n": "6",
    "o": "6",
    "p": "7",
    "q": "7",
    "r": "7",
    "s": "7",
    "t": "8",
    "u": "8",
    "v": "8",
    "w": "9",
    "x": "9",
    "y": "9",
    "z": "9"
}
#array of valid chars
validChars = ["_", ".", "@", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
while runAgain in ["Y", "y"]:
    #variable to check if input letters are all valid
    valid = True
    #getting input
    phoneLetters = input("Input a telephone number expressed in letters: ").lower().replace(" ", "")
    #checking if characters in input are all valid
    for char in phoneLetters:
        if char not in validChars:
            valid = False
    #getting the output phone number
    if valid and len(phoneLetters) == 7:
        phoneNumber = ""
        for char in phoneLetters:
            phoneNumber += phoneNumberMapping[char]
        printOut = phoneNumber[0:3] + "-" + phoneNumber[3:]
        print("The phone number is", printOut)
    else:
        print("That is an invalid phone number.")
    print()
    #algorithm to ask user if they want to use the program again
    runAgain = input("Would you like to input another telephone number? (Y/N): ")
    while runAgain not in ["Y", "y", "N", "n"]:
        runAgain = input("Would you like to input another telephone number? (Y/N): ")
    print()
print("Thank you! Goodbye!")