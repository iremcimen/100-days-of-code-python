# Day 12 - Number Guessing Game

This project is a simple interactive game where the player tries to guess a randomly selected number between 1 and 100.
It demonstrates the use of functions, conditional logic, loops, and user input handling in Python. The game includes two
difficulty levels that affect the number of guesses allowed.

## ✅ What I Learned

- How to define and use functions with parameters and return values
- How to implement game logic using `if-elif-else` statements
- How to use loops (`while`) to control game flow and user interaction
- How to set difficulty levels that impact gameplay
- How to provide feedback to the user after each guess
- How to import and use external modules (`random` and `art`)

## 📁 File

- `solution_2.py` : Contains the full game logic including difficulty selection, guess checking, and user feedback.

## 📝 Notes

- The game generates a random number between 1 and 100 using `randint` from the `random` module
- The player chooses a difficulty level: `easy` gives 10 guesses, `hard` gives 5 guesses
- After each guess, the player receives feedback if the guess is too high, too low, or correct
- The game ends when the player guesses correctly or runs out of attempts
- The game displays an ASCII art logo at the start using `from art import logo`  
