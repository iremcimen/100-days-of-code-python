import random
from art import logo

easy = 10
hard = 5

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
answer = random.randint(1, 100)
# print(answer)

if difficulty == 'easy':
    chances = easy
else:
    chances = hard

game_over = False
while not game_over:
    if difficulty == 'easy':
        print(f"You have {chances} attempts remaining to guess the number.")
    elif difficulty == 'hard':
        print(f"You have {chances} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        game_over = True
    else:
        if guess > answer:
            print("Too high.")

        else:
            print("Too low.")

        chances -= 1

        if chances == 0:
            print(f"You've run out of guesses. You lose. The answer was {answer}.")
            game_over = True
        else:
            print("Guess again.")