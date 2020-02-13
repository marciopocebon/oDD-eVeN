import random

runs = 0

#BATTING First
def batting1():

    for i in range(120):
        global runs
        user = int(input("Enter a number between 1 and 6 \n"))
        comp = random.randint(1, 6)
        print(comp)
        if user == comp:
            print("You are out")
            print("You have scored " + str(runs))
            print("Target " + str(runs + 1))
            break
        else:
            runs += user



def bowling2():
    sum2 = 0
    for i in range(120):
        user = int(input("Enter a number between 1 and 6 \n"))
        comp = random.randint(1, 6)
        print(comp)
        if user == comp:
            print("Computer is out")
            print("Computer has scored " + str(sum2))
            break
        else:
            sum2 += comp

        if sum2 > target:
            print("\n Computer wins")
            break

    if target > sum2:
        print("\n You win")



coin = random.randint(1,2)
toss = int(input("Put Toss..........Choose 1 or 2\n"))

if toss == coin:
    print("You Won The Toss")
    choice = int(input("Batting (1) \nBowling (2) \n"))
else:
    print("You Lost The Toss \n")
    print("Computer Choose Bowling \n")
#print(" \n In this game you get to play batting first. The rest is just normal odd or even game. \n")


batting1();
target = runs
bowling2();






