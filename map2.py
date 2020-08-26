from board import *
import funcs
import map1
import time

lady = {"LADY": 0}
scientist = {"SCIENTIST": 0}
professor = {"PROFESSOR": 0}


def map2start():
    inmapstart = True
    while inmapstart:
        print("""
You are in a small town.
You see a a House, a big Laboratory, a Grass Route
and your Home.

1) Go to the House
2) Go to the Laboratory
3) Go to the Grass Route
4) Go Home""")
        walking = input(">>: ")
        while walking == "1":
            print('''
You are inside a Lady's house
You see a young Lady reading a book

1) Talk to the Lady
2) Leave the House''')
            talk = input(">>: ")
            if talk == "1" and lady["LADY"] == 0:
                print('''
Young Lady:
"Hey! I'm learning a lot with this book! Do you want to read it?"
1)"No!"  2)"It would be great, if you don't mind"''')
                read = input(">>: ")
                if read == "1":
                    lady["LADY"] -= 1
                    board.player["BEHAVIOR"] -= 1
                    print('\nYoung Lady:\n"Okay then... You harsh!"')
                    print("You got -1 BEHAVIOR point!")
                    continue
                if read == "2":
                    lady["LADY"] += 1
                    board.player["BEHAVIOR"] += 1
                    board.player["MANA"] += 10
                    print("\n*Reading the book, you got +10 MANA!!*")
                    print('"TOTAL MANA":', board.player["MANA"])
                    print('''\nYoung Lady:\n"Ahh, you're so gentle! *-*"''')
                    print("You got +1 BEHAVIOR point!")
                    continue
            if talk == "1" and lady["LADY"] == -1:
                print('''\nYoung Lady:\n"Why don't you just go away? Get out of my house!" ''')
                break
            if talk == "1" and lady["LADY"] == 1:
                print('''\nYoung Lady:\n"Did you like the book? Come anytime you want!" ''')
            if talk == "2":
                break
        while walking == "2":
            print('''
You are inside a Laboratory
You see a Scientist next to the door
and a Professor close to a machine

1) Talk to the Scientist
2) Talk to the Professor
3) Leave the Laboratory''')
            lab = input(">>: ")
            if lab == "1":
                if scientist["SCIENTIST"] == 0:
                    print('''\nScientist:\n"Professor Veneer is my master!\n
1)"I don't care!"   2)"Oh, realy? Who's this?""''')
                    scientisttalk = input(">>: ")
                    if scientisttalk == "1":
                        if scientist["SCIENTIST"] == 0:
                            scientist["SCIENTIST"] -= 1
                            board.player["BEHAVIOR"] -= 1
                            print('''\nScientist:\n"Ahh, these "bad boys"... So DARK..." ''')
                            print("You got -1 BEHAVIOR point!")
                            continue
                    if scientisttalk == "2":
                        if scientist["SCIENTIST"] == 0:
                            scientist["SCIENTIST"] += 1
                            board.player["BEHAVIOR"] += 1
                            print('''\nScientist:\n"He's that gentleman after the machine, GOOD man..." ''')
                            print("You got +1 BEHAVIOR point!")
                            continue
                if scientist["SCIENTIST"] != 0:
                    if scientist["SCIENTIST"] == -1:
                        print('''\nScientist:\n"I DON'T CARE" ''')
                    if scientist["SCIENTIST"] == 1:
                        print('''\nScientist:\n"Have you talked to Professor Veneer?" ''')
            if lab == "2":
                if professor["PROFESSOR"] == 0:
                    print("""\nProfessor Veneer:
"Hello friend! Hello.. 'friend'?! That's slang...
What is your name?" """)
                    name = input("""\nType your name here\n>>: """)
                    print("\nIs", name, "your name, really?")
                    check = input("1) Yes   2) No\n>>: ")
                    if check == "1":
                        professor["PROFESSOR"] += 1
                        board.player["NAME"] = name
                        time.sleep(1)
                        print('\nProfessor Veneer:\n"Ahh, so you are', board.player["NAME"])
                    if check == "2":
                        print('\nProfessor Veneer:\n"You crazy, or what?"')
                        pass
                if professor["PROFESSOR"] == 1 and board.player["CLASS"] == "":
                    print('''Once named, you must choose your CLASS"''')
                    time.sleep(1)
                    funcs.playerfirstpick()
                    continue
                if professor["PROFESSOR"] == 1 and board.player["CLASS"] != "":
                    print('''\nProfessor Veneer:\n"Well, there's a lot to in the FOREST, you know..."''')
            if lab == "3":
                break
        if walking == "3":
            if board.player["CLASS"] == "":
                print("""\nCitizen:
"WHOA DUDE!! Don't do that!! Going LIKE THIS to the world?
You better choose your CLASS first...
Why don't you go to the LAB??" """)
            if board.player["CLASS"] != "":
                print("""\nCitizen:
"I see the old Veneer has taught you some tricks. Good luck out there!" """)
                break
        if walking == "4":
            map1.map1start()
