import os, random, time
Sword = 3
Staff = 1
Stave = 2
level = []
difficultyValueCondition = False
while True:
    try:
        option = None
        optionSet = None
        option = input("""Option Select: 
                       RPG Alpha 0.1a

                       a. Start Game
                       b. Settings
                       c. Exit \nAnswer: """)
        os.system("cls")
        if (option == "a"):
            print("The Game will start.")
            time.sleep(5)
            os.system("cls")
            game_session()
        elif (option == "b"):
            optionLoop = True
            TamperedWithSettings = True
            while (optionLoop == True):
                print("""
                    a. Set Difficulty (1-3)
                    b. Set Equipment (Sword, Staff, Stave)
                    c. Quit Back to Main Menu""")
                optionSet = input("Option Select: ")
                if (optionSet == "a"):
                    while (difficultyValueCondition == False):
                        difficultyEvalCheck = False
                        while (difficultyEvalCheck == False):
                            optionDifficulty = int(input("Enter 1-3 number to set Difficulty: "))
                            if (optionDifficulty == 1):
                                count = 0
                                print("Difficulty set to Easy with 10 levels")
                                while (count != 10):
                                    print(count)
                                    level.append(count)
                                    count = count + 1
                                difficultyEvalCheck = True
                            elif (optionDifficulty == 2):
                                count = 0
                                print("Difficulty set to Medium with 20 levels")
                                while (count != 20):
                                    print(count)
                                    level.append(count)
                                    count = count + 1
                                difficultyEvalCheck = True
                            elif (optionDifficulty == 3):
                                count = 0
                                print("Difficulty set to Hard with 30 levels")
                                while (count != 30):
                                    print(count)
                                    level.append(count)
                                    count = count + 1
                                difficultyEvalCheck = True
                            else:
                                print("Invalid")
                        difficultyValueCondition = True
                    optionLoop = False
                elif (optionSet == "b"):
                    while (optionLoop == True):
                        optionWeapon = input("Select Starter Weapon (a. Sword \nb. Staff \nc. Stave)")
                        if (optionWeapon == "a"):
                            print("Now will start with the weapon Sword.")
                            optionWeaponFinal = Sword
                            optionLoop = False
                        elif (optionWeapon == "b"):
                            print("Now will Start with the weapon Staff.")
                            optionWeaponFinal = Staff
                            optionLoop = False
                        elif (optionWeapon == "c"):
                            print("Now will Start with the weapon Stave.")
                            optionWeaponFinal = Stave
                            optionLoop = False
                        else:
                            print("Invalid Weapon choice. Try Again")
                elif (optionSet == "c"):
                    optionLoop = False
        elif (option == "c"):
            print("Quitting Program... \nThanks for playing.")
            time.sleep(5)
            break
        else:
            print("Invalid option try again.")
    except:
        for i in range(5):
            print("Exception Error")
        
def game_session():
    #Temporary Placeholder
    print("Game is still a work in progress so no games yet")
    character = []
    enemies = ["Slime", "Goblin","Kobold","Dragon"]
    enemySubclass = ["Great","Greater","Poisonous","Disaster","Calamity"]
    playerEquipment = [optionWeapon]
    gameLoop = True
    rolledEnemy = random.choice(enemies)
    rolledSubclass = random.choice(enemySubclass)
    rolledEnemyBoss = rolledEnemy0 + " " + rolledSubclass
    #while (gameLoop = True):
    #    print("")
    
        
    #All the Game Code Goes here
    #This game is a WIP or a work in progress. the base game wasn't even written yet
