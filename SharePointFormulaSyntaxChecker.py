import random
import sys

officialHelp = "https://support.microsoft.com/en-us/office/introduction-to-sharepoint-formulas-and-functions-94e1b4cc-cd1c-49c2-80ec-90c9b9591f47"

def FormulaChecker(command):
    return "\n{0} your command have syntax errors. {1}\n".format(random.choice(foo), random.choice(bar))

def CheckSyntax():
    print("Enter your formula:")
    inputCommand = input()
    print("{0}".format(FormulaChecker(inputCommand)))  

def HandleInput(number):
    if number == 1:
        CheckSyntax()
        PrintMenu()
    elif number == 2:
        PrintHelp()
        PrintMenu()
    elif number == 3:
        sys.exit("Exit")
    else:
        print("Unknown command, try again.")

def PrintMenu():
    print("1. Check command syntax.")
    print("2. Help")
    print("3. Exit program")
    print("Enter option:")
    try:
        choice = int(input())
        HandleInput(choice)
    except SystemExit:
        print("Exiting program.")
    except:
        print("Unknown command, try again.")
        PrintMenu()

def PrintHelp():
    print("Check the official documentation for guidance in the mysterious world of SharePoint formulas: {0}\n".format(officialHelp))

def InitializeData():
    global foo
    foo = ["Nope,","Hey,","Hmm,","Eehm... this is embarrasing,","Hahahahah,", "Oh,","Wow,", "Amazingly enough, ","Syntax valid! \n No, just kidding,"]
    global bar
    bar = ["What's wrong? Hell if I know...","Tough luck bruv.", "Wait no...yea, still wrong.", "Perhaps you should try the help option.", "Just give up like the rest of us.", "I could give you information on WHAT went wrong, but that would spoil all the SharePoint fun now would it?", "I will spare you the trouble: https://bfy.tw/P9vg", "Welcome to the wonderful world of SharePoint! Please come again."]

if __name__ == "__main__":
    print("Welcome to the SharePoint Formula syntax checker for SharePoint on premises 2013/2016.")
    InitializeData()
    PrintMenu()
