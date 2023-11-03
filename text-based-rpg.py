import os, random, time
Sword = 3
Staff = 1
Stave = 2

print("""
a. Start Game
b. Options
c. Quit""")
while True:
    try:
        option = None
        optionSet = None
        option = input("""Option Select: 
                       RPG Alpha 0.1a

                       a. Start Game
                       b. Settings
                       c. Exit""")
        if (option.lower == "a"):
            print("The Game will start.")
            time.sleep(5)
            os.system("cls")
            game_session()
        elif (option.lower == "b"):
            optionLoop = True
            TamperedWithSettings = True
            while (optionLoop == True):
                print("""
                    a. Set Difficulty (1-3)
                    b. Set Equipment (Sword, Staff, Stave)
                    c. Quit Back to Main Menu""")
                optionSet = input("Option Select: ")
                if (optionSet.lower == "a"):
                    optionDifficulty = input("Enter 1-3 number to set Difficulty: ")
                    print("Difficulty Set to ", optionDifficulty)
                    optionLoop = False
                elif (optionSet.lower == "b"):
                    while (optionLoop)
                    optionWeapon = input("Select Starter Weapon (a. Sword \nb. Staff \nc. Stave)")
                    if (optionWeapon.lower == "a"):
                        print("Now will start with the weapon Sword.")
                        optionWeaponFinal = Sword
                    elif (optionWeapon.lower == "b"):
                        print("Now will Start with the weapon Staff.")
                        optionWeaponFinal = Staff
                    elif (optionWeapon.lower == "c"):
                        print("Now will Start with the weapon Stave.")
                        optionWeaponFinal = Stave
                    else:
                        print("Invalid Weapon choice. Try Again")
                elif (optionSet.lower == "c"):
                    optionLoop = False
        elif (option.lower == "c"):
            print("Quitting Program... \nThanks for playing.")
            time.sleep(5)
            break
        else:
            print("Invalid option try again.")
    except:
        for i in range(5):
            print("Exception Error")
        
def game_session():
    character = []
    enemies = []
    playerEquipment = [optionWeapon]
    #All the Game Code Goes here