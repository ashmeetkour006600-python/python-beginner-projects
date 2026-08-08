#  ROCK PAPER SCISSORS GAME
print("let's start the game")
import random
userscore=0
computerscore=0

for i in range(1,4):
    
    choose=random.choice(["rock","paper","scissors"])
    guess = input("enter choice:")
    
    if guess == choose:
        print("match draw")
        
    elif guess =="rock" and choose == "scissors":
        print(" rock beats scissors")
        userscore=userscore+1
        
        
    elif guess =="paper" and choose == "scissors":
        print(" scissors cuts the paper ")
        computerscore=computerscore+1
       
    elif guess =="rock" and choose == "paper":
         print(" paper catch the rock ")
         computerscore=computerscore+1
    
    
    print("the choioce is:",choose)
    print("user score:",userscore)
    print("computer score:",computerscore)
if computerscore > userscore:
        print("computer is the winner")
    
elif computerscore==userscore:
    print("it's a draw")
else:
    print("user is the winner")
