# Day 11 - Blackjack Project

This project focuses on building a card game using Python logic, flow control, and custom functions. It demonstrates intermediate programming skills like function composition, list management, condition handling, and loop-driven gameplay.

## ✅ What I Learned
- How to use functions to modularize game logic (`deal_card`, `calculate_score`, `compare`)
- How to handle edge cases like Blackjacks and Aces (11 or 1 logic)
- How to structure a game that interacts with the user via inputs and outputs
- How to simulate a simplified version of real Blackjack game rules
- How to write clean and structured code that separates responsibilities

## 📁 Files
- `main.py`: Contains the full logic of the Blackjack game including user interaction, score comparison, and computer AI (draws up to 17).
- `art.py`: Includes an ASCII logo for visual enhancement at the start of the game.

## 📝 Notes
- The game begins with two cards dealt to both the user and the computer.
- Aces are handled with a dynamic value (11 or 1) to prevent busts.
- If the user gets a Blackjack (21 with 2 cards), the game ends immediately.
- The user can choose to draw more cards; the computer automatically draws until it reaches a score of 17 or more.
- Results include win, lose, or draw, with custom feedback using emojis.
- ASCII art (`logo`) is displayed at the start using `from art import logo`.
- The game can be replayed as many times as the user wants by typing `'y'`.