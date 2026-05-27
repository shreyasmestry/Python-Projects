import random

options=["Rock","Paper","Scissors"]
i=0
while i<5:
    i+=1
    user=input("Enter Rock,Paper or Scissors(or quit to stop) : ")

    if user=="quit":
        print("Thanks for playing!Goodbye.")
        break
    if user not in options:
        print("Invalid input!Please try again.")
        continue

    computer=random.choice(options)

    if user==computer:
        print("It's a tie!")
    elif user=="Rock" and computer=="Scissors":
        print("You win!Rock crushes Scissors.")

    elif user=="Scissors" and computer=="Paper":
        print("You win!Scissors cut Paper.")

    elif user=="Paper" and computer=="Rock":
        print("You win!Paper covers Rock.")

    else:
        print("You Lose!")

