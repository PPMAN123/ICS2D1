# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-11-22

#Example 1
def fancyMessage():
  print("///************\\\\\\")
  print("|||Hello World!|||")
  print("\\\\\\************///")

fancyMessage()
print()

#Example 2 and 3
def fancyCustomMessage(message: str, symbol: str):
  print("///", end="")
  print(symbol*len(message), end="")
  print("\\\\\\")

  print("|||", end="")
  print(message, end="")
  print("|||")

  print("\\\\\\", end="")
  print(symbol*len(message), end="")
  print("///")

message = input("Enter a message to make it fancy: ")
symbol = input("Enter a symbol to fill in the space: ")
while len(symbol) != 1:
  symbol = input("Enter a symbol to fill in the space: ")
  if len(symbol) == 1:
    break
fancyCustomMessage(message, symbol)
print()

#Example 3
def numVowels(word: str):
  counter = 0
  for char in word:
    if char in "aeiouAEIOU":
      counter += 1
  return counter

word = input("Input a word: ")
if numVowels(word) % 2 == 0:
  print("Your word has an even number of vowels")
else:
  print("Your word has an odd number of vowels")
print()

#Example 4
import math
def areaOfCircle(radius: float):
  """
  Function to find area of circle

  Parameters
  >radius: float

  Returns
  >float
    pi*r^2
  """
  return math.pi*(radius**2)

def areaOfRectange(base: float, height: float):
  """
  Function to find area of a rectangle

  Parameters
  >base: float
  >height: float

  Returns
  >float
    base*height
  """

  return base*height

def areaOfTriangle(base: float, height: float):
  """
  Function to find the area of a triangle

  Parameters
  >base: float
  >height: float

  Returns
  >float
    base/2 * height
  
  """

  return (base/2)*height

quit = False

while quit == False:
  print("1. Area of a circle")
  print("2. Area of a rectangle")
  print("3. Area of a triangle")
  print("4. Quit the program")
  userChoice = input("Enter a choice: ")
  while len(userChoice) != 1 and not userChoice.isnumeric():
    userChoice = input("Enter a choice: ")
    if len(userChoice) == 1 and userChoice.isnumeric():
      break
  if userChoice == "1":
    radius = input("Enter a radius: ")
    while not radius.isnumeric():
      radius = input("Enter a radius: ")
      if radius.isnumeric():
        break
    print("The area of the circle is", areaOfCircle(float(radius)))
  elif userChoice == "2":
    base = input("Enter the base: ")
    height = input("Enter the height: ")
    while not base.isnumeric():
      base = input("Enter the base: ")
      if base.isnumeric():
        break
    while not height.isnumeric():
      height = input("Enter the height: ")
      if height.isnumeric():
        break
    print("The area of the rectangle is", areaOfRectange(float(base),float(height)))
  elif userChoice == "3":
    base = input("Enter the base: ")
    height = input("Enter the height: ")
    while not base.isnumeric():
      base = input("Enter the base: ")
      if base.isnumeric():
        break
    while not height.isnumeric():
      height = input("Enter the height: ")
      if height.isnumeric():
        break
    print("The area of the trianlge is", areaOfTriangle(float(base),float(height)))
  elif userChoice == "4":
    quit = True
