import random
num = random.randint(1, 9)
guess = int(input("What is your guess? "))
while (guess != num):
    if(guess > num):
        print("Too high!")
    else:
        print("Too low!");
    guess = int(input("What is your next guess? "))
print("Correct!")