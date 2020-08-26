from board import *
import enemies
import map3
import shops
import time

knownmap = {"KNOWNMAP": 0}
man = {"MAN": 0}
woman = {"WOMAN": 0}
showman = {"SHOWMAN": 0}
tavern = {"TAVERN": 0}
tavernman = {"TAVERNMAN": 0}


# North North of the City
def map4end():
    inmapend = True
    while inmapend:
        print('''
You are at the Border of the city

You see a ''')
        walkingend = input(">>: ")
        if walkingend == "1":
            print("a")


# Tavern, East of the City - done
def map4east():
    inmapeast = True
    while inmapeast:
        if tavern["TAVERN"] == 0:
            print("""
You entered Severius Tavern in Derivian!
The decoration is terrible
There are some Bad Guys in a table
The Waitress is looking at you
You see a Man by himself starring at the window

1) Talk to the Bad Guys
2) Speak with the Waitress
3) Bother the lonely Man""")
            tavernoption = input(">>: ")
            if tavernoption == "1":
                print("\nYou come close to the table. The guys stop talking, and look at you")
                badguystalk = input('1)"Ugly face for me is hunger!"   2)"Excuse me guys, can you help me?"\n>>: ')
                if badguystalk == "1":
                    print("\nAll the crew get astonished. One guy says:")
                    print('''Slim Guy:\n"YEAH DUDE! I'M HUNGRY!!"''')
                    badguystalk2 = input('1)"Of course you are! Slim as fuck..."   2)"Sure bro, on me!"\n>>: ')
                    if badguystalk2 == "1":
                        tavern["TAVERN"] += 1
                        print('''
The guys laugh and start bullying the poor slim boy...

Looks like the Boss:
"Whoa man! What you thinking? Think we FUN?? I'ma kill you!!"''')
                        time.sleep(2)
                        funcs.deriviantavernboss()
                        print("\nAfter beating the bad ass, you notice the tavern is destroyed")
                        time.sleep(1)
                    if badguystalk2 == "2":
                        tavern["TAVERN"] += 1
                        print('''Looks like the Boss:\n"Whoa man! What you thinking? Think we POOR?? I'ma kill you!!"''')
                        time.sleep(2)
                        funcs.deriviantavernboss()
                        print("\nAfter beating the bad ass, you see tavern completely destroyed")
                        time.sleep(1)
                if badguystalk == "2":
                    tavern["TAVERN"] += 1
                    print('''Looks like the Boss:\n"Whoa man! What you thinking? Think we GOOD?? I'ma kill you!!"''')
                    time.sleep(2)
                    funcs.deriviantavernboss()
                    print("\nAfter beating the bad ass, you notice the tavern is destroyed")
                    time.sleep(1)
            if tavernoption == "2":
                print('''
You see a strange looking waitress, and her boss is behind her

Waitress:
"So, what's gonna be?"

1)"What crap do you sell here?"   2)"I'd like to place an order"''')
                waitressoption = input("\n>>: ")
                if waitressoption == "1":
                    print('''Waitress:\n"Hmm... "''')
                    time.sleep(1)
                    shops.shopmap4()
                if waitressoption == "2":
                    print('''Waitress:\n"Finally someone polite!"''')
                    time.sleep(1)
                    shops.shopmap4()
            if tavernoption == "3":
                print('\nYou come close to the man\n1)"Hey you!"  2)"Sorry for bothering..."\n')
                mantalk = input(">>: ")
                if mantalk == "1":
                    print('Man:\n"Ahh, leave me alone please..."')
                if mantalk == "2" and tavernman["TAVERNMAN"] == 0:
                    print('Man:\n"No problem, please, have a seat, tell me your name"')
                    nameanswer = board.player["NAME"]
                    namecheck = input(">>: ")
                    if namecheck == nameanswer:
                        board.player["BEHAVIOR"] += 1
                        tavernman["TAVERNMAN"] += 1
                        print('Man:\n"You really look like you said the truth! Take this"')
                        board.player["POUCH"].append("Beer")
                        time.sleep(1)
                        print("You goot a Beer from the man!")
                        time.sleep(1)
                        print("[POUCH]:", board.player["POUCH"])
                    if namecheck != nameanswer:
                        board.player["BEHAVIOR"] -= 1
                        tavernman["TAVERNMAN"] -= 1
                        print('Man:\n"Nanana! Something tells me this is not your name!"')
                if mantalk == "2" and tavernman["TAVERNMAN"] == -1:
                    print('''Man:\n"You're a liar! Your presence bothers me!"''')
                if mantalk == "2" and tavernman["TAVERNMAN"] == 1:
                    print('Man:\n"Hey,"', board.player["NAME"], '! How has life treating you?"')
        if tavern["TAVERN"] == 1:
            tavern["TAVERN"] += 1
            time.sleep(1)
            print('''
The bar is completely broken... The Owner of the bar comes and says:

Tavern Owner:
"You see this mess? Yes... Maybe it's because..... 
SOME STUPID PEOPLE HAD A FIGHT IN HERE!! You know..."

And kicks you out from the place...''')
            time.sleep(2)
        if tavern["TAVERN"] == 2:
            print('''
The Tavern's door is closed
You see the Waitress near the entrance

Waitress:
"Bastard!! Lucky me that got some stuff before that rude kick me off"

1)"Got some stuff?" 2)"Hmm, whatever..."''')
            choice = input("\n>>: ")
            if choice == "1":
                shops.shopmap4()
                break
            if choice == "2":
                break


