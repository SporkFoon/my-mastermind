import random

def play_mastermind():
    num_positions = random.randint(1, 10)
    num_colors = random.randint(1, 8)
    solution = {0: 0, 1: False, 2: [random.randint(1, num_colors) for _ in range(num_positions)]}

    print(f"Playing Mastermind with {num_colors} colors and {num_positions} positions")

    while not solution[1]:
        guess = input("What is your guess?: ")

        if len(guess) != num_positions or any(ord(c) <= ord('0') or ord(c) > ord('0') + num_colors for c in guess):
            print("Bad guess.\nTry again.")
        else:
            print(f"Your guess is {guess}")
            solution[0] += 1
            feedback = {'correct_position': 0, 'correct_color': 0}

            for i in range(num_positions):
                if ord(guess[i]) - ord('0') == solution[2][i]:
                    feedback['correct_position'] += 1
                elif (ord(guess[i]) - ord('0')) in solution[2]:
                    feedback['correct_color'] += 1

            print('*' * feedback['correct_position'] + 'o' * feedback['correct_color'])

            solution[1] = True if feedback['correct_position'] == num_positions else False

    print(f"You solved it after {solution[0]} rounds.")


play_mastermind()