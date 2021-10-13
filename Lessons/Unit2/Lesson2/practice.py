# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-10-13

import random

#Example 1.
integer = int(input("Enter an integer: "))
if integer > 0:
    print("Your number is positive")
if integer == 0:
    print("Your number is zero")
if integer < 0:
    print("Your number is negative")
print("Thanks for using my program")
print()

#Example 2.
number = random.randint(1,6)
if number % 2 == 0:
    print("Your number is even")
if number % 2 != 0:
    print("Your number is negative")
print()

#Example 3.
scheduled = int(input("Enter the scheduled time of arrival (hhmm): "))
estimated = int(input("Enter the estimated time of arrival (hhmm): "))
if scheduled > estimated:
    print("Your flight isearly")
if scheduled == estimated:
    print("Your flight is on time")
if scheduled < estimated:
    print("Your flight is delayed")
print()