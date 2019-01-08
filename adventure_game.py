# You are welcome to write and include any other Python files you want or need
# however your game must be started by calling the main function in this file.
#Ryan Sleeper
#Adventure Game
from random import random
from random import randrange

def mainCharacter():                 #This creates the main character
    playerName = input("Enter your player's name: ")
    specialAbility = input("Choose a special ability: Super Strength (Strength) or Super Speed (Speed): ")
    if specialAbility == "Strength":
        attack = 10
        probOfRun = .25
    else:
        attack = 5
        probOfRun = .75
    if not(specialAbility == "Strength" or specialAbility == "Speed"):
        attack = 5
        probOfRun = .5
    accuracy = .75
    playerHealth = 100
    playerEndurance = 100
    playerCash = 0

    return playerName, specialAbility, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy

def enemy1():                  #These are all of the enemies the main character may have to fight
    enemy = "Shark Man"
    enemyHealth = 25
    probOfHitting = .4
    enemyAttack = 5
    amountOfCash = 25
    return enemy, enemyHealth, probOfHitting, enemyAttack, amountOfCash

def enemy2():
    enemy = "Captain Black Beard"
    enemyHealth = 35
    probOfHitting = .5
    enemyAttack = 6
    amountOfCash = 35
    return enemy, enemyHealth, probOfHitting, enemyAttack, amountOfCash

def enemy3():
    enemy = "Kraken"
    enemyHealth = 50
    probOfHitting = .6
    enemyAttack = 10
    amountOfCash = 50
    return enemy, enemyHealth, probOfHitting, enemyAttack, amountOfCash

def enemy4():
    enemy = "Village Guard"
    enemyHealth = 50
    probOfHitting = .7
    enemyAttack = 7
    amountOfCash = 50
    return enemy, enemyHealth, probOfHitting, enemyAttack, amountOfCash

def battles(playerHealth, playerCash, attack, accuracy, enemy, enemyHealth, enemyAttack, probOfHitting, amountOfCash):    #This runs all of the battles between the main character and the enemies
    while playerHealth > 0 and enemyHealth > 0:                                   
        playerAttack = random()
        if playerAttack < accuracy:
            enemyHealth = enemyHealth - attack
        else:
            enemyHealth = enemyHealth
        enemyHit = random()
        if enemyHit < probOfHitting:
            playerHealth = playerHealth - enemyAttack
        else:
            playerHealth = playerHealth
    if playerHealth <= 0:
        print("You have been defeated by {0}.".format(enemy))
        print("I hope you enjoyed the game, please play again!")
    else:
        print("Congratulations! You defeated {0}! You have earned ${1}!".format(enemy, amountOfCash))
        playerCash = playerCash + amountOfCash
        print("Health = {0}\nCash = {1}".format(playerHealth, playerCash))
    return playerHealth, playerCash
        
        
        
def runAway(probOfRun, playerEndurance):         #This is the code for if your character will be able to run away
    runAwayTry = random()
    if runAwayTry < probOfRun:
        print("Congratulations! You successfully ran away! However, in doing so, you lost a little bit of endurance.")
        playerEndurance = playerEndurance - 10
        if playerEndurance <= 0:
            print("Oh no, you have died from exhaustion.")
            print("I hope you enjoyed the game. Please play again!")
        print(playerEndurance)
        return playerEndurance
    else:
        print("Oh no, you were not fast enough to get away! You must now stay and fight!")
        return "fight"
    
#The next parts are the chapters for each step in the adventure, there are a total of 5 chapters. Most people will make it to chapter 4 but a lot lose before 5.
def chapter1():
    print("You have woken up in the middle of the ocean on a wooden raft. You have nothing except a small oar. Far into the distance you see an island.\nIt is your only hope for survival. You must get there quickly before you die of hunger or something else that may be in these treacherous waters.\nGood luck and choose wisely!")
    playerName, specialAbility, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy = mainCharacter()
    print("Welcome {0}, in this survival game you must make choices in order to get to the end. Your choices will ultimately decide whether or not you ever reach the island in the distance.\nLet's begin.".format(playerName))
    print("Here are your starting attributes: \nSpecial Ability = {0}\nHealth = {1}\nEndurance = {2}\nCash = {3}\nAttack = {4}\nChances of Running Away = {5}\nAccuracy = {6}".format(specialAbility, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy))
    print("\n")
    strangeObject = input("You see a strange object in the ocean, however it is a little out of the way towards the island. Do you want to go see what it is (y/n)? ")
    print("\n")
    enemy, enemyHealth, probOfHitting, enemyAttack, amountOfCash = enemy1()
    if strangeObject == "y":
          print("Congratulations! You have found a golden egg, this is worth $100. However, you exerted some energy going out of your way.")
          playerCash = playerCash + 100
          playerEndurance = playerEndurance - 10
          print("Cash = {}".format(playerCash))
          print("Endurance = {}".format(playerEndurance))
    else:
        print("Oh no! {0}, has just jumped onto your raft!".format(enemy))
        fight1 = input("You have two options, you can fight or run. What do you want to do? (f/r) ")
        print("\n")
        if fight1 == "f":
            playerHealth, playerCash = battles(playerHealth, playerCash, attack, accuracy, enemy, enemyHealth, enemyAttack, probOfHitting, amountOfCash)
        else:
            battleOrRun = runAway(probOfRun, playerEndurance)
            if battleOrRun == "fight":
                 playerHealth, playerCash = battles(playerHealth, playerCash, attack, accuracy, enemy, enemyHealth, enemyAttack, probOfHitting, amountOfCash)
            else:
                 playerEndurance = battleOrRun
                        
    return playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy


