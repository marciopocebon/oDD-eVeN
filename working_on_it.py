import random

runs = 0
runs1 = 0

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


# BOWLING FIRST
def bowling1():
    for i in range(120):
        global runs1
        comp1 = int(input("Enter a number between 1 and 6 \n"))
        user1 = random.randint(1, 6)
        print(user1)
        if user1 == comp1:
            print("Computer is out")
            print("Runs scored " + str(runs1))
            print("Target " + str(runs1 + 1))
            break
        else:
            runs1 += comp1

def batting2():
    sum2 = 0
    for i in range(120):
        user1 = int(input("Enter a number between 1 and 6 \n"))
        comp1 = random.randint(1, 6)
        print(comp1)
        if user1 == comp1:
            print("You are out")
            print("You have scored :  " + str(sum2))
            break
        else:
            sum2 += comp1

        if target > sum2:
            print("\n Computer wins")
            break

    if sum2 > target:
        print("\n You win")






coin = random.randint(1,2)
toss = int(input("Put Toss..........Choose 1 or 2\n"))

if toss == coin:
    print("You Won The Toss")
    choice = int(input("Batting (1) \nBowling (2) \n"))
    if choice == 1:
        batting1();
        target = runs
        bowling2();
    if choice == 2:
        bowling1()
        target = runs1
        batting2();


else:
    print("You Lost The Toss \n")
    comp2 = random.randint(1, 2)
    if comp2 == 1:
        print("Computer chose Bowling \n")
        batting1();
        target = runs
        bowling2();
    if comp2 == 2:
        print("Computer chose Batting \n")
        bowling1()
        target = runs1
        batting2();

#print(" \n In this game you get to play batting first. The rest is just normal odd or even game. \n")
