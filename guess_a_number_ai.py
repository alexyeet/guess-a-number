
#guess a number a.i.
#alex f
#
#this program prompts the player to choose a number and guesses it.



import random
import math 


# config
pass

# helper functions

def show_start_screen():
    print("*************************")
    print("*  guess a number ai!!  *")
    print("*************************")
    print("in this game, you will be asked to choose a low and high number")
    print("then, you'll choose a number within that range")
    print("i will guess it!")


def show_credits():

    print("thank you for playing, "+name+"! ")
    print("this game was made by alex f in mr coopers programming 1 class :)")
    
    print("thanks for playing!! ┬┴┬┴┤( ͡° ͜ʖ├┬┴┬┴")
    print("completed on 10/6/17") 
    
def high_and_low():

    low = int(input("give me a low number, "+name+"  "))
    high = int(input("ok, now give me a high number, "+name+"  "))
    return low, high
    

def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """

    guess = (current_high+current_low)//2
    return guess


def pick_number(low, high):
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    print ("think of a number between " +str(low) + " and " +str(high)+", "+name)
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

        correct = input("is " + str(guess) + " correct, "+name+"? (type y/n) ")

        if correct.lower() == 'y' or correct.lower() == 'yes':
            return 0

        highlow = input("is your number higher or lower,"+name+"? (type h/l) ")
        
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
    
    print ("i guessed it, " +name +"! :) ")

def play_again():
    while True:
        decision = input("would you like to play again, "+name+"? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("i don't understand, "+name+". please enter 'y' or 'n' ")

    
def play():

    current_low,current_high = high_and_low()
    check = -1
    tries = 0

    limit=round(math.log(current_high-current_low+1, 2) +.5)
    
    pick_number(current_low, current_high)
    
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

name = input("first, what is your name?  ")

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



