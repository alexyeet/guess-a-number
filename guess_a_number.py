import random

#configuration

low=1
high=100
limit=10

#translating guess to numeric

def get_guess():
    while True:
        g = input("take a guess: ")
        
        if g.isnumeric():
            g=int(g)
            return g
        else:
            print ("hey dude it's gotta be a number")

#game start 

rand = random.randint(low, high)
print("i'm thinking of a number from "+str(low)+" to "+str(high)+".");

guess = -1
tries = 0

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
    
    
