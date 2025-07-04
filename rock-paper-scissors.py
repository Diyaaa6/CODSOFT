import random
L=["rock","paper","scissor"]
u=0
c=0
ch=True
while ch:
    
    user=input("Enter your choice(rock, paper, or scissors): ")
    num = random.randint(0,2)
    print("Computer choose: ",L[num])
    if(user=="rock"):
        if(num==0):
            print("Tie!")
            print()
        elif(num==1):
            print("Comuter wins!")
            c+=1
            print()
        elif(num==2):
            print("You win!")
            u+=1
            print()
        else:
            print("Oops! my bad")
    elif(user=="paper"):
        if(num==0):
            print("You win!")
            u+=1
        elif(num==1):
            print("Tie!")
        elif(num==2):
            print("Comuter wins!")
            c+=1
        else:
            print("Oops! my bad")
    elif(user=="scissors"):
        if(num==0):
            print("Comuter wins!")
            c+=1
            print()
        elif(num==1):
            print("You win!")
            u+=1
            print()
        elif(num==2):
            print("Tie!")
            print()
        else:
            print("Oops! my bad")
    else:
        print("OOPS enter a valid choice!")
    chi=input("Do you want to continue(Y/N)?!")
    print()
    if(chi=="Y"):
        ch=True
    elif(chi=="N"):
        print("Your total score is: ",u)
        print("Computer's total score is: ",c)
        ch=False
    else:
        print("A wrong choice!")
