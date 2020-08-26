from board import *
import skills
import items
import enemies
import classes
import time


def playerfirstpick():
    playerpickoptions = ["1", "2", "3"]
    playerpick = input("""
    
  1) Warrior         2) Archer           3) Mage
    STR: 15           STR: 13             STR: 9
    HIT: 1-3          HIT: 6-11           HIT: 1-2
    ARMOR: 4          ARMOR: 3            ARMOR: 2       
    HP: 130           HP: 100             HP: 90
    MANA: 20          MANA: 30            MANA: 100

    ---------------------SKILLS----------------------------
    *Bash*            *Sharpshoot*        *Fireball*
    *Stun Hit*        *Critical Hit*      *Lightning Strike*

>>: """)

    while playerpick not in playerpickoptions:
        print('\nInvalid entry. Choose "1", "2" or "3"')
        playerpick = input("\n>>: ")
    if playerpick == "1":
        classes.pickwarrior()
    if playerpick == "2":
        classes.pickarcher()
    if playerpick == "3":
        classes.pickmage()


def playerfight():
    playerdamage = board.player["STR"] + board.player["WEAPONDMG"] + randint(board.player["DICEMIN"], board.player["DICEMAX"])
    enemytakendamage = (playerdamage - board.enemy["ARMOR"])
    board.enemy["HP"] -= enemytakendamage
    print("\nYou hit", enemytakendamage, "damage, and the enemy has", board.enemy["HP"], "HP left.")


def playerskilluse():
    print('\nChoose your Skill - Type 1, 2, 3 or 4\nType "0" to Return')
    print("\nSKILLBOOK:", board.player["SKILLBOOK"], '\n["MANA"] :', board.player["MANA"])
    if board.player["MANA"] <= 0:
        print("HINT: Careful!! If you cast a spell with NO MANA, the enemy WILL HIT you!!")
    skill = input("\n>>: ")
    while skill != "0" and skill != "1" and skill != "2" and skill != "3" and skill != "4":
        print('\nInvalid Entry - Type "1", "2", "3" or "4"\nType "0" to Return')
        print("\nSKILLBOOK:", board.player["SKILLBOOK"], '\n["MANA"] :', board.player["MANA"])
        skill = input("\n>>: ")
    if skill == "0":
        board.menu = "2"
    if skill == "1":
        if board.player["CLASS"] == "Warrior":
            skills.skillbash()
        if board.player["CLASS"] == "Archer":
            skills.skillsharpshoot()
        if board.player["CLASS"] == "Mage":
            skills.skillfireball()
        if board.enemy["HP"] > 0:
            time.sleep(1)
            enemies.enemyfight()
    if skill == "2":
        if board.player["CLASS"] == "Warrior":
            skills.skilldoublestrike()
        if board.player["CLASS"] == "Archer":
            skills.skillcriticalhit()
        if board.player["CLASS"] == "Mage":
            skills.skilllightningstrike()
        if board.enemy["HP"] > 0:
            time.sleep(1)
            enemies.enemyfight()


def playeritemuse():
    print("a")


def playerinfo():
    print("\nYou are in the info menu\nChoose your Info\n1)Status   2)Equip   3)Inventory   4)Enemy Info\n")
    infochoice = input(">>: ")
    if infochoice == "1":
        print('\nSTR:', board.player["STR"])
        print('ARMOR:', board.player["ARMOR"])
        print('CURRENT HP:', board.player["HP"])
        print('CURRENT MANA:', board.player["MANA"])
        print('CLASS:', board.player["CLASS"])
        print('SKILLBOOK:', board.player["SKILLBOOK"])
    if infochoice == "2":
        print('\nWEAPON:', board.player["WEAPON"])
        print('CHEST:', board.player["CHEST"])
        print('AMULET:', board.player["AMULET"])
        print('HIT:', board.player["DICEMIN"], "-", board.player["DICEMAX"])
        print('CURRENT EXP:', board.player["EXP"])
    if infochoice == "3":
        print('\nINVENTORY:', board.player["INVENTORY"])
        print('GOLD:', board.player["GOLD"])
    if infochoice == "4":
        print('\nCURRENT ENEMY')
        print('NAME:', board.enemy["NAME"])
        print('DAMAGE:', board.enemy["STR"])
        print('ARMOR:', board.enemy["ARMOR"])
        print('CURRENT HP:', board.enemy["HP"])


