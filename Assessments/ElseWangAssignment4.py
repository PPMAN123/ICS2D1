"""
programmed by: elsa
programmed on:nov, 12,2021
programmed for: ICS201-2A (Assignment 4)

"""


print("")
print("Question 3:")



ask = "y"
while ask == "y" or ask == "Y":
  try:
    number = ""
    word = input("Input a telephone number expressed in letters: ")
    word = word.replace(" ","")

    if len(word)==7:
      for char in word:
        if char in "ABCabc":
          number+= "2"
        elif char in "DEFdef":
          number+= "3"
        elif char in "GHIghi":
          number+= "4"
        elif char in "JKLjkl":
          number+= "5"
        elif char in "MNOmno":
          number+= "6"
        elif char in "PQRSpqrs":
          number+= "7"
        elif char in "TUVtuv":
          number+= "8"
        elif char in "WYXZwyxz":
          number+= "9"
        else:
          print("ERROR: Not the right input")
          break
    else:
      print("ERROR: Not the right input")
    if len(number) != 0:
      print("The phone number is", number[0:3]+"-"+number[3:])
  except ValueError:
    print("ERROR: That is an invalid number.")
  ask = input("Would you like to play again? (Y/N):")
  if ask == "N" or ask == "n":
    print("Thanks for playing!")
    break