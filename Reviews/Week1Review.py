# Programmed by: Ethan Zhou
# Programmed on: 2021-09-27
# Programmed for: Ms Wun ICS2O1

#1.
print(42/5)

print(42//5)

print(42%5)

print(40%5)

print(1%2)

print(2%1)

print(45+4*4-2)

print(45 + 43 % 5 * (23 * 3 % 2))

print(5**2)

print(5.1**2)
print()

#2.
price = float(input("How much is your item? "))
amount = float(input("How many would you like to purchase? "))
print("$"+str(round((price*amount)*1.13,2)))
print()

#3.
width = float(input("Enter the width of the rectangle (cm): "))
length = float(input("Enter the length of the rectangle (cm): "))
print("The perimeter is", width+width+length+length, "cm")
print("The area is", width*length, "squared cm")
print()

#4.
diameter = float(input("Enter the diameter of the pizza in inches: "))
cost = (0.05*(diameter**2))+0.75+1
print("The cost of making the pizza is: $" + "%.2f" %cost)
print()

#5.
time = float(input("Input a time less than 4.5 seconds "))
if time > 4.5:
  while time < 4.5:
    time = float(input("Input a time less than 4.5 seconds "))
print("The height of the object is:", 100-(4.5*(time**2)), "meters")
print()

#6.
amount = float(input("Enter the amount of meal: "))
tip = float(input("Enter the tip as a percentage: "))/100
tax = float(input("Enter the tax rate as a percentage: "))/100
total = amount+(amount*tip)+(amount*tax)

print("Amount of meal:", amount)
print("Tip:", "$" + str(round(amount*tip,2)))
print("Tax:", "$" + str(round(amount*tax,2)))
print("Total:", "$" + str(round(total,2)))
print()

#7.
employeeName = input("Employee Name: ")
hours = float(input("Number of hours worked in a week: "))
pay = float(input("Enter hourly pay rate: "))
gross = hours*pay
federal = float(input("Enter federal withholding rate: "))
state = float(input("Enter state tax withholding rate: "))
totalDeduction = round((pay*federal*10) + (pay*state*10),2)

print("Employee name:", employeeName)
print("Hours worked:", hours)
print("Pay rate:", "$" + str(pay) , "Per Hour")
print("Gross pay:", "$" + str(gross))
print("Deductions:")
print(" Federal Withholding (" + str(federal*10) + "%):", "$" + str(round(pay*federal*10,2)))
print(" State Withholding (" + str(state*10) + "%):", "$" + str(round(pay*state*10,2)))
print(" Total Deduction:", "$" + str(totalDeduction))
print("Net Pay: $" + str(gross-totalDeduction))