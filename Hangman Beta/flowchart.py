import LVL1
import LVL2
import LVL3
import LVL4
import LVL5

print('='*160)
print('''
      WELCOME TO OUR HANGMAN BETA/ALPHA GAME...FIRST OF ITS KIND
      THANKS FOR CHOOSING OUR GAME
      WE HOPE THAT YOU WILL BE ABLE TO COMPLETE THE GAME :)
      ''')
print('='*160)
lvl = 1
if lvl == 1:
    print("question is:", LVL1.p)
    print("HINT:", LVL1.h)
    while LVL1.c <= 5 and lvl == 1:
        x = input("guess the letter:").upper()
        if x == LVL1.x1 or x == LVL1.x2:
            for i in range(0, 4):

                if x == LVL1.q[i]:
                    LVL1.p[i] = x
                    print(LVL1.p)
                    print(x, "is included.")
                    i = 0
                    if LVL1.p == LVL1.q:
                        lvl = lvl + 1
                        print("your guess was correct and you can proceed to the next level.")
                        break
                i = i + 1
        else:
            LVL1.c = LVL1.c + 1
            print(x, "is the wrong guess.")
    if LVL1.c >= 5:
        print("You exceeded you tries.......thanks a bunch for playing and testing our simple hangaman game.........")
if lvl == 2:
    print("question is:", LVL2.p)
    print("HINT:", LVL2.h)
    while LVL2.c <= 5 and lvl == 2:
        x = input("guess the letter:").upper()
        if x == LVL2.x1 or x == LVL2.x2 or x == LVL2.x3:
            for i in range(0, 5):

                if x == LVL2.q[i]:
                    LVL2.p[i] = x
                    print(LVL2.p)
                    print(x, "is included.")
                    i = 0
                    if LVL2.p == LVL2.q:
                        lvl = lvl + 1
                        print("your guess was correct and you can proceed to the next level.")
                        break
                i = i + 1
        else:
            LVL2.c = LVL2.c + 1
            print(x, "is the wrong guess.")
    if LVL2.c >= 5:
        print("You exceded you tries.......thanks a bunch for playing and testing our simple hangaman game.........")
if lvl == 3:
    print("question is:", LVL3.p)
    print("HINT:", LVL3.h)
    while LVL3.c <= 5 and lvl == 3:
        x = input("guess the letter:").upper()
        if x == LVL3.x1 or x == LVL3.x2 or x == LVL3.x3 or x == LVL3.x4:
            for i in range(0,6):

                if x == LVL3.q[i]:
                    LVL3.p[i] = x
                    print(LVL3.p)
                    print(x, "is included.")
                    i = 0
                    if LVL3.p == LVL3.q:
                        lvl = lvl + 1
                        print("your guess was correct and you can proceed to the next level.")
                        break
                i = i + 1
        else:
            LVL3.c = LVL3.c + 1
            print(x, "is the wrong guess.")
    if LVL3.c >= 5:
        print("You exceeded you tries.......thanks a bunch for playing and testing our simple hangaman game.........")
if lvl == 4:
    print("question is:", LVL4.p)
    print("HINT:", LVL4.h)
    while LVL4.c <= 5 and lvl == 4:
        x = input("guess the letter:").upper()
        if x == LVL4.x1 or x == LVL4.x2 or x == LVL4.x3 or x == LVL4.x4 or x == LVL4.x5:
            for i in range(0,7):

                if x == LVL4.q[i]:
                    LVL4.p[i] = x
                    print(LVL4.p)
                    print(x, "is included.")
                    i = 0
                    if LVL4.p == LVL4.q:
                        lvl = lvl + 1
                        print("your guess was correct and you can proceed to the next level.")
                        break
                i = i + 1
        else:
            LVL4.c = LVL4.c + 1
            print(x, "is the wrong guess.")
    if LVL4.c >= 5:
        print("You exceeded you tries.......thanks a bunch for playing and testing our simple hangman game.........")
if lvl == 5:
    print("question is:", LVL5.p)
    print("HINT:", LVL5.h)
    while LVL5.c <= 5 and lvl == 5:
        x = input("guess the letter:").upper()
        if x == LVL5.x1 or x == LVL5.x2 or x == LVL5.x3 or x == LVL5.x4 or x == LVL5.x5 or x == LVL5.x6:
            for i in range(0, 8):

                if x == LVL5.q[i]:
                    LVL5.p[i] = x
                    print(LVL5.p)
                    print(x, "is included.")
                    i = 0
                    if LVL5.p == LVL5.q:
                        lvl = lvl + 1
                        print('''your guess was correct and hence you have cleared level 5!......
thanks a bunch for playing and testing our simple hangman game.........
congrats... if you completed the game.........
we are going to update this version and make it more interactive so stay tuned for the coming year....
at last but not the least we want to thank our computer ma'am(i.e. shanthi ma'am) for this opportunity
as we got to learn and experience new stuff....
For any feedback please contact our developers,i.e. Prathamesh and Amruth
                         ''')
                        break
                i = i + 1
        else:
            LVL5.c = LVL5.c + 1
            print(x, "is the wrong guess.")
    if LVL5.c >= 5:
        print("You exceeded you tries.......thanks a bunch for playing and testing our simple hangman game.........")
