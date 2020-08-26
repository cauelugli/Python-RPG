from board import *

chest = {"ITEM": 1}
oldman = {"OLDMAN": 0}


def map1start():
    inmapstart = True
    while inmapstart:
        print("""
You are in your room
You see your bed, a chest and a staircase down
    
1) Open the chest
2) Go downstairs
3) Rest in Bed""")
        walkingstart = input(">>: ")
        if walkingstart == "1":
            if chest["ITEM"] == 1:
                print("\nYou found a Sword! ID: 1 (Use this ID to browse your equips and itens!)")
                chest["ITEM"] -= 1
                board.player["INVENTORY"].append("Sword")
                funcs.equip()
                continue
            if chest["ITEM"] == 0:
                print("\nThe chest is empty")
        if walkingstart == "2":
            inmapend = True
            while inmapend:
                print("""
You are in a living room
You see a person and a door

1) Talk to the person
2) Go throught the door
3) Go upstairs""")
                walkingend = input(">>: ")
                if walkingend == "1":
                    print('''\nOld Man:\n"It's a nice day today to slay some foes, isn't it?"''')
                    talk = input('''
1) "Oh, yeah! I'm ready to smash!"
2) "Nah! I am not that violent one..."
>>: ''')
                    if talk == "1":
                        print('''\nOld Man:\n"You're one of my kind! I Like the bad guys!" ''')
                        if oldman["OLDMAN"] == 0:
                            board.player["BEHAVIOR"] -= 1
                            board.player["STR"] += 1
                            print('You got -1 BEHAVIOR point!\nYou got +1["STR"]')
                            oldman["OLDMAN"] += 1
                    if talk == "2":
                        print('\nOld Man:\n"You better be tough, kid. No good to be good, some say..."')
                        if oldman["OLDMAN"] == 0:
                            board.player["BEHAVIOR"] += 1
                            print("You got +1 BEHAVIOR point!")
                            oldman["OLDMAN"] += 1
                if walkingend == "2":
                    inmapstart = 0
                    break
                if walkingend == "3":
                    break
        if walkingstart == "3":
            board.player["HP"] = board.player["MAXHP"]
            board.player["MANA"] = board.player["MAXMANA"]
            print("\nYou slept, recovering HP and MANA!")
            print('["HP"]:', board.player["HP"])
            print('["MANA"]:', board.player["MANA"])


