#  Number guessing game
print("let's start the game")
import random
number = random.randint(1,100)
guess=1
while guess != number:
    guess=int(input("enter your number:"))
    if guess>number:
        print("the number is too high")
    

    elif guess < number:
         print("the number is too low")
    
    else:
         print("you guess correct number")
print("secret number is:",number)