# Rival Path, West of the City - done
def map4west():
    inmapwest = True
    while inmapwest:
        print('''
You are West the City

The clear path goes on West
You see Derivian City East
There's a Small Grass as you look South

1) Continue walking West
2) Go back to Derivian City
3) Examine the Small Grass''')
        walkingwest = input(">>: ")
        if walkingwest == "1" and board.player["RIVAL"] == "":
            print('''
You see a man coming at you

Man:
"Hey you! I don't know why, but I'd like to become your rival! Say my name!"

1)"I don't give a shit about your name"   2)"Ok, you are..."''')
            rivaltalk = input("\n>>: ")
            if rivaltalk == "1":
                board.player["BEHAVIOR"] -= 1
                rivalnames = ["Bradley", "Tommy", "John", "Joe", "Globinicius", "Copernicus", "Potattor"]
                board.player["RIVAL"] = rivalnames[randint(0, 6)]
                print(board.player["RIVAL"], ':\n"Fuck you, I am', board.player["RIVAL"], 'the Great! '
                                                                                          'And I will break you!')
                time.sleep(1)
                funcs.derivianrival()
            while rivaltalk == "2":
                rivalname = input("Type your Rival's name\n>>: ")
                print("Is", rivalname, "your Rival's name?\n1)Yes  2)No")
                check = input(">>: ")
                while check != "1" or check != "2":
                    print("Invalid entry. Type 1 or 2")
                    check = input(">>: ")
                if check == "1":
                    board.player["RIVAL"] = rivalname
                    print(board.player["RIVAL"], ''':\n"Allright! Now that I have a name, let's fight!"''')
                    time.sleep(1)
                    funcs.derivianrival()
                    break
                if check == "2":
                    pass
        if walkingwest == "1" and board.player["RIVAL"] != "":
            print("\n")
        if walkingwest == "2":
            map4start()
            break
        if walkingwest == "3":
            enemies.enemycharmap1_4()


# Showman map, North of the City
def map4north():
    inmapnorth = True
    while inmapnorth:
        print("mapmenunorth")
        walkingnorth = input(">>: ")
        if walkingnorth == "1":
            print("showman")
        if walkingnorth == "2":
            print("giovani sanctuary")
        if walkingnorth == "3":
            print("Go back south")


# South of the City - done
def map4start():
    inmapstart = True
    while inmapstart:
        if knownmap["KNOWNMAP"] == 0:
            print("""
You are in a City, but you don't know the name
You see a wooden map in front of you
and two houses

1) Read the map
2) Talk to the Nearest person""")
            walkingstart = input(">>: ")
            if walkingstart == "1":
                print("\nYou read the map and discovered the city of Derivian!")
                time.sleep(1)
                board.player["KNOWNMAPS"].append("Derivian")
                knownmap["KNOWNMAP"] += 1
                break
            if walkingstart == "2":
                print("""
You look West, and see a man working on his yard
You look East, and see a woman outside her house

1) Talk to the Man
2) Talk to the Woman""")
                choosetalk = input("\n>>:")
                if choosetalk == "1" and man["MAN"] == 0:
                    print('\nMan:\n"Hello there! How may I help you?"')
                    talkman = input('\n1)"If I kill you, do I get XP?"   2)"What is the name of this city?"')
                    if talkman == "1":
                        man["MAN"] -= 1
                        board.player["BEHAVIOR"] -= 1
                        print('''\nMan:\n"Well, I don't know what "XP" means but, this is the city of Derivian"''')
                        time.sleep(1)
                        print("\nYou discovered the city of Derivian!")
                        board.player["KNOWNMAPS"].append("Derivian")
                        knownmap["KNOWNMAP"] += 1
                    if talkman == "2":
                        man["MAN"] += 1
                        board.player["BEHAVIOR"] += 1
                        print('''\nMan:\n"This is the city of Derivian! Nice name, isn't it?"''')
                        time.sleep(1)
                        print("\nYou discovered the city of Derivian!")
                        board.player["KNOWNMAPS"].append("Derivian")
                        knownmap["KNOWNMAP"] += 1
                if choosetalk == "1" and man["MAN"] != 0:
                    if man["MAN"] == -1:
                        print('''\nMan:\n"You here to kill me, again? "LiTtlE xP hUnTeR" you..."''')
                    if man["MAN"] == 1:
                        print('''\nMan:\n"We have so many nice things here! Like the Rolling Showman!"''')
                if choosetalk == "2" and woman["WOMAN"] == 0:
                    print('''\nWoman:\n"What's on your mind?"''')
                    talkwoman = input('\n1)"Better not even tell you..."   2)"I would like to know this city"')
                    if talkwoman == "1":
                        woman["WOMAN"] -= 1
                        board.player["BEHAVIOR"] -= 1
                        print('''\nWoman:\n"Don't take me for a fool!"''')
                    if talkwoman == "2":
                        woman["WOMAN"] += 1
                        print('''\nMan:\n"Why don't you just walk around?"''')
                if choosetalk == "2" and woman["WOMAN"] != 0:
                    if woman["WOMAN"] == -1:
                        print('''\nMan:\n"Can't you see I'm busy here? Why don't you talk to that man?"''')
                    if woman["WOMAN"] == 1:
                        print('''\nMan:\n"Maybe that gentleman could help you. I've got things to do"''')
        if knownmap["KNOWNMAP"] == 1:
            print("""
You are in  Derivian City

You see a way North, with some people gathered 
There is a tavern East with a banner "Severus"
You see South the Grass Route to the Forest
You see a trail West

1) Walk North the City
2) Go East to the Tavern
3) Walk South to the Forest
4) Go West to the Trail""")
            walkingstart2 = input(">>: ")
            if walkingstart2 == "1":
                map4north()
                break
            if walkingstart2 == "2":
                map4east()
                break
            if walkingstart2 == "3":
                map3.map3end()
                break
            if walkingstart2 == "4":
                map4west()
                break

