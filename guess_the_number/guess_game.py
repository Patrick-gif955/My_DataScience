
import random

x = random.randint(1, 20)
# You are to enter a number between 1 and twenty, the aim is to try to guess the number the computer picked between one and twnty
while True:
    user_input = input("Enter a number between 1 to 20, press d to exit: ")

    if user_input.lower() == "d":
        break
    try:
        guess = int(user_input)
        if guess == x:
            print(f"Hurray 🥳 You guessed right the number is {x}")
            break
        elif guess < x:
            print(f"Your guess is {guess}, it's too low , try again ")
        elif guess > x:
            print(f"Your guess is t{guess}, it's oo high, try again")
    except ValueError:
        print("Invalid input")

