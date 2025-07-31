# Day 10 - Calculator Project

This project covers intermediate Python concepts such as:
- Functions with outputs
- Reusing functions (recursive function calls)
- Dictionaries for function selection
- While loops and user-driven flow control
- Importing external modules (like `art` for ASCII art)

## ✅ What I Learned
- How to define functions that return values
- How to store functions inside a dictionary and call them dynamically
- How to use while loops to create an ongoing calculation
- How to recursively restart a program from within itself
- How to structure a simple calculator using clean, readable logic

## 📁 File
- `main.py`: Contains the final version of the calculator app with function mapping and recursive restart logic.

## 📝 Notes
- The calculator allows users to perform continuous operations using the previous result.
- If the user types 'n', the screen is cleared (simulated with `print("\n" * 20)`) and a new calculation begins.
- ASCII art is displayed at the start using an external `art` module (`from art import logo`).