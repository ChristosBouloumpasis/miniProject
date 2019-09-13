#TASK
# 1) As a user, I want to use a command-line application that will output a predefined list of the names of the people in my team as well as a
# 2) list of the drinks that people in my team typically ask for, so that I can remember everybody’s names and see if all of the drinks are available to make.
#    As a user, I want to invoke the application and get a list of the people in my team as well as the available drinks E.g. $ python3 app.py get-people
# 3) As a user, I want a nicer, interactive menu to use the application, so that I don’t have to be remembering and typing out commands all the time
# 4) As a user, I want to add new drinks and people to the app so that I can keep the app up-to-date, in case people leave or join the team, or new drinks are available
# 5) As a user, I want to be able to store the favourite drink of everyone in my team, so I know what to get them when they ask for a drink.
# 6) As a user, I want to be able to save all the drinks and people names I’ve entered in the app so that I don’t have to re-enter them every time I restart the app


import os
from rounds import Round

def saveOrderFile(orders):
    with open('orders.txt','w') as ordersfile:
        for key, value in orders.items():
            ordersfile.write(f"{key},{value}\n")



##############################################################################
###
###
##############################################################################
def savePersonFile(person):
    with open('people.txt','a') as peoplefile:
        peoplefile.write(person + "\n")

##############################################################################
###
###
##############################################################################
def saveDrinkFile(drink):
    with open('drinks.txt','a') as drinksfile:
        drinksfile.write(drink + "\n")

##############################################################################
###
###
##############################################################################
def saveChoicesFile(choices):
    with open('choices.txt','a') as choicesfile:
        for key, value in choices:
            choicesfile.write(key + ", " + value + "\n")

##############################################################################
###
###
##############################################################################
def saveChoiceFile(choice):
    with open('choices.txt','a') as choicesfile:
        choicesfile.write(choice + "\n")


##############################################################################
###
### Prints dictionary
##############################################################################
def printDict(title, body):
    print("+==================================================================+")
    print(f"|  {title}")
    print("+==================================================================+")
    index = 1
    for key, value in body.items():
        print(f"| {index}) {key} - {value}")
        index = index + 1
    print("+==================================================================+")


def readOrdersFile():
    ordersDict = {}
    with open('orders.txt','r') as orders_file:
        orders = orders_file.readlines()
    for order in orders:
        ordersArray = [x.strip() for x in order.split(',')]
        ordersDict[ordersArray[0]] = ordersArray[1]

    printDict("The round",ordersDict)
    # return choicesDict
##############################################################################
###
###
##############################################################################
def readChoicesFile():
    choicesDict = {}
    with open('choices.txt','r') as choices_file:
        choices = choices_file.readlines()
    for choice in choices:
        choiceArray = [x.strip() for x in choice.split(',')]
        choicesDict[choiceArray[0]] = choiceArray[1]

    printDict("People and their choices",choicesDict)
    return choicesDict
##############################################################################
###
###
##############################################################################
def readPeopleFile():
    with open('people.txt','r') as people_file:
        people = people_file.readlines()
        return people
##############################################################################
###
###
##############################################################################
def readDrinksFile():
   with  open('drinks.txt','r') as drinks_file: #Use some memory managment
    people = drinks_file.readlines()
    return people
##############################################################################
###
###
##############################################################################
def printList(title, body):
    print("+==================================================================+")
    print(f"|  {title}")
    print("+==================================================================+")
    for item in body:
        print(f"| {body.index(item) + 1}  {item}")
    print("+==================================================================+")




##############################################################################
###              Add People menu
##############################################################################
def inputNewPeople(people):
    printList("People", people)
    newPeopleMenu = """
Please enter a list of people, name by name
    """
    peopleList = []
    print(newPeopleMenu)
    print("Input a new person")
    # number of elemetns as input
    continueInput = "y"
    while continueInput.lower() == "y":
        ele = input("Enter the name here:")
        peopleList.append(ele)
        savePersonFile(ele)
        continueInput = input("Do you want to enter another name? [Y/N]: ")
        print("The input was: " + continueInput)

    print("Your new list of people has been registered")
    return peopleList

##############################################################################
###              Add People with a favourite drink
##############################################################################
def inputNewPeopleWithDrinks(people):
    #TODO The user might give you a invalid input here so you need to protect yourself from that
    newPeopleMenu = """
    Please set one favorite drink for each person
    """
    printList("People", people)
    print(newPeopleMenu)

    peopleList = {}
    continueInput = "y"
    while continueInput.lower() == "y":
        index = int(input("Type the corresponding number of that person here: "))
        drink = input("Now enter the person's favorite drink here: ")
        peopleList[people[index - 1]] = drink
        continueInput = input("Do you want to pick a drink for another person? [Y/N]: ")
        print(continueInput)

    print("Your new list of people and drinks has been registered")
    print(peopleList)
    return peopleList

##############################################################################
###              Add Drinks menu
##############################################################################
def inputNewDrinks():
    newDrinksMenu = """
Please enter a list of drinks, name by name
    """
    drinksList = []
    print(newDrinksMenu)
    print("Enter the first name here:")
    # number of elemetns as input
    continueInput = "y"
    while continueInput.lower() == "y":
        ele = input()
        drinksList.append(ele)
        continueInput = input("Do you want to enter another name? [Y/N]:")


    print("Your new list of people has been registered")
    return drinksList

##############################################################################
###      Create round menu
##############################################################################
def createRound():
    newDrinksMenu = """Please create an order of drinks by typing the name of the person."""
    print(newDrinksMenu)
    creatorName = input("First type your own name here: ")
    newround = Round(creatorName)
    choices = readChoicesFile()
    continueInput = "y"
    while continueInput.lower() == "y":
        orderName = input("Type the name here: ")
        newround.inputChoice(choices[orderName], orderName)
        continueInput = input("Do you want to enter another order? [Y/N]:")

    result = newround.getRound()
    saveOrderFile(result["Round"])





##############################################################################
###       MENU CHOICE
##############################################################################
def acceptArguments(input):
    listPeople = readPeopleFile()
    listDrinks = readDrinksFile()

    if input == "1":
        printList("PEOPLE", listPeople)
        return True
    elif input == "2":
        printList("DRINKS", listDrinks)
        return True
    elif input == "3":
        inputNewPeople(listPeople)
        return True
    elif input == "4":
        inputNewDrinks()
        return True
    elif input == "5":
        choices = inputNewPeopleWithDrinks(listPeople)
        #Save people to file
        saveChoicesFile(choices)
        return True
    elif input == "6":
        readChoicesFile()
        return True
    elif input == "7":
        createRound()
        return True
    elif input.lower() == "help" or input.lower() == "8":
        print("Really now, you need help, just read the menu mate.")
        return True
    elif input == "9":
        return False
    elif input == "10":
        readOrdersFile()
        return True
    else:
        print("That is not a valid command. Type help to find what command you can ")
        return True


##############################################################################
### MAIN PROG
##############################################################################
try:
    mainLoopRunning = True
    while mainLoopRunning == True:
        menu = """ 
           Welcome to BrIW v0.1
           Please, select an option below by entering a number:
         
                [1] Get all people 
                [2] Get all drinks
                [3] Add people
                [4] Add drinks 
                [5] Add People With Fav Drinks
                [6] Print Dictionary
                [7] Create Round
                [8] Help
                [9] Exit
                [10] Bring Round
        
        """
        print(menu)
        choice = input("Type your choice here: \n")
        os.system('clear')
        mainLoopRunning = acceptArguments(choice)
    print("Goodbye, see you soon!")
except Exception as e:
    print(e)