def chapter2(playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy):
    print("\n")
    print("Congratulations, you have made it past the first obstacle. As you row on towards the island you see a ship approaching you.")
    shipDecision = input("You have two options, you can board the ship or try to run away and hide. What would you like to do (b for board/h for hide)? ")
    print("\n")
    enemy, enemyHealth, probOfHitting, enemyAttack, amountOfCash = enemy2()
    if shipDecision == "b":
        print("Ah ha, you have boarded {0}'s pirate ship.".format(enemy))
        print("At first he is friendly but then notices you have some money on you.")
        print("He asks you for the money but you refuse.")
        fight2 = input("You have two options, fight or run away (f/r): ")
        print("\n")
        if fight2 == "f":
            playerHealth, playerCash = battles(playerHealth, playerCash, attack, accuracy, enemy, enemyHealth, enemyAttack, probOfHitting, amountOfCash)
        else:
            battleOrRun = runAway(probOfRun, playerEndurance)
            if battleOrRun == "fight":
                 playerHealth, playerCash = battles(playerHealth, playerCash, attack, accuracy, enemy, enemyHealth, enemyAttack, probOfHitting, amountOfCash)
            else:
                 playerEndurance = battleOrRun
    else:
        battleOrRun = runAway(probOfRun, playerEndurance)
        if battleOrRun == "fight":
            playerHealth, playerCash = battles(playerHealth, playerCash, attack, accuracy, enemy, enemyHealth, enemyAttack, probOfHitting, amountOfCash)
        else:
            playerEndurance = battleOrRun
    
    return playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy


def chapter3(playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy):
    enemy, enemyHealth, probOfHitting, enemyAttack, amountOfCash = enemy3()
    print("\n")
    print("Great Job! You are getting so close. The island is getting bigger and bigger.")
    print("As soon as your hope was greater than ever, a huge wave flipped over your raft flinging you into the air.")
    print("In a panic, you swim as quickly as you can to the little of what is left of your raft.")
    print("Unfortunately, you look up to realize what had caused the massive wave. Between you and the island now stands the {0}!".format(enemy))
    krakenFight = input("You have two options run (r) or fight (f): ")
    print("\n")
    while krakenFight == "r":
        print("\n")
        print("Your raft is in pieces and this monster is too quick to get away from.")
        print("You better stand up and fight before you run out of endurance.")
        playerEndurance = playerEndurance - 10
        print("Endurance = {}".format(playerEndurance))
        if playerEndurance <= 0:
            print("Oh no, you have died from exhaustion.")
            print("I hope you enjoyed the game. Please play again!")
            break
        krakenFight = input("Stand and fight (f) or try to run (r)? ")
        if krakenFight != "f":
            krakenFight = "r"
    if krakenFight == "f":
        playerHealth, playerCash = battles(playerHealth, playerCash, attack, accuracy, enemy, enemyHealth, enemyAttack, probOfHitting, amountOfCash)
    
    return playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy


def chapter4(playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy):
    enemy, enemyHealth, probOfHitting, enemyAttack, amountOfCash = enemy4()
    print("\n")
    print("Incredible! You have defeated the all of your enemies and made it to the island. Exhausted, you approach the gate that leads into the village on the island.")
    print("A guard stands there and asks for the entry fee of $200.")
    print("You hand him all of the money you have.")
    print("A few minutes go by....")
    if playerCash >= 200:
        print("The guard says you have enough money and allows you to enter the village. You live happily ever after!")
    else:
        print("The guard tells you that you need more money and cannot enter the village until you have $200.")
        print("You have two options. You can try and kill the guard for his keys to the gate or you can go back out into the ocean to search for more valuable items.")
        guardDecision = input("Fight (f) or Go Search (s): ")
        print("\n")
        if guardDecision == "f":
           playerHealth, playerCash = battles(playerHealth, playerCash, attack, accuracy, enemy, enemyHealth, enemyAttack, probOfHitting, amountOfCash) 
        else:
            print("You search for hours and hours before you finally give up and head back to shore.")
            guardDecision = input("The guard asks if you have any more money, and you reply yes (y)/no (n)? ")
            print("\n")
            if guardDecision == "y":
                print("The guard counts the money and shoves it back in your face saying this still isn't enough!")
                print("You've had enough and decide to fight!")
                playerHealth, playerCash = battles(playerHealth, playerCash, attack, accuracy, enemy, enemyHealth, enemyAttack, probOfHitting, amountOfCash)
            else:
                print("You tell him no and he yells at you to get out of his face and leave this island at once!")
                print("You've had enough and decide to fight!")
                playerHealth, playerCash = battles(playerHealth, playerCash, attack, accuracy, enemy, enemyHealth, enemyAttack, probOfHitting, amountOfCash)
                
    return playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy

def chapter5(playerHealth, playerEndurance, playerCash):
    print("\n")
    print("Absolutely terrific! You have made it across the ocean on a raft fighting off every obstacle in your way. You are a true warrior.")
    print("Here are your final statistics:\nHealth = {0}\nEndurance = {1}\nCash = {2}".format(playerHealth, playerEndurance, playerCash))

def youLost():
    print("You Lose!")

def main():
    playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy = chapter1()
    if playerHealth > 0 and playerEndurance > 0:
        playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy = chapter2(playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy)
        if playerHealth > 0 and playerEndurance > 0:
            playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy = chapter3(playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy)
            if playerHealth > 0 and playerEndurance > 0:    
                playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy = chapter4(playerName, playerHealth, playerEndurance, playerCash, attack, probOfRun, accuracy)
                if playerHealth > 0 and playerEndurance > 0:
                    chapter5(playerHealth, playerEndurance, playerCash)
    else:
        youLost()

main()