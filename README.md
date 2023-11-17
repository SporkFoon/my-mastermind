# Mastermind Game

## Overview

The provided Python program is an implementation of the classic game **Mastermind**. Mastermind is a code-breaking game where the player attempts to guess a secret color sequence within a certain number of rounds.

## Program Flow

1. **Random Solution Generation:**
   - The program generates a random solution, which is a sequence of colors.
   - The number of positions in the sequence (`num_positions`) and the number of possible colors (`num_colors`) are also randomly determined.

2. **Player Guesses:**
   - The player is prompted to make guesses for the color sequence by entering their guess through the console.

3. **Guess Validation:**
   - The program checks the validity of the player's guess:
     - Ensures that the guess has the correct length.
     - Verifies that the guess contains valid color representations.

4. **Feedback and Visual Representation:**
   - If the guess is valid, the program provides feedback on the guess by comparing it to the randomly generated solution.
   - The feedback consists of two components:
     - The number of correctly guessed colors in the correct positions (`correct_position`).
     - The number of correctly guessed colors in the incorrect positions (`correct_color`).
   - The program prints a visual representation of the feedback using '(star)' and 'o' symbols.
	 - '(star)' represents a correctly guessed color in the correct position.
	 - 'o' represents a correctly guessed color in the incorrect position.
	 - The visual representation is printed in the same order as the player's guess.

5. **Game Continues:**
   - The player continues making guesses until they correctly guess the entire color sequence (i.e., `correct_position` equals the number of positions in the sequence).

6. **Game Completion:**
   - Once the player correctly guesses the sequence, the program prints the number of rounds it took to solve the puzzle.
