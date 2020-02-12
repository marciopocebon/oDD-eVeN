import random
print("\nIn this game you get to play batting first. The rest is just normal odd or even game.\n")
sum1=0
for i in range(100):
    human=int(input("Enter a number between 1 and 6\n"))
    comp=random.randint(1,6)
    print(comp)
    if human==comp:
        print("You are out")
        print("You have scored "+str(sum1))
        break
    else:
        sum1+=human

sum2=0
for i in range(100):
    human=int(input("Enter a number between 1 and 6\n"))
    comp=random.randint(1,6)
    print(comp)
    if human==comp:
        print("Computer is out")
        print("Computer has scored "+str(sum2))
        break
    else:
        sum2+=comp
    if sum2>sum1:
        print("\nComputer wins")
        break

if sum1>sum2:
    print("\nYou win")
