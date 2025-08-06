# Day 12 - Number Guessing Game

This project focuses on applying conditional logic, loops, and user input to build an interactive number guessing game. It incorporates difficulty levels and feedback-based user interaction to make the game dynamic and engaging.

## ✅ What I Learned
- How to use the `random module` to generate random numbers

- How to use `if-else statements` to control game logic

- How to implement difficulty settings using variable values

- How to manage game flow using `while loops` and `boolean flags`

- How to structure user interaction for a simple game

## 📁 File
- `solution_1.py`: Contains the number guessing game logic with easy/hard mode and feedback after each guess

## 📝 Notes
- The game picks a number between 1 and 100 using `random.randint()`

- Player chooses a difficulty level which determines the number of attempts (easy = 10, hard = 5)

- After each incorrect guess, the player is told whether the guess was too high or too low

- When attempts run out, the correct answer is revealed

- The game uses an ASCII logo `from art import logo` to decorate the start screen