# MIT License

# Copyright (c) 2023 Priyansh Sanjaybhai Zinzuvadia

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import unittest
from unittest.mock import patch
from io import StringIO
import stone_paper_scissors_game


class TestStonePaperScissorsGame(unittest.TestCase):

    # Test for the game exit functionality when the user inputs 'q'
    @patch("builtins.input", side_effect=["rock", "q"])
    def test_game_exit(self, mock_input):
        # Redirect the standard output to capture printed messages
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            # Run the main function of the game
            stone_paper_scissors_game.main()
            # Assert that the printed output matches the expected farewell message
            self.assertEqual(mock_stdout.getvalue().strip(), "Thanks for playing. Goodbye!")

    # Test for handling an invalid input followed by a valid input
    @patch("builtins.input", side_effect=["invalid", "rock", "q"])
    def test_invalid_input_then_valid_input(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            stone_paper_scissors_game.main()
            # Define the expected output when an invalid input is given and then the player wins
            expected_output = "Error: Please input a valid value\nYour Input:\n\nComputer's Input:\n\nIt's a tie!"
            # Assert that the printed output matches the expected output
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    # Test for the scenario where the player wins
    @patch("builtins.input", side_effect=["rock", "q"])
    @patch("random.randint", return_value=0)
    def test_player_wins(self, mock_randint, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            stone_paper_scissors_game.main()
            # Define the expected output when the player wins
            expected_output = "Your Input:\n\nComputer's Input:\n\nYou won!"
            # Assert that the printed output matches the expected output
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    # Add more test cases for different scenarios


if __name__ == '__main__':
    unittest.main()
