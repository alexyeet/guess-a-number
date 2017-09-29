
#guess a number a.i.
#alex f
#
#this program prompts the player to choose a number and guesses it.



import random
import math 

# config
low = 1
high = 10
limit=round(math.log(high-low+1, 2) +.5)


# helper functions

def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    pass
    
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """

    guess = (current_high+current_low)//2
    return guess


def pick_number():
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    print ("think of a number between " +str(low) + " and " +str(high))
    print ("press enter when you're done :) ")
    cont=input()

def check_guess(guess):

    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """

    while True:

        correct = input("is " + str(guess) + " correct? (type y/n) ")

        if correct.lower() == 'y' or correct.lower() == 'yes':
            return 0

        highlow = input("is your number higher or lower? (type h/l) ")
        
        if highlow.lower() == 'h':
            check = -1
            return check
        elif highlow.lower() == 'l':
            check = 1
            return check
   

def show_result(guess):
    """
    Says the result of the game. (The computer might always win.)
    """
    
    print ("told you i'm a genius :^)")

def play_again():
    while True:
        decision = input("would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("i don't understand. please enter 'y' or 'n' ")

    tries += 1

    while False:
        print("thanks for playing!! ┬┴┬┴┤( ͡° ͜ʖ├┬┴┬┴")
    
def play():
    current_low = low
    current_high = high
    check = -1
    tries = 0
    
    pick_number()
    
    while check != 0 and tries < limit:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            # adjust current_low
            current_low=guess
        elif check == 1:
            # adjust current_high
            current_high=guess
        tries += 1

    show_result(guess)


# game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



