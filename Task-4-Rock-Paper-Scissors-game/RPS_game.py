import random

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def main():
    choices = ["rock", "paper", "scissors"]
    
    user_score = 0
    comp_score = 0

    print("=== CODSOFT - ROCK PAPER SCISSORS ===")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    print("Type 'quit' to exit\n")

    while True:
        user_choice = input("Your choice (rock/paper/scissors): ").lower().strip()
        
        if user_choice == "quit":
            break

        if user_choice not in choices:
            print("Invalid choice! Please type rock, paper, or scissors.\n")
            continue

        comp_choice = random.choice(choices)
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {comp_choice}")

        result = get_winner(user_choice, comp_choice)

        if result == "tie":
            print("Result: It's a Tie!")
        elif result == "user":
            print("Result: You Win! 🎉")
            user_score += 1
        else:
            print("Result: Computer Wins!")
            comp_score += 1
        
        print(f"Score -> You: {user_score} | Computer: {comp_score}\n")
        print("-" * 40 + "\n")

    print("\n=== Final Score ===")
    print(f"You: {user_score} | Computer: {comp_score}")
    if user_score > comp_score:
        print("Overall Winner: YOU! 🏆")
    elif comp_score > user_score:
        print("Overall Winner: COMPUTER")
    else:
        print("Overall: DRAW!")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()