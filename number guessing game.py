import random

def guess(x):
    random_number = random.randint(1, x)  
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number between 1 and {x}: ')) 
        if guess > random_number:
            print('Sorry, you are too high!')
        elif guess < random_number:
            print('Sorry, you are too low!')

    print('You guessed it correctly!')

guess(100)

        
    

