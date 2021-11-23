# Ethan Zhou
# ICS2O1
# Ms Wun
# 2021-11-23

def enterMarks():
    """
    Function to write initial marks in a file called ICSMarks.txt

    Parameters
    >none

    Returns
    >file change
        write the file to the following format:
            --name --mark
    """
    file = open("ICSMarks.txt", 'w')
    keepGoing = True
    while keepGoing:
    #Get Information
        print("Enter the following information. Type \"x\" to stop.")
        name = input("Enter name: ")
        if name.lower() != "x":
            mark = float(input("Enter mark: "))
            print("")
        
            file.write(name + " ")
            file.write(str(mark))
            file.write("\n")
        else:
            keepGoing = False
            file.close()

def addMarks():
    """
    Function to add more marks into the file ICSMarks.txt

    Parameters
    >none

    Returns
    >File change
        Adds more lines into ICSMarks.txt in the following format:
            --name --mark
    """
    file = open("ICSMarks.txt", 'a')
    
    keepGoing = True
    
    while keepGoing:
        print("Enter the following information. Type \"x\" to stop.")
        name = input("Enter name: ")
        
        if name.lower() != "x":
            mark = float(input("Enter mark: "))
            print("")
        
            file.write(name + " ")
            file.write(str(mark))
            file.write("\n")
        else:
            keepGoing = False
            file.close()
    
def changeMarks():
    """
    Function that rewrites the file with new string with modified marks

    Parameters
    >none

    Returns
    >File change
        Rewrites the entire file with an accumulator called data in this format:
            --name --mark
    """
    file = open("ICSMarks.txt", 'r')
    
    name = input("Enter the name of the student: ")
    newMark = float(input("Enter the new mark: "))
    
    #data is acc
    data = ""
    
    for line in file:
        if line != "\n":    
            student = line.split(" ")   
        
            sName = student[0]
            sMark = student[1]      
        
            if sName == name:
                sMark = str(newMark)+"\n"
        
            data += sName + " " + sMark
    
    file.close()
    
    file = open("ICSMarks.txt", 'w')
    file.write(data)
    file.close()
def menu():
    """
    Function that creates a menu and runs the functions based on the user's input

    Paramerters
    >none

    Returns
    >none

    *It just organises the functions and runs them
    """
    print("Hello User, please select from the following menu: ")
    print("1 -- Enter a new set of marks")
    print("2 -- Add to existing set of marks")
    print("3 -- Change a mark")
    print("4 -- Exit Program")
    choice = input("Enter your choice: ")
    print(" ")
    
    if choice == "1":
        enterMarks()
        print(" ")
        menu()
    elif choice == "2":
        addMarks()
        print(" ")
        menu()
    elif choice == "3":
        changeMarks()
        print(" ")
        menu()
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid choice. Try again.")
        menu()
    
#RUNNING THE PROGRAM
menu()

