import random

secret_number = random.randint(1, 20)

guess_number = int(input("Guess a number: "))

attempts = 5

while secret_number != guess_number and attempts > 0:

    if guess_number > secret_number:
        print("Too high!")

    elif guess_number < secret_number:
        print("Too low!")

    attempts -= 1

    print(f"Attempts remaining: {attempts}")

    if attempts > 0:
        guess_number = int(input("Guess again: "))


if guess_number == secret_number:
    print("Correct! 🎉")
else:
    print(f"Game over! The number was {secret_number}")