def fight():
    main = True
    while main:
        print("\nYou are in a fight\nChoose your option\n1)Fight  2)Skill  3)Item  4)Info  5)Run\n")
        menu = input(">>: ")
        if menu == "1":
            playerfight()
            time.sleep(1)
            if board.enemy["HP"] > 0:
                enemies.enemyfight()
        if menu == "2":
            playerskilluse()
        if menu == "3":
            playeritemuse()
        if menu == "4":
            playerinfo()
        if board.enemy["HP"] <= 0:
            print("\nYou killed the enemy!\n** END OF FIGHT **")
            exp()
            time.sleep(2)
            levelup()
            time.sleep(2)
            drop()
            time.sleep(2)
            equip()
            enemyfightreset()
            break
        if menu == "5":
            runchance = randint(0, 3)
            if runchance != 3:
                print("\nYou ran away from the Fight!\n** END OF FIGHT **")
                enemyfightreset()
                time.sleep(1)
                break
            else:
                print("\nCouldn't Escape!")
                time.sleep(1)
                enemies.enemyfight()
        if board.player["HP"] <= 0:
            print("\nYou were killed!\n** END OF FIGHT **")
            break


def drop():
    dropchance = randint(0, 15)
    if dropchance == 0 or dropchance == 1:
        board.player["INVENTORY"].append("Sword")
        print("\nLOOT:\nSword : +5 [STR] | Hit 1-3 | ID: 1")
    if dropchance == 2 or dropchance == 3 or dropchance == 4:
        board.player["INVENTORY"].append("Leather Armor")
        print("\nLOOT:\nLeather +3 [ARMOR] | ID: 2")
    if dropchance == 5:
        board.player["INVENTORY"].append("Amulet")
        print("\nLOOT:\nAmulet : +3 [STR] | +2 [ARMOR] | +10 [MANA] | ID: 3")
    if dropchance == 6:
        board.player["INVENTORY"].append("Special Item")
        print("\nLOOT:\nSpecial Item : +5 [STR] | +3 [ARMOR] | +15 [MANA] | ID: 4")


def exp():
    x = board.enemy["NAME"]
    if x == "Orc":
        board.player["EXP"] += 39 + randint(5, 15)
    if x == "Zombie":
        board.player["EXP"] += 40 + randint(5, 14)


def equip():
    inequip = True
    while inequip:
        print("\nDo you want to equip an item?   1)Yes  -)No  2)Inventory")
        equipoption = input("\n>>: ")
        if equipoption == "1" and board.player["INVENTORY"] == "":
            print("\nYour INVENTORY is empty")
        while equipoption == "1":
            print("\nSword - ID:1 | Leather Armor - ID:2 | Amulet - ID:3 | Special Item - ID:4 | Longsword - ID:5")
            print("Which item do you want to equip?  Please type ID of the item")
            print('INVENTORY:', board.player["INVENTORY"],
                  '  INV CAP:', (0 + len(board.player["INVENTORY"])), "/", board.player["INVENTORYCAP"])
            itemchoice = input("\n>>: ")
            itemoptions = ["1", "2", "3", "4", "5"]
            if itemchoice == "1":
                items.sword()
                break
            if itemchoice == "2":
                items.leatherarmor()
                break
            if itemchoice == "3":
                items.amulet()
                break
            if itemchoice == "4":
                items.specialitem()
                break
            if itemchoice == "5":
                items.longsword()
                break
            if itemchoice not in itemoptions:
                pass
        if equipoption == "2":
            print('\nINVENTORY:', board.player["INVENTORY"], '\nGOLD:', board.player["GOLD"])
            continue
        if equipoption != "1" or equipoption != "2":
            break


