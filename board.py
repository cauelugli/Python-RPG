from random import randint
import board
import funcs
import enemies
import map1
import map2
import map3
import map4

board.player = {
    "NAME": "",
    "CLASS": "",
    "STR": 0,
    "ARMOR": 0,
    "HP": 0,
    "MAXHP": 0,
    "LEVEL": 1,
    "SKILL1": "",
    "SKILL2": "",
    "SKILL3": "",
    "SKILL4": "",
    "MANA": 0,
    "MAXMANA": 0,
    "SKILLBOOK": [],
    "DICEMIN": 0,
    "DICEMAX": 0,
    "WEAPON": "",
    "WEAPONDMG": 0,
    "SHIELD": "",
    "SHIELDARMOR": 0,
    "CHEST": "",
    "AMULET": "",
    "INVENTORY": [],
    "INVENTORYCAP": 5,
    "POUCH": [],
    "EXP": 0,
    "GOLD": 0,
    "BEHAVIOR": 0,
    "KNOWNMAPS": [],
    "RIVAL": ""
}
board.enemy = {
    "NAME": "",
    "STR": 0,
    "ARMOR": 0,
    "HP": 0}

# beginning of the program
map1.map1start()
map2.map2start()
map3.map3start()
map4.map4start()


# test fight
# board.player["HP"] += 120
# board.player["ARMOR"] += 4
# board.player["MANA"] += 30
# board.player["CLASS"] = "Warrior"
# enemies.enemycharmap1_3()
