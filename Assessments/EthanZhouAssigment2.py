#Ethan Zhou
#ICS2O1
#Ms Wun
#2021-10-15

#1.
try:
    #get input
    number = int(input("Enter a number between 1 and 10: "))
    if number >= 1 and number <= 10:
        #hardcoding the roman numerals
        if number == 1:
            print("The roman numeral for", number, "is I.")
        if number == 2:
            print("The roman numeral for", number, "is II.")
        if number == 3:
            print("The roman numeral for", number, "is III.")
        if number == 4:
            print("The roman numeral for", number, "is IV.")
        if number == 5:
            print("The roman numeral for", number, "is V.")
        if number == 6:
            print("The roman numeral for", number, "is VI.")
        if number == 7:
            print("The roman numeral for", number, "is VII.")
        if number == 8:
            print("The roman numeral for", number, "is VIII.")
        if number == 9:
            print("The roman numeral for", number, "is IX.")
        if number == 10:
            print("The roman numeral for", number, "is X.")
    else:
        print("ERROR: That is not between 1 and 10.")
except ValueError:
    print("ERROR: That is an invalid number.")
print()

#2.
try:
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year: "))

    #days in months
    january = 31
    feburary = 28
    feburaryLeap = 29
    march = 31
    april = 30
    may = 31
    june = 30
    july = 31
    august = 31
    september = 30
    october = 31
    november = 30
    december = 31

    #Date detections
    if month >= 1 and month <= 12:
        if year % 100 == 0 and year % 400 == 0:
            if year % 100 != 0 and year % 4 == 0:
                #leap year
                if month == 1:
                    print("There are", january, "days in January")
                if month == 2:
                    print("There are", feburaryLeap, "days in Feburary")
                if month == 3:
                    print("There are", march, "days in March")
                if month == 4:
                    print("There are", april, "days in April")
                if month == 5:
                    print("There are", may, "days in May")
                if month == 6:
                    print("There are", june, "days in June")
                if month == 7:
                    print("There are", july, "days in July")
                if month == 8:
                    print("There are", august, "days in August")
                if month == 9:
                    print("There are", september, "days in September")
                if month == 10:
                    print("There are", october, "days in October")
                if month == 11:
                    print("There are", november, "days in November")
                if month == 12:
                    print("There are", december, "days in December")
            else:
                #not a leap year
                if month == 1:
                    print("There are", january, "days in January")
                if month == 2:
                    print("There are", feburary, "days in Feburary")
                if month == 3:
                    print("There are", march, "days in March")
                if month == 4:
                    print("There are", april, "days in April")
                if month == 5:
                    print("There are", may, "days in May")
                if month == 6:
                    print("There are", june, "days in June")
                if month == 7:
                    print("There are", july, "days in July")
                if month == 8:
                    print("There are", august, "days in August")
                if month == 9:
                    print("There are", september, "days in September")
                if month == 10:
                    print("There are", october, "days in October")
                if month == 11:
                    print("There are", november, "days in November")
                if month == 12:
                    print("There are", december, "days in December")
        else:
            #not a leap year
            if month == 1:
                    print("There are", january, "days in January")
            if month == 2:
                print("There are", feburary, "days in Feburary")
            if month == 3:
                print("There are", march, "days in March")
            if month == 4:
                print("There are", april, "days in April")
            if month == 5:
                print("There are", may, "days in May")
            if month == 6:
                print("There are", june, "days in June")
            if month == 7:
                print("There are", july, "days in July")
            if month == 8:
                print("There are", august, "days in August")
            if month == 9:
                print("There are", september, "days in September")
            if month == 10:
                print("There are", october, "days in October")
            if month == 11:
                print("There are", november, "days in November")
            if month == 12:
                print("There are", december, "days in December")
    else:
        print("ERROR: That is an invalid input")
except ValueError:
    print("ERROR: That is an invalid input")
print()

#3.
try:
    #menu
    print("GEOMETRY CALCULATOR\n")
    print("1. Area of Circle")
    print("2. Area of Rectangle")
    print("3. Area of Triangle")
    print("4. Quit")
    print()
    #choice
    choice = int(input("Please enter your choice (1-4): "))
    print()
    #math
    if choice == 1:
        #circle
        print("AREA OF A CIRCLE\n")
        radius = float(input("Enter the radius (cm): "))
        pi = 3.14
        print("\nThe area of the circle is", round((radius**2)*pi, 2), "squared cm.\n")
        print("Thank you for using my geometry calculator!\n\n***")
    if choice == 2:
        #rectangle
        print("AREA OF A RECTANGLE\n")
        length = float(input("Enter the length (cm): "))
        width = float(input("Enter the width (cm): "))
        print("\nThe area of the rectangle is", round(length*width,2), "squared cm.\n")
        print("Thank you for using my geometry calculator!\n\n***")
    if choice == 3:
        #triangle
        print("AREA OF A TRIANGLE\n")
        base = float(input("Enter the base (cm): "))
        height = float(input("Enter the height (cm): "))
        print("\nThe area of the rectangle is", round((base*length)/2,2), "squared cm.\n")
        print("Thank you for using my geometry calculator!\n\n***")
    if choice == 4:
        #quiting
        print("Good bye!")
        print("Thank you for using the Geometry Calculator!\n")
except ValueError:
    print("ERROR: There was an invalid input")