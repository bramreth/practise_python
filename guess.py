from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 4
# Start your game!
while guesses_left>0:
    guess = int(raw_input("guess:"))
    if guess == random_number:
        print 'you win!'
        break
    guesses_left -=1
else:
    print 'you lose.'