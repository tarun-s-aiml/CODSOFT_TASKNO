# CODSOFT Python Programming Internship
# Task 4: Rock-Paper-Scissors Game

import random


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"

    if (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"

    return "computer"


def play_game():
    choices = ["rock", "paper", "scissors"]

    user_score = 0
    computer_score = 0

    while True:
        print("\n==============================")
        print("    ROCK PAPER SCISSORS")
        print("==============================")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "4":
            print("\nFinal Score:")
            print("You:", user_score)
            print("Computer:", computer_score)
            print("\nThanks for playing!")
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
            continue

        user_choice = choices[int(choice) - 1]
        computer_choice = random.choice(choices)

        print("\nYou chose:", user_choice)
        print("Computer chose:", computer_choice)

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("Result: It's a tie!")

        elif winner == "user":
            print("Result: You win!")
            user_score += 1

        else:
            print("Result: Computer wins!")
            computer_score += 1

        print("\nScore:")
        print("You:", user_score)
        print("Computer:", computer_score)


if __name__ == "__main__":
    play_game()
