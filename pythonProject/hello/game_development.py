# i am infinite
# hello guys today we are going to develop a program which is a game of snake,water and gun
# when you are done with code always have a eye on it to know how you have done it
print("--------------------welcome-to-snake,water,and gun game ----------------------------------")
print("hello initializing the game...")
# you need to learn making complex as well as simple codes
s = input("sir please enter enter to enter into the game ")
import random
i = 0
r = 0
t = 0
list5 = ["snake","water","gun"]
p = random.choice(list5)
exit = False
if s=="enter":
    x = input("sir please enter (int) to go to instructions or (game) to start the game (int/game) : ")
    if x=="int":
        print("This just like stone paper scissor.\n Both the players should keep the gestures simultaneously.\n The snake drinks the water, \nthe gun shoots the snake,\n and gun has no effect on water")
    elif x=="game":
        while exit is not True:
            s = input("sir please enter the any of the besides(snake,water,gun) : ")
            if s=="snake"or "water" or "gun":
                print("sir please enter the input(snake,water,gun)")
                if s == "quit":
                    exit = True
                elif s == "snake" and p == "snake":
                    print("are kuch nahe huha")
                    i += 1
                elif s == "water" and p == "water":
                    print("are kuch nahe huha lagtha he dono dost bangaye")
                    i += 1
                elif s == "gun" and p == "gun":
                    print("are kuch nahe huha inka kuch nahe hoga")
                    i += 1
                elif s == "snake" and p == "water":
                    print("are thu tho jeet gaya")
                    t += 1
                elif s == "water" and p == "gun":
                    print("are thu tho jeet gaya congragulations man")
                    t += 1
                elif s == "gun" and p == "snake":
                    print("are thu tho jeet gaya lagtha he indono ko thum jeethhi jahoge")
                    t += 1
                elif s == "snake" and p == "gun":
                    print("firse try kar")
                    r += 1
                elif s == "water" and p == "snake":
                    print("firse tru kar")
                    r += 1
                elif s == "gun" and p == "water":
                    print("firse!!!")
                if exit == True:
                    print("!!!results!!!")
                    print("the number of times you are won is ", t)
                    print("the number of times you are lost is ", r)
                    print("the number of times you are draw with computer is ", i)
                    if t > r:
                        print("you are won")
                    elif t < r:
                        print("you need to try again to ")
                    else:
                        print("you are draw")
    else:
        print("sir please enter the correct input")
        x = input("sir please enter int to go to instructions or game to start the game (int/game) : ")
        if x == "int":
            print(
                "This just like stone paper scissor. Both the players should keep the gestures simultaneously. The snake drinks the water, the gun shoots the snake, and gun has no effect on water")
        elif x == "game":
            while exit is not True:
                s = input("sir please enter the any of the besides(snake,water,gun) : ")
                if s == "snake" or "water" or "gun":
                    print("sir please enter the input(snake,water,gun)")
                    if s == "quit":
                        exit = True
                    elif s == "snake" and p == "snake":
                        print("are kuch nahe huha")
                        i += 1
                    elif s == "water" and p == "water":
                        print("are kuch nahe huha lagtha he dono dost bangaye")
                        i += 1
                    elif s == "gun" and p == "gun":
                        print("are kuch nahe huha inka kuch nahe hoga")
                        i += 1
                    elif s == "snake" and p == "water":
                        print("are thu tho jeet gaya")
                        t += 1
                    elif s == "water" and p == "gun":
                        print("are thu tho jeet gaya congragulations man")
                        t += 1
                    elif s == "gun" and p == "snake":
                        print("are thu tho jeet gaya lagtha he indono ko thum jeethhi jahoge")
                        t += 1
                    elif s == "snake" and p == "gun":
                        print("firse try kar")
                        r += 1
                    elif s == "water" and p == "snake":
                        print("firse tru kar")
                        r += 1
                    elif s == "gun" and p == "water":
                        print("firse!!!")
                    if exit == True:
                        print("!!!results!!!")
                        print("the number of times you are won is ", t)
                        print("the number of times you are lost is ", r)
                        print("the number of times you are draw with computer is ", i)
                        if t > r:
                            print("you are won")
                        elif t < r:
                            print("you need to try again to ")
                        else:
                            print("you are draw")
        else:
            print("have a good day")
# finally we are done with code
else:
    print("sir have a good day")
