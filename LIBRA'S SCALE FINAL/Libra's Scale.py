
# This is the final draft of my first video game, 'Libra's Scale'! I hope that you enjoy! - Kye Nicholas Kalb 2022
import time
from token import SOFT_KEYWORD
import turtle
import random
from random import randint

def main():

    inventory = []
    getitem = ['Item']
    directions = {
        'North',
        'South',
        'East',
        'West',
        }

    rooms = {
        'Dungeon Entrance': {'North':'Opening Hall'},
        'Opening Hall': {'West':'Villain\'s Headquarters', 'North':'Alchemy Lab', 'South':'Dungeon Entrance'},
        'Villain\'s Headquarters': {'East':'Opening Hall'},
        'Alchemy Lab': {'North':'Prison', 'South':'Opening Hall', 'East':'Church'},
        'Church': {'East':'Wizard\s Quarters', 'West':'Alchemy Lab'},
        'Wizard\s Quarters': {'North':'Dining Hall', 'West':'Church'},
        'Dining Hall': {'South':'Wizard\s Quarters', 'West':'Kitchen'},
        'Kitchen': {'West':'Prison', 'East':'Dining Hall'},
        'Prison': {'South':'Alchemy Lab', 'East':'Kitchen'},
    }

    items = {
        'Opening Hall':'Sheath',
        'Villain\'s Headquarters':'Pommel',
        'Alchemy Lab':'Handle',
        'Church':'Blade 1/2',
        'Dining Hall':'Guard',
        'Prison':'Blade 2/2'
    }



    currentroom = 'Dungeon Entrance'
    newroom = ''
    inventory = []
    swordpieces = 0
    loopingvar = True

    while loopingvar == True:
        #main game display
        print("                               ")
        print("-------------------------------")
        print("You are in the " + str(currentroom))
        print("You have: " + str(inventory))
        print("-------------------------------")
        print("                               ")
        choiceorig = input("What would you like to do? (Enter a cardinal direction, or 'Item'.) > ")
        choice = str.title(choiceorig)
        #moves player
        if choice in directions:
            if choice in rooms[currentroom]:
                currentroom = rooms[currentroom][choice]
            else:
                print("You cannot go that way.")
        #lets player pick up items
        elif choice in getitem:
            if currentroom in items:
                inventory.append(items[currentroom])
                print("Look! A piece of your sword!")
                del items[currentroom]
                swordpieces += 1
            else:
                print("You don't see a piece of your sword in here...")
        elif swordpieces == 6 and choice == "Reforge":
            loopingvar = False
            print("You have all the pieces!")
            time.sleep(2)
            print("As you lay all of the pieces out in front of you, a bright light starts to glow")
            time.sleep(2)
            print("All six pieces of your sword slowly start to raise from the ground and meld together!")
            time.sleep(2)
            print("From the glowing light, your sword, as sharp as ever, returns once again to your hands")
            time.sleep(2)
            print("You've done it! You've restored your legendary blade to it's former glory!")
            time.sleep(2)
            print("You can now battle your enemy and save your son!")
            time.sleep(2)
            battlenow()

def battlenow():
    battlenow = input("Would you like to face your enemy now? (answer with y/n) > ")
    if battlenow == 'y':
        battle()
    elif battlenow == 'n':
        print("You can't give up now!")
    else:
        print("Invalid input, please try again.")

        



