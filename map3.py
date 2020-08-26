from board import *
import enemies
import map2

guruhint = '''
Guru:
"Sure, good man. Have a seat, I'll tell you something:

There are some People in this game that will "SCORE" your BEHAVIOR.

And what does that mean?

It means that, depending on how you interact with people 
(KINDLY or HARSHLY) on your journey, you will get different reactions. 

Not everybody will score you a point, and you'll never know it when you get one.

Later on, this REPUTATION will be CRUCIAL in certain situations!

Anyway, just live the way you are, never pretend you're someone else.
This is your fate to Eternity.
Strength, my brother!"'''


def map3end():
    inmapend = True
    while inmapend:
        print("""
You are at the End of the Forest
You see the entrance of a City

1) Go to the City
2) Go Back South the Forest
3) Walk around the Forest""")
        walkingend = input(">>: ")
        if walkingend == "1":
            enemies.enemycharmap1_4()
            break
        if walkingend == "2":
            enemies.enemycharmap1_4()
            map3middle()
        if walkingend == "3":
            enemies.enemycharmap1_4()


def map3middle():
    inmapmiddle = True
    while inmapmiddle:
        print("""
You are in the Middle of the Forest
You see a trail heading North, and the trail back South
You see a very old man, looks like a Guru
He's meditating deeply

1) Go North the Forest
2) Go Back South
3) Talk to the Guru
4) Walk around the Forest""")
        walkingmiddle = input(">>: ")
        if walkingmiddle == "1":
            print("\nYou walked North the Forest")
            enemies.enemycharmap1_4()
            map3end()
            break
        if walkingmiddle == "2":
            map3start()
            break
        if walkingmiddle == "3":
            print('''\nGuru:\n"What's the reason you speak to me?"''')
            gurutalk = input('''
1)"Say something useful!"   2)"Could you please help me, somehow?"
>>: ''')
            if gurutalk == "1":
                board.player["BEHAVIOR"] -= 1
                print('''\nGuru:\n"Is this the best you can be? You still have a lot to learn..."''')
            if gurutalk == "2":
                print(guruhint)
        if walkingmiddle == "4":
            enemies.enemycharmap1_4()


def map3start():
    inmapstart = True
    while inmapstart:
        print("""
You are at the Beginning of the Forest
You see a trail heading North
You see the Small Town far away

1) Go North the Forest
2) Go Back to Town
3) Walk around the Forest""")
        walkingstart = input(">>: ")
        if walkingstart == "1":
            enemies.enemycharmap1_4()
            map3middle()
            break
        if walkingstart == "2":
            map2.map2start()
        if walkingstart == "3":
            enemies.enemycharmap1_4()

