from board import *
import funcs


def enemycharmap1_4():
    x = randint(0, 10)
    if x == 0 or x == 1 or x == 2:
        enemyorc()
        print("\nYou see an", board.enemy["NAME"])
        print("ENEMY:", board.enemy)
        funcs.fight()
    if x == 3 or x == 4 or x == 5:
        enemyzombie()
        print("\nYou see an", board.enemy["NAME"])
        print("ENEMY:", board.enemy)
        funcs.fight()
    else:
        print("\nYou walked, and didn't find enemies.")


def enemyhit():
    enemydamage = board.enemy["STR"] + randint(0, 4)
    return enemydamage


def enemyfight():
    enemyhit()
    enemydamage = enemyhit()
    playertakendamage = (enemydamage - (board.player["ARMOR"] + board.player["SHIELDARMOR"]))
    board.player["HP"] -= playertakendamage
    print("The enemy hits you", playertakendamage, "damage, and you have", board.player["HP"], "HP left.")


def enemyorc():
    board.enemy["NAME"] = "Orc"
    board.enemy["STR"] += 15
    board.enemy["ARMOR"] += 3
    board.enemy["HP"] += 70


def enemyzombie():
    board.enemy["NAME"] = "Zombie"
    board.enemy["STR"] += 12
    board.enemy["ARMOR"] += 5
    board.enemy["HP"] += 85

