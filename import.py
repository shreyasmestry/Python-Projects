import random
while True:
    a=random.randint(1,3)
    b=int(input("Guess a number: "))
    print(f"Computer generated {a}")
    if a==b:
        print("You won!")
        break
    else:
        print("Better Luck Next Time!")
        