def battle():
    attacks = ["You swing your blade as hard as you can!", "As you swing your weapon, you feel the strength rush through you!", "You attack your enemy!", "Tired or not, you will save your son!"]
    print("As you enter the chambers of your enemy, you hear your son call out for you.")
    time.sleep(1)
    print("They're crying. Water lines the room, a cold floor made of blood red bricks lay underneath your feet.")
    time.sleep(1)
    print("For this next part of the game, you're going to type 'Attack' or 'Dodge' to battle the villain.")
    time.sleep(1)
    print("Attacking will deal a random d12 of damage to your enemy, and dodging will nullify their attack for their turn.")
    time.sleep(1)
    print("This will require a little bit of luck. Good luck!")
    time.sleep(1)

    playerhealth = 75
    bosshealth = 100

    while bosshealth >= 0:
        print("                               ")
        print("-------------------------------")
        print("Your Current HP: " + str(playerhealth))
        print("Boss's Current HP: " + str(bosshealth))
        print("-------------------------------")
        print("                               ")
        battlechoiceorig = input("Would you like to dodge or attack? > ")
        battlechoice = str.title(battlechoiceorig)
        if battlechoice == "Attack":
            dtwelve = randint(1, 12)
            print(random.choice(attacks))
            bosshealth = bosshealth - dtwelve
            print("You deal " + str(dtwelve) + " damage!")
            time.sleep(1)
            print("The villain attacks back!")
            deight = randint(1, 8)
            playerhealth = playerhealth - deight
            print("You take " + str(deight) + " damage!")
            if playerhealth == 0:
                print("You've been defeated, and your enemy escapes with their hostage!")
                time.sleep(1)
                print("Who's going to save them now?!")
                time.sleep(1)
                print("You need to rise and try again!")
                time.sleep(1)
                title()
            elif bosshealth == 0:
                print("Your blade finally pierces your enemy through their heart, slaying the evil in the dungeon!")
                time.sleep(1)
                print("Your son clings to you with happiness, and you're able to finally leave your adventuring behind.")
                time.sleep(1)
                print("Congratulations! You've slain the evil, rescued your kid, and completed your mission!")
                time.sleep(1)
                print("Thank you so much for playing my game, I hope that you enjoyed it!")
                time.sleep(1)
                credits()
            else:
                continue
        elif battlechoice == "Dodge":
            print("You dodged their attack!")
        else:
            print("That's not an option right now! You've gotta attack or dodge!")


def credits():
    print("Game IP: Kye Kalb")
    time.sleep(1)
    print("Programming: Kye Kalb")
    time.sleep(1)
    print("More Programming: Kye Kalb")
    time.sleep(1)
    print("Like, Everything Else: Kye Kalb")
    time.sleep(1)
    print("Thanks again for playing! I'll return you to the main menu in 10 seconds.")
    time.sleep(10)
    title()


def title():

    print("Welcome to Libra's Scale! This is a text-based adventure game.")
    time.sleep(1)
    print("You are a retired adventurer who's archnemesis has come back from the netherrealm to make your life hell.")
    time.sleep(1)
    print("They've kidnapped your son, and they've taken them deep into a dungeon.")
    time.sleep(1)
    print("In your final battle with your nemesis, they shattered your sword into six pieces.")
    time.sleep(1)
    print("Brave this dungeon, find your sword's pieces, reforge it, and defeat your enemy!")
    time.sleep(1)
    print("Once you have all six pieces of your sword, type 'Reforge' to wield your blade once more!")
    time.sleep(1)
    
    enter = input("Your son is waiting for you! Will you enter the dungeon? Respond with y/n: ")
    
    if enter == 'y':
        main()

print("Welcome to Libra's Scale! This is a text-based adventure game.")
time.sleep(1)
print("You are a retired adventurer who's archnemesis has come back from the netherrealm to make your life hell.")
time.sleep(1)
print("They've kidnapped your son, and they've taken them deep into a dungeon.")
time.sleep(1)
print("In your final battle with your nemesis, they shattered your sword into six pieces.")
time.sleep(1)
print("Brave this dungeon, find your sword's pieces, reforge it, and defeat your enemy!")
time.sleep(1)
print("Once you have all six pieces of your sword, type 'Reforge' to wield your blade once more!")
time.sleep(1)

enter = input("Your son is waiting for you! Will you enter the dungeon? Respond with y/n: ")

if enter == 'y':
    main()
else:
    print("Okay, maybe next time then!")
    exit