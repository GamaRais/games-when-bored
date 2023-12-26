import random

def seperator():
    print("----------------------------------------")
def titleornah():
    yeornah = input("Would you like to restart? (Y/N)\n")
    if yeornah == 'y' or yeornah == 'Y':
        gameis()
    else:
        exit()
def fishornah():
    pushingpositivity = input("Would you like to keep fishing? (Y/N)\n")
    if pushingpositivity == 'y' or pushingpositivity == 'Y':
        fishing()
    else:
        print("Okay")
        titleornah()
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
        titleornah()
    fishornah()
def activity():
    option2 = input("Now what will you do?\na. Find a job\nb. Go fishing\nc. Meet your neighbors\n")
    if option2 == "a":
        seperator()
        job = input("You have multiple job offers, which one do you take?\na. A paid internship at a software firm where the pay is 30 dollars per hour\nb. Retail worker with 7 dollars per hour\nc. Teaching job that pays horrible but boosts social stats and work ethic\n")
        if job == "a":
            seperator()
            chance = random.randint(1, 5)
            if chance == 1:
                print("You got hired for a one-day internship. You can reapply later on.")
                time = random.randint(1, 7)
                money = (30*time)
                seperator()
                print(f"You worked {time} hours and earned {money} dollars. Your internship has ended")
            else:
                print("You didn't make the internship. You can always reapply, though.")
                seperator()
                activity()
        elif job == "b":
            seperator()
            activity()
        elif job == "c":
            seperator()
            activity()
    elif option2 == "b":
        fishing()
    elif option2 == "c":
        seperator()
        neighbors = ("Angela", "Michael", "Andrew", "Julia", "Freddy", "Robertson", "Pogba", "Drogba", "Mesut", "Kyool")
        neighbor = random.choice(neighbors)
        if neighbor == 'Angela' or neighbor == 'Julia':
            acceptance = input(f"Your neighbor is {neighbor}, and she welcomes you in. Do you accept? (Y/N)\n")
        else:
            acceptance = input(f"Your neighbor is {neighbor}, and he welcomes you in. Do you accept? (Y/N)\n")
        if acceptance == 'y' or acceptance == 'Y':
            tea = input(f"{neighbor} offers to make you tea. (Y/N)\n")
            if tea == 'y' or tea == 'Y':
                print("You both had a nice time")
                seperator()
                if neighbor == 'Freddy':
                    pizzeria = input("Some time passes and Freddy offers to show you to his pizza parlor (Y/N)\n")
                    if pizzeria == 'y' or pizzeria == 'Y':
                        backstage = input("You had a nice pizza, and afterwards he offers to show you backstage (Y/N)\n")
                        if backstage == 'y' or backstage == 'Y':
                            print("You got chased down by Foxy and died via his hook")
                            print("*GAME OVER*")
                            seperator
                            titleornah()
                    else:
                        print("You went home safely")
                        seperator()
                        activity()
                activity()
        else:
            activity()
def gameis():
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
        print("GAME OVER")
        exit()
    else:
        print("Sorry, but your answer was not picked up by our systems.")
        print("GAME OVER")
        seperator()
    activity()
username = input("Username: ")
gameis()
