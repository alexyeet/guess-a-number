import random
import math

#configuration

low=1
high=100
limit=round(math.log(high-low+1, 2) +.5)


#welcome screen

print ("welcome 2   g u e s s   a   n u m b e r")


#translating guess to numeric

def get_guess():
    while True:
        g = input("take a guess: ")
        
        if g.isnumeric():
            g=int(g)
            return g
        else:
            print ("hey dude it's gotta be a number")

#play game

def play_again():
    while True:
        decision=input("wanna play again? (y/n)")
        decision = decision.lower()

        if decision == "y" or decision == "yes":
                return True
        elif decision == "n" or decision =="no":
                return False

        print ("i'm confused please say 'y' or 'n'")

again=True 
                       
while again:     
    #game start

    print ("u got " + str(limit) + " guesses") 

    rand = random.randint(low, high)
    print("i'm thinking of a number from "+str(low)+" to "+str(high)+".");

    guess = -1
    tries = 0

    #play game

    while guess != rand and tries < limit:
        guess = get_guess()
        
        if guess < rand:
            print("too low")
        elif guess > rand:
            print("too high")

        tries += 1

    #game end
        
    if guess == rand:
        print ("yeet u did it")
        print ("u should be a medical terminologist")

    else:
        print ("ur dumb as bricks it was actually " +str(rand))
        print ("try taking medical terminology then try again :/")

    again=play_again()

print ("see ya later")
    
    
