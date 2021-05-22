


import random

#def is to dine a function
# pass x as a parameter 
# use whule loop since we dont know how many iterations, looking for x
#  as long as guess does not = the random number 
# make user inoput number
#
#
#
#
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}'))
        if guess < random_number:
            print("Sorry to low try again")
        elif guess > random_number:
            print("Sorry guess again Too high")

    print(f"Yay you guess number {random_number} correctly")

guess(10)

def computer_guess(x):
    low = 1
    high = x 
    feedback = ''
# we want to be able to let them know if they are too high or to low so we pass  low and high parameters in
    while feedback != 'c' :
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f' Is {guess} to high (H), too low (L) or correct (C)').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1

    print(f"the computer guessed your number, {guess}, correctly!")








