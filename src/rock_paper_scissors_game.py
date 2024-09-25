# MIT License

# Copyright (c) 2023 Priyansh Sanjaybhai Zinzuvadia

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import random

# ASCII art for the game outcomes
rock = """
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     ________
---'    _____)____
           _______)
          ________)
         ________)
---.___________)
"""

scissors = """
   ________
---'   _____)____
          _______)
       ___________)
      (____)
---.__(___)
"""

# Mapping for user input to ASCII art
options = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

# List of outcomes
outcomes = ["It's a tie!", "You lost!", "You won!"]

def main():
    while True:
        try:
            # Get user input and validate
            user_input = input("Please type your input (Rock/Paper/Scissor) or 'q' to quit:\n").lower()

            if user_input == 'q':
                print("Thanks for playing. Goodbye!")
                break  # Exit the loop if the user inputs 'q'

            if user_input not in options:
                raise ValueError("Please input a valid value")

            # Display user's choice
            print("\nYour Input:\n", options[user_input])

            # Generate random computer output and display corresponding ASCII art
            comp_output = random.randint(0, 2)
            print("\nComputer's Input:")
            print(options["rock" if comp_output == 0 else "paper" if comp_output == 1 else "scissors"])

            # Determine the winner
            result = (comp_output - ["rock", "paper", "scissors"].index(user_input)) % 3
            print(outcomes[result])

        except ValueError as ve:
            print(f"Error: {ve}")
            

if __name__ == "__main__":
    main()
