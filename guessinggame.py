import random
actual = random.randint(1, 99)
guess = int(raw_input("Guess a number between 1 and 99:"))
while actual != "guess":
    print
    if guess < actual:
        print ("Your guess is too low!")
        guess = int(raw_input("Enter an integer from 1 to 99:"))
    elif guess > actual:
        print ("Your guess is too high!")
        guess = int(raw_input("Enter an integer from 1 to 99:"))
    else:
        print ("You guessed it!")
        break
    print

