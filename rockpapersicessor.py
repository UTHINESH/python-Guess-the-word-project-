import random

print("Welcome to the Rock, Paper, Scissors Game!")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"

    elif user_choice == 'quit':
        print("Goodbye!")
        quit()

    else:
        return "Computer wins!"

while True:
    user_choice = input("Enter your choice ((rock, paper, scissors) or QUIT to quit the game): ").lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    print(f"Computer chose {computer_choice}. {determine_winner(user_choice, computer_choice)}")


