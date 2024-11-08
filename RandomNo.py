import random

def guess(x):
    random_number = random.randint(1,x)
   
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter the random number from 1 to {x}: "))
        if guess < random_number:
            print("Sorry number is too low")
        elif guess > random_number:
            print("sorry number is too high")
        else:
            print("Your correct") 
    
    
             
guess(10)                
