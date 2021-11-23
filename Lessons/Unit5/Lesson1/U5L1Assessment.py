# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-11-22

#4.
def whatToWear(temperature: float):
  """
  Function to find out what to wear according to the temperature

  Parameters
  >temperature: float

  Returns
  >none
  """

  if temperature <= 50.0:
    print("Wear a jacket")
  elif temperature < 70:
    print("Wear a sweater")
  elif temperature >= 70:
    print("Wear a t-shirt")

temperature = input("Enter the temperature in fahrenheit: ")
while not temperature.isnumeric() or not temperature.isdecimal():
  temperature = input("Enter the temperature in fahrenheit: ")
  if temperature.isnumeric() or temperature.isdecimal():
    break
whatToWear(float(temperature))
print()

#5.
def greetings(word: str, n: int):
  """
  Function to print a word by a number of times

  Parameters
  >word: str
  >n: int

  Returns
  >none
  """
  print(word*n)

word = input("Enter a word: ")
n = input("Enter how many times you want to print that word: ")
while not n.isnumeric() or not n.isdecimal():
  n = input("Enter how many times you want to print that word: ")
  if n.isnumeric() or n.isdecimal():
    break
greetings(word,int(n))
print()

#6.

def toCelsius(fahrenheit: float):
  """
  Function to convert fahrenheit to celsius

  Parameters
  >fahrenheit: float

  Returns
  >float
    (5/9)(fahrenheit-32)
  """

  return ((fahrenheit-32)*5)/9

fahrenheit = input("Enter the temperature in fahrenheit: ")
while not fahrenheit.isnumeric() or not fahrenheit.isdecimal():
  fahrenheit = input("Enter the temperature in fahrenheit: ")
  if fahrenheit.isnumeric() or fahrenheit.isdecimal():
    break
print(fahrenheit, "fahrenheit is", toCelsius(float(fahrenheit)), "celsius")
print()

#7.
def largestNum(firstNum: float, secondNum: float, thirdNum: float):
  """
  Function to find the largest number out of 3 numbers

  Parameters
  >firstNum: float
  >secondNum: float
  >thirdNum: float

  Returns:
  >float
    the largest number out of the 3 Parameters
  """
  numList = [firstNum, secondNum, thirdNum]
  numList = sort(numList)
  return round(numList[2],18)

firstNum = input("Enter the first number: ")
while not firstNum.isnumeric() or not firstNum.isdecimal():
  firstNum = input("Enter the first number: ")
  if firstNum.isnumeric() or firstNum.isdecimal():
    break
secondNum = input("Enter the second number: ")
while not secondNum.isnumeric() or not secondNum.isdecimal():
  secondNum = input("Enter the second number: ")
  if secondNum.isnumeric() or secondNum.isdecimal():
    break
thirdNum = input("Enter the second number: ")
while not thirdnum.isnumeric() or not thirdNum.isdecimal():
  thirdNum = input("Enter the second number: ")
  if thirdNum.isnumeric() or thirdNum.isdecimal():
    break

print("The largest number is", largestNum(float(firstNum), float(secondNum), float(thirdNum)))