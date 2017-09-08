import random

#configuration

low=1
high=100

rand = random.randint(low, high)
print("i'm thinking of a number from "+str(low)+" to "+str(high)+".");

guess = -1

while guess != rand:
    guess = input("take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("too low")
    elif guess > rand:
        print("too high")
    else:
        print("good job!!!")

print("yeet")
