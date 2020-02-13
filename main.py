import random

runs = 0
def batting():

    for i in range(120):
        global runs
        user = int(input("Enter a number between 1 and 6 \n"))
        comp = random.randint(1, 6)
        print(comp)
        if user == comp:
            print("You are out")
            print("You have scored " + str(runs))
            break
        else:
            runs += user




print(" \n In this game you get to play batting first. The rest is just normal odd or even game. \n")


batting();
target = runs + 1

sum2 = 0
for i in range(120):
    user = int(input("Enter a number between 1 and 6 \n"))
    comp = random.randint(1,6)
    print(comp)
    if user == comp:
        print("Computer is out")
        print("Computer has scored " + str(sum2))
        break
    else:
        sum2 += comp

    if sum2 > target:
        print("\nComputer wins")
        break

if target > sum2:
    print("\n You win")



