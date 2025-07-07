"""
Write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.

2. Then check for the number of times the letters in the word LOVE occurs.

3. Then combine these numbers to make a 2 digit number and print it out.
"""

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    true_count = (
            combined_names.count("t") +
            combined_names.count('r') +
            combined_names.count('u') +
            combined_names.count('e')
    )

    love_count = (
            combined_names.count('l') +
            combined_names.count('o') +
            combined_names.count('v') +
            combined_names.count('e')
    )

    love_score = int(str(true_count) + str(love_count))

    print(love_score)

calculate_love_score("yunus", "irem")