def levelup():
    print("\nYou got", board.player["EXP"], "EXP points!")
    if board.player["EXP"] < 100:
        pass
    if board.player["EXP"] >= 100:
        print("*You advanced to Level 2!!*")
        board.player["LEVEL"] = 2
        if board.player["CLASS"] == "Warrior":
            board.player["STR"] += 3
            board.player["ARMOR"] += 1
            board.player["MAXHP"] += 10
            board.player["MAXMANA"] += 5
            board.player["DICEMAX"] += 2
            print('\nSTR:', board.player["STR"], ' ARMOR:', board.player["ARMOR"], ' HIT:', board.player["DICEMIN"],
                  "-", board.player["DICEMAX"])
            print('MAX HP:', board.player["MAXHP"], '  MAX MANA:', board.player["MAXMANA"])
        if board.player["CLASS"] == "Archer":
            board.player["STR"] += 3
            board.player["ARMOR"] += 2
            board.player["MAXHP"] += 7
            board.player["MAXMANA"] += 7
            board.player["DICEMIN"] += 1
            board.player["DICEMAX"] += 3
            print('\nSTR:', board.player["STR"], ' ARMOR:', board.player["ARMOR"], ' HIT:', board.player["DICEMIN"],
                  "-", board.player["DICEMAX"])
            print('MAX HP:', board.player["MAXHP"], '  MAX MANA:', board.player["MAXMANA"])
        if board.player["CLASS"] == "Mage":
            board.player["STR"] += 2
            board.player["ARMOR"] += 1
            board.player["MAXHP"] += 6
            board.player["MAXMANA"] += 15
            board.player["DICEMIN"] += 1
            board.player["DICEMAX"] += 4
            print('\nSTR:', board.player["STR"], ' ARMOR:', board.player["ARMOR"], ' HIT:', board.player["DICEMIN"],
                  "-", board.player["DICEMAX"])
            print('MAX HP:', board.player["MAXHP"], '  MAX MANA:', board.player["MAXMANA"])


def enemyfightreset():
    board.enemy["NAME"] = ""
    board.enemy["STR"] = 0
    board.enemy["ARMOR"] = 0
    board.enemy["HP"] = 0


# bosses fights
def deriviantavernboss():
    board.enemy["NAME"] = "Bad Guys' Boss"
    board.enemy["STR"] += 20
    board.enemy["ARMOR"] += 12
    board.enemy["HP"] += 140
    options = "\nYou are in a fight\nChoose your option\n1)Fight  2)Skill  3)Item  4)Info  5)Run\n"
    main = True
    while main:
        print(options)
        menu = input(">>: ")
        if menu == "1":
            playerfight()
            if board.enemy["HP"] > 0:
                enemies.enemyfight()
        if menu == "2":
            playerskilluse()
        if menu == "3":
            playeritemuse()
        if menu == "4":
            playerinfo()
        if board.enemy["HP"] <= 0:
            print("\nYou killed the enemy!\n** END OF FIGHT **")
            board.player["EXP"] += 60 + randint(10, 20)
            levelup()
            board.player["POUCH"].append("Bad Guys Emblem")
            print("\nYou received the Bad Guys Emblem")
            print("\nLOOT:\nBad Guys Emblem -5 [BEHAVIOR]")
            enemyfightreset()
            break
        if menu == "5":
            print("\nNo escape from this fight!")
        if board.player["HP"] <= 0:
            print("\nYou were killed!\n** END OF FIGHT **")
            break


def derivianrival():
    print("a")
    board.enemy["NAME"] = board.player["RIVAL"]
    board.enemy["STR"] += 20
    board.enemy["ARMOR"] += 12
    board.enemy["HP"] += 140
    options = "\nYou are in a fight\nChoose your option\n1)Fight   2)Skill   3)Info   4)Run\n"
    main = True
    while main:
        print(options)
        menu = input(">>: ")
        if menu == "1":
            playerfight()
            if board.enemy["HP"] > 0:
                enemies.enemyfight()
        if menu == "2":
            playerskilluse()
        if menu == "3":
            playerinfo()
        if board.enemy["HP"] <= 0:
            print("\nYou killed the enemy!\n** END OF FIGHT **")
            board.player["EXP"] += 60 + randint(10, 20)
            levelup()
            board.player["POUCH"].append("Bad Guys Emblem")
            print("\nYou received the Bad Guys Emblem")
            print("\nLOOT:\nBad Guys Emblem -5 [BEHAVIOR]")
            enemyfightreset()
            break
        if menu == "4":
            print("\nNo escape from this fight!")
        if board.player["HP"] <= 0:
            print("\nYou were killed!\n** END OF FIGHT **")
            break