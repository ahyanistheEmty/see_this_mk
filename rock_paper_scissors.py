import random

def play_game():
    options = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
        if user_choice == 'quit':
            break
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue
            
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
        print("-" * 20)

if __name__ == "__main__":
    play_game()
