import random

print("RULES\n-------------------------------"
"-------------------------------------------" \
"-----------------------------------------\n1. I will choose a number between 1 and 100\n\
2. When a number is guessed, the user is told if the actual number is higher or lower\n\
3. The user will get a certain number of guesses, depending on the level of difficulty\n\
4. When a number is guessed, the number must be a whole number; going above 100 or below 1 is up to the user")

def start():
    while True:
        difficulty = input("\nSelect a difficulty: Easy, Medium, Hard")

        if str.lower(difficulty) == "easy" or str.lower(difficulty) == "e":
            chances = 16
            print(f"\nYou get {chances} chances!")
            return chances
        elif str.lower(difficulty) == "medium" or str.lower(difficulty) == "m":
            chances = 12
            print(f"\nYou get {chances} chances!")
            return chances
        elif str.lower(difficulty) == "hard" or str.lower(difficulty) == "h":
            chances = 8
            print(f"\nYou get {chances} chances!")
            return chances
        else:
            print("\n\nInvalid Input, Please Try Again!\n")


def game(chances):
    guesses = 0
    number = random.randint(1, 100)
    while True:
        if guesses >= chances:
            print(f"\nSorry, you weren't able to guess the number! The hidden number was {number}.")
            break
        guess = input("\n\nEnter your guess: ")
        if str(guess).isdigit():
            guesses += 1
            if int(guess) < number:
                print("\nHigher!")
            if int(guess) > number:
                print("\nLower!")
            elif int(guess) == number:
                print(f"\n\nCongradulations! you guessed the number in {guesses} try(s) with {chances - guesses} to go! The hidden number was {number}")
                break
        else:
            print("\n\nInvalid Input, Please Try Again!\n")

while True:
    play = input("\nWorld you like to play? (y or n)")
    if str.lower(play) == "y" or str.lower(play) == "yes":
        chances = start()
        game(chances)
    elif str.lower(play) == "n" or str.lower(play) == "no":
        break
    else:
        print("\n\nInvalid Input, Please Try Again!\n")
