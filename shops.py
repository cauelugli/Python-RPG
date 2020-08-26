from board import *
import map4


def shopmap4():
    inshop = True
    while inshop:
        print("\nDo you want to buy or sell?\n1)Buy   2)Sell   0)Exit")
        decide = input("\n>>: ")
        if decide == "0":
            print("\nYou quit shopping")
            break
        if decide == "1":
            buymap4()
            break
        if decide == "2":
            sellmap4()
            break


def buymap4():
    print('''
          ** Derivian Tavern Shop **

 ID
 1)  Water      +15["HP"]                  10$
 2)  Beer       +15["MANA"]                20$
 3)  Meat       +30["HP"] | +15["MANA"]    40$

 4)  Longsword     +6["STR"] | Hit 1-6     120$ 
 5)  Special Item  +5["STR"] | +5["ARMOR"] | +15["MANA"]   1 Rolled Joint

Press 0 to Exit''')
    inbuying = True
    while inbuying:
        buying = input("\nChoose your option\n>>: ")
        buyingoptions = ["0", "1", "2", "3", "4", "5"]
        while buying not in buyingoptions:
            buying = input("\nInvalid entry, check the item ID\n>>: ")
        if buying == "0":
            print("\nYou stopped buying")
            break
        if buying == "1":
            if board.player["GOLD"] < 10:
                print("\nYou don't have enougth GOLD!")
                pass
            if board.player["GOLD"] >= 10:
                board.player["GOLD"] -= 10
                board.player["POUCH"].append("Water")
                print("\n1 Water bought for 10$!")
        if buying == "2":
            if board.player["GOLD"] < 15:
                print("\nYou don't have enougth GOLD!")
                pass
            if board.player["GOLD"] >= 15:
                board.player["GOLD"] -= 15
                board.player["POUCH"].append("Beer")
                print("\n1 Beer bought for 10$!")
        if buying == "3":
            if board.player["GOLD"] < 30:
                print("\nYou don't have enougth GOLD!")
                pass
            if board.player["GOLD"] >= 30:
                board.player["GOLD"] -= 30
                board.player["POUCH"].append("Meat")
                print("\n1 Meat bought for 10$!")
        if buying == "4":
            if board.player["GOLD"] < 120:
                print("\nYou don't have enougth GOLD!")
                pass
            if board.player["GOLD"] >= 120:
                board.player["GOLD"] -= 120
                board.player["INVENTORY"].append("Longsword")
                print("\nLongsword bought for 10$!")
                funcs.equip()
        if buying == "5" and "Rolled Joint" not in board.player["POUCH"]:
            print('''
Waitress:
"I can give you the Special Item, if you bring me a Rolled Joint...
I need to smoke, I'm pissed off today..."''')
        if buying == "5" and "Rolled Joint" in board.player["POUCH"]:
            board.player["POUCH"].remove("Rolled Joint")
            board.player["POUCH"].append("Special Item")
            print('''
Waitress:
"That's what I'm talking about boy!"

You exchanged Rolled Joint for Special Item!''')
            funcs.equip()


def sellmap4():
    selling = True
    while selling:
        print("Press 0 to exit Selling\nPress any key to Sell")
        x = input(">>: ")
        if x == "0":
            break
        else:
            if board.player["INVENTORY"] == "" and board.player["POUCH"] == "":
                print("\nYou have nothing to sell")
            if board.player["INVENTORY"] != "" or board.player["POUCH"] != "":
                print("\nThese are your items available for selling")
                playerinvpouch = board.player["INVENTORY"] + board.player["POUCH"]
                for i in playerinvpouch:
                    print(i)
                print("**ITENS IDs**")
                print("Sword: 1 | Leather Armor: 2 | Amulet: 3 | Special Item: 4 | Longsword: 5"
                      "Water: 6 | Beer: 7 | Meat: 8 | Rolled Joint: 9 | Bad Guys' Emblem: Not Buying")
                choicelist = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                choice = input("\n>>: ")
                while choice not in choicelist:
                    print("\nInvalid entry. Check the Item ID")
                    choice = input("\n>>: ")
                if choice == "1" and "Sword" in board.player["INVENTORY"]:
                    print("\nDo you want to sell your Sword for 30$?\n1)Yes  2)No")
                    decide = input("\n>>: ")
                    if decide == "1":
                        board.player["INVENTORY"].remove("Sword")
                        board.player["GOLD"] += 30
                        print("Sword sold for 30$!")
                    if decide == "2":
                        pass
                if choice == "2" and "Leather Armor" in board.player["INVENTORY"]:
                    print("\nDo you want to sell your Leather Armor for 25$?\n1)Yes  2)No")
                    decide = input("\n>>: ")
                    if decide == "1":
                        board.player["INVENTORY"].remove("Leather Armor")
                        board.player["GOLD"] += 25
                        print("Leather Armor sold for 25$!")
                    if decide == "2":
                        pass
                if choice == "3" and "Amulet" in board.player["INVENTORY"]:
                    print("\nDo you want to sell your Amulet for 35$?\n1)Yes  2)No")
                    decide = input("\n>>: ")
                    if decide == "1":
                        board.player["INVENTORY"].remove("Amulet")
                        board.player["GOLD"] += 35
                        print("Amulet sold for 35$!")
                    if decide == "2":
                        pass
                if choice == "4" and "Special Item" in board.player["INVENTORY"]:
                    print("\nDo you want to sell your Special Item for 50$?\n1)Yes  2)No")
                    decide = input("\n>>: ")
                    if decide == "1":
                        board.player["INVENTORY"].remove("Special Item")
                        board.player["GOLD"] += 50
                        print("Special Item sold for 50$!")
                    if decide == "2":
                        pass
                if choice == "5" and "Longsword" in board.player["INVENTORY"]:
                    print("\nDo you want to sell your Longsword for 60$?\n1)Yes  2)No")
                    decide = input("\n>>: ")
                    if decide == "1":
                        board.player["INVENTORY"].remove("Longsword")
                        board.player["GOLD"] += 60
                        print("Longsword sold for 40$!")
                    if decide == "2":
                        pass
                if choice == "6" and "Water" in board.player["POUCH"]:
                    print("\nDo you want to sell your Water for 5$?\n1)Yes  2)No")
                    decide = input("\n>>: ")
                    if decide == "1":
                        board.player["POUCH"].remove("Water")
                        board.player["GOLD"] += 5
                        print("Water sold for 5$!")
                    if decide == "2":
                        pass
                if choice == "7" and "Beer" in board.player["POUCH"]:
                    print("\nDo you want to sell your Beer for 10$?\n1)Yes  2)No")
                    decide = input("\n>>: ")
                    if decide == "1":
                        board.player["POUCH"].remove("Beer")
                        board.player["GOLD"] += 10
                        print("Beer sold for 10$!")
                    if decide == "2":
                        pass
                if choice == "8" and "Meat" in board.player["POUCH"]:
                    print("\nDo you want to sell your Meat for 15$?\n1)Yes  2)No")
                    decide = input("\n>>: ")
                    if decide == "1":
                        board.player["POUCH"].remove("Meat")
                        board.player["GOLD"] += 15
                        print("Meat sold for 15$!")
                    if decide == "2":
                        pass
                if choice == "9" and "Rolled Joint" in board.player["POUCH"]:
                    print("\nDo you want to sell your Rolled Joint for 100$?\n1)Yes  2)No")
                    decide = input("\n>>: ")
                    if decide == "1":
                        board.player["POUCH"].remove("Rolled Joint")
                        board.player["GOLD"] += 100
                        print("Rolled Joint sold for 100$!")
                    if decide == "2":
                        pass
