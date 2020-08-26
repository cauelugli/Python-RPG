from board import *


def pickwarrior():
    print("\nYou chose the Warrior Class!")
    board.player["CLASS"] = "Warrior"
    board.player["STR"] += 15
    board.player["DICEMIN"] += 1
    board.player["DICEMAX"] += 3
    board.player["ARMOR"] += 4
    board.player["HP"] += 130
    board.player["MAXHP"] += 130
    board.player["MANA"] += 20
    board.player["MAXMANA"] += 20
    board.player["SKILL1"] = "Bash"
    board.player["SKILL2"] = "Double Strike"
    board.player["SKILLBOOK"].append("1) Bash : 5 Mana")
    board.player["SKILLBOOK"].append("2) Double Strike : 10 Mana")
    print("STR: 15 | HIT: 1-3 | ARMOR: 4 | HP: 130 | MANA: 20")
    print("SKILLS:", board.player["SKILLBOOK"])


def pickarcher():
    print("\nYou chose the Archer Class!")
    board.player["CLASS"] = "Archer"
    board.player["STR"] += 13
    board.player["DICEMIN"] += 6
    board.player["DICEMAX"] += 11
    board.player["ARMOR"] += 3
    board.player["HP"] += 100
    board.player["MAXHP"] += 100
    board.player["MANA"] += 30
    board.player["MAXMANA"] += 30
    board.player["SKILL1"] = "Sharpshoot"
    board.player["SKILL2"] = "Critical Hit"
    board.player["SKILLBOOK"].append("1) Sharpshoot : 7 Mana")
    board.player["SKILLBOOK"].append("2) Critical Hit : 15 Mana")
    print("STR: 13 | HIT: 6-11 | ARMOR: 3 | HP: 100 | MANA: 30")
    print("SKILLS:", board.player["SKILLBOOK"])


def pickmage():
    print("\nYou chose the Mage Class!")
    board.player["CLASS"] = "Mage"
    board.player["STR"] += 9
    board.player["DICEMIN"] += 1
    board.player["DICEMAX"] += 2
    board.player["ARMOR"] += 2
    board.player["HP"] += 90
    board.player["MAXHP"] += 90
    board.player["MANA"] += 100
    board.player["MAXMANA"] += 100
    board.player["SKILL1"] = "Fireball"
    board.player["SKILL2"] = "Lightning Strike"
    board.player["SKILLBOOK"].append("1) Fireball : 15 Mana")
    board.player["SKILLBOOK"].append("2) Lightning Strike: 25 Mana")
    print("STR: 9 | HIT: 1-2 | ARMOR: 2 | HP: 90 | MANA: 100")
    print("SKILLS:", board.player["SKILLBOOK"])
