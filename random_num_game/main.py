import random


print("Welcome to the guessing game")
Welcome = input("What is your name? \n")
print("Welcome " + Welcome)
print("Let's get started")
tries = 0
x = 0
y = 0
score = 0
GUESSES = []
z = 0
while x < 5:
    print("\n\nRound ", y+1)
    Com_guess = random.randint(1, 9)
    #print(Com_guess)
    print("Guess the generated number, you have three trials")
    guess = eval(input('Enter you first guess:'))
# use for loop the while loop
    tries = 0
    GUESSES.append(Com_guess)

    while tries < 3:
        if guess == Com_guess and tries == 0:
            print("You are correct, you get 10 points")
            tries = 5
            score += 10
        elif guess == Com_guess and tries == 1:
            print("You are correct, you get 5 points")
            score += 5
            tries = 5
        elif guess == Com_guess and tries == 2:
            print("You are correct, you get 3 points")
            score += 3
            tries = 5
        elif guess != Com_guess and tries == 2:
            break
        else:
            newguess = eval(input('Try another number:'))
            guess = newguess
        tries += 1

    y += 1
    x += 1

print("\nYour final score is ", score)
print(GUESSES)