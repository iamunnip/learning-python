import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = str(input("Enter your choice (rock, paper, scissors) "))
print("Computer choice", computer_choice)

if computer_choice == user_choice:
    print("Tie")
elif user_choice == "rock" and computer_choice == "scissors":
    print("User wins")
elif user_choice == "paper" and computer_choice == "rock":
    print("User wins")
elif user_choice == "scissors" and computer_choice == "paper":
    print("User wins")
else:
    print("Computer wins")
