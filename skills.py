from board import *
import funcs


def skillbash():
    while board.player["MANA"] < 5:
        print("\nYou lack mana to cast a spell.")
        break
    if board.player["MANA"] >= 5:
        bashdamage = (board.player["STR"] + 4)
        board.enemy["HP"] -= bashdamage
        board.player["MANA"] -= 5
        print("\nYou BASH the enemy for", bashdamage, "damage, and the enemy has", board.enemy["HP"], "HP left.")
        return bashdamage


def skilldoublestrike():
    while board.player["MANA"] < 10:
        print("\nYou lack mana to cast a spell.")
        break
    if board.player["MANA"] >= 10:
        playerdamage = 2 * (board.player["STR"] + board.player["WEAPONDMG"] + randint(board.player["DICEMIN"],
                                                                                      board.player["DICEMAX"]))
        enemytakendamage = (playerdamage - board.enemy["ARMOR"])
        board.enemy["HP"] -= enemytakendamage
        print("\nYou hit", enemytakendamage, "damage, and the enemy has", board.enemy["HP"], "HP left.")
        print("It's a DOUBLE STRIKE!!")
        board.player["MANA"] -= 10


def skillsharpshoot():
    while board.player["MANA"] < 7:
        print("\nYou lack mana to cast a spell.")
        break
    if board.player["MANA"] >= 7:
        sharpshootdamage = (board.player["STR"] + board.player["DICEMAX"])
        board.enemy["HP"] -= sharpshootdamage
        board.player["MANA"] -= 7
        print("\nYou hit a SHARPSHOOT", sharpshootdamage, "damage, and the enemy has", board.enemy["HP"], "HP left.")
        return sharpshootdamage


def skillcriticalhit():
    while board.player["MANA"] < 15:
        print("\nYou lack mana to cast a spell.")
        break
    if board.player["MANA"] >= 15:
        criticalhitdamage = (board.player["STR"] * 2) + randint(board.player["DICEMIN"], board.player["DICEMAX"])
        board.enemy["HP"] -= criticalhitdamage
        board.player["MANA"] -= 15
        print("\nA great CRITICAL HIT for", criticalhitdamage, "damage, and the enemy has", board.enemy["HP"], "HP left.")
        return criticalhitdamage


def skillfireball():
    while board.player["MANA"] < 15:
        print("\nYou lack mana to cast a spell.")
        break
    if board.player["MANA"] >= 15:
        fireballdamage = board.player["STR"] + randint(12, 24)
        board.enemy["HP"] -= fireballdamage
        board.player["MANA"] -= 15
        print("\nA swift FIREBALL strikes", fireballdamage, "damage, and the enemy has", board.enemy["HP"], "HP left.")
        return fireballdamage


def skilllightningstrike():
    while board.player["MANA"] < 25:
        print("\nYou lack mana to cast a spell.")
        break
    if board.player["MANA"] >= 25:
        lightningstrikedamage = board.player["STR"] + randint(24, 48)
        board.enemy["HP"] -= lightningstrikedamage
        board.player["MANA"] -= 25
        print("\nA fierce LIGHTNING STRIKE for", lightningstrikedamage, "damage, and the enemy has", board.enemy["HP"], "HP left.")
        return lightningstrikedamage
