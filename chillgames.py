#imports
import random
#this is the start of a game
#seperator function
def seperator():
    print("----------------------------------------")
#ask to go fishing
def fishornah():
    pushingpositivity = input("Would you like to keep fishing? (Y/N)\n")
    if pushingpositivity == 'y' or 'Y':
        fishing()
    else:
        titleornah()
#activity function
def fishing():
    seperator()
    option3 = ("marlin", "shark", "sardine", "tuna", "seasnake")
    collection = random.choice(option3)
    if collection == 'marlin':
        value = random.randint(200, 400)
        print(f"Wow! you caught a {value} pound marlin!")
    elif collection == 'shark':
        value = random.randint(85, 525)
        print(f"Wow! you caught a {value} pound shark!")
    elif collection == 'sardine':
        print("Tough luck, you caught a 3-gram sardine")
    elif collection == 'tuna':
        value = random.randint(79, 1800)
        print(f"You caught a {value} pound tuna!")
    elif collection == 'seasnake':
        print("Tough luck, it was very venomous and it bit you. You died in the hospital")
        exit()
    fishornah()
#python valley function   
def pythonvalley():
    print("Hello and welcome to Python Valley, where it is not a terminal version of stardew valley.")
    seperator()
    print(f"Hello {username}, I welcome you on this island. I will lead you to your stay")
    house = ("_________\n|       |\n|       |\n|   _   |\n|__|_|__|")
    print(f"{house}")
    seperator()
    option1 = input("Pick any of the following dialogue options. Just type the letter that corresponds with the option.\na. 'Wow, thank you so much for this house, I really could not thank you enough!\nb. 'Ew, this is a disgusting house. Are there any spare houses I can buy?\n")
    if option1 == 'a':
        seperator()
        print("Why your welcome, I really hope you enjoy your stay here. Remember that you have to pay me by the end of the month, though, or else we will have to go through the eviction process.")
    elif option1 == 'b':
        print(f"How dare you {username}, leave this establishment at once!\n Game Over")
        titleornah()
    else:
        print("Sorry, but your answer was not picked up by our systems.")
        titleornah()
        seperator()
    option2 = input("Now what will you do?\na. Find a job\nb. Go fishing\nc. Meet your neighbors\n")
    if option2 == "a":
        seperator()
        job = input("You have multiple job offers, which one do you take?\na. A paid internship at a software firm where the pay is 30 dollars per hour\nb. Retail worker with 23 dollars per hour\nc. Teaching job that pays horrible but boosts social stats and work ethic\n")
        if job == "a":
            seperator()
            hours = random.randint(1, 8)
            pay = 30*hours
            print("You worked there for {hours} hours and earned {pay} dollars")
        elif job == "b":
            seperator()
            print("You work there for a solid 4 months before being fired due to inflation. You are now homeless because your already unsustainable job pay was barely enough to pay rent and die on the streets due to hypothermia.\n WOEST ENDING")
        elif job == "c":
            seperator()
            print("You foresaw the success of a whole generation of kids and they turn the already modern landscape into a eutopian society filled with drones, skyscrapers, and etc. You didn't do anything special individually, but you helped this society learn and turn into what it is now\n Neutral Ending")
    elif option2 == "b":
        fishing()
    elif option2 == "c":
        seperator()
        print("You had very nice neighbors and they all greeted you and welcomed you into their home\nMEH ENDING")
    titleornah()
#TicTacToe
def rockpaperscissors():
    options = ("rock", "paper", "scissors")
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Pick one of the three (rock, paper, scissors): ")

    seperator()
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("*Draw*")
    elif player == "rock" and computer == "scissors":
        print("*You Win!*")
    elif player == "paper" and computer == "rock":
        print("*You Win!*")
    elif player == "scissors" and computer == "paper":
        print("*You Win!*")
    else:
        print("*You Lose!*")
    titleornah()
#question to go back to title
def titleornah():
    seperator()
    yesorno = input("Would you like to go back to the title screen? (Y/N)\n")
    if yesorno == 'y' or yesorno == 'Y':
        title()
    elif yesorno == 'n' or yesorno == 'N':
        exit()
    else:
        print("It seems your answer was not inputted correctly")
        titleornah()
#title function
def title():
        options = input(f"Hello {username}, please select from the list of games:\n a. Python Valley\n b. Rock Paper Scissors\n")
        if options == 'a':
            pythonvalley()
        if options == 'b':
            rockpaperscissors()

#start game
username = input("Username: ")
title()
