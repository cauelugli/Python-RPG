from board import *


def sword():
    while board.player["WEAPON"] != "":
        print("\nYou have", board.player["WEAPON"], "currently equipped, do you want to change or keep?")
        print("1) Change   2) Keep")
        decide = input("\n>>: ")
        if decide == "1":
            board.player["WEAPONDMG"] += 5
            board.player["DICEMIN"] += 1
            board.player["DICEMAX"] += 3
            board.player["INVENTORY"].remove("Sword")
            board.player["WEAPON"] = "Sword -   ID: 1"
            print('\nYou equipped a Sword!\n"Sword": +5["STR"] | Hit 1-3')
        if decide == "2":
            pass
    if board.player["WEAPON"] == "":
        board.player["WEAPONDMG"] += 5
        board.player["DICEMIN"] += 1
        board.player["DICEMAX"] += 3
        board.player["INVENTORY"].remove("Sword")
        board.player["WEAPON"] = "Sword -   ID: 1"
        print('\nYou equipped a Sword!\n"Sword": +5["STR"] | Hit 1-3')


def leatherarmor():
    while board.player["CHEST"] != "":
        print("\nYou have", board.player["CHEST"], "currently equipped, do you want to change or keep?")
        print("1) Change   2) Keep")
        decide = input("\n>>: ")
        if decide == "1":
            board.player["ARMOR"] += 3
            board.player["INVENTORY"].remove("Leather Armor")
            board.player["CHEST"] = "Leather Armor -   ID: 2"
            print('\nYou equipped a Leather Armor!\n"Leather Armor": +3["ARMOR"]')
        if decide == "2":
            pass
    if board.player["CHEST"] == "":
        board.player["ARMOR"] += 5
        board.player["INVENTORY"].remove("Leather Armor")
        board.player["CHEST"] = "Leather Armor -   ID: 2"
        print('\nYou equipped a Leather Armor!\n"Leather Armor": +3["ARMOR"]')


def amulet():
    while board.player["AMULET"] != "":
        print("\nYou have", board.player["AMULET"], "currently equipped, do you want to change or keep?")
        print("1) Change   2) Keep")
        decide = input("\n>>: ")
        if decide == "1":
            board.player["STR"] += 3
            board.player["ARMOR"] += 2
            board.player["MAXMANA"] += 10
            board.player["INVENTORY"].remove("Amulet")
            board.player["WEAPON"] = "Amulet -   ID: 3"
            print('\nYou equipped an Amulet!\n"Amulet": +3["STR"] | +2["ARMOR"] | +10["MAXMANA"]')
        if decide == "2":
            pass
    if board.player["AMULET"] == "":
        board.player["STR"] += 3
        board.player["ARMOR"] += 2
        board.player["MAXMANA"] += 10
        board.player["INVENTORY"].remove("Amulet")
        board.player["WEAPON"] = "Amulet -   ID: 3"
        print('\nYou equipped an Amulet!\n"Amulet": +3["STR"] | +2["ARMOR"] | +10["MAXMANA"]')


def specialitem():
    while board.player["AMULET"] != "":
        print("\nYou have", board.player["AMULET"], "currently equipped, do you want to change or keep?")
        print("1) Change   2) Keep")
        decide = input("\n>>: ")
        if decide == "1":
            board.player["STR"] += 5
            board.player["ARMOR"] += 3
            board.player["MAXMANA"] += 15
            board.player["INVENTORY"].remove("Special Item")
            board.player["AMULET"] = "Special Item -   ID: 4"
            print('\nYou equipped a Special Item!\n"Special Item": +5["STR"] | +5["ARMOR"] | +15["MANA"]')
        if decide == "2":
            pass
    if board.player["AMULET"] == "":
        board.player["STR"] += 5
        board.player["ARMOR"] += 3
        board.player["MAXMANA"] += 15
        board.player["INVENTORY"].remove("Special Item")
        board.player["AMULET"] = "Special Item -   ID: 4"
        print('\nYou equipped a Special Item!\n"Special Item": +5["STR"] | +5["ARMOR"] | +15["MANA"]')


def longsword():
    while board.player["WEAPON"] != "":
        print("\nYou have", board.player["WEAPON"], "currently equipped, do you want to change or keep?")
        print("1) Change   2) Keep")
        decide = input("\n>>: ")
        if decide == "1":
            board.player["WEAPONDMG"] += 6
            board.player["DICEMIN"] += 1
            board.player["DICEMAX"] += 6
            board.player["INVENTORY"].remove("Longsword")
            board.player["WEAPON"] = "Longsword - ID:5"
            print('\nYou equipped a Longsword!\n"Longsword": +6["STR"] | Hit 1-6')
        if decide == "2":
            pass
    if board.player["WEAPON"] == "":
        board.player["WEAPONDMG"] += 6
        board.player["DICEMIN"] += 1
        board.player["DICEMAX"] += 6
        board.player["INVENTORY"].remove("Longsword")
        board.player["WEAPON"] = "Longsword - ID:5"
        print('\nYou equipped a Longsword!\n"Longsword": +6["STR"] | Hit 1-6')