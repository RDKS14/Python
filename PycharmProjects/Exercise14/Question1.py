import random
print("Welcome to my Rock, Paper, Scissors Game \n "
      "There is just 3 Rules:\n "
      "1.Rock Smashes Scissors\n "
      "2.Paper Covers Rock\n "
      "3.Scissors Cuts Paper\n "
      "Good Luck" )

user = input("Enter a choice (rock, paper, scissors): ")
actions = ["rock", "paper", "scissors"]
computer = random.choice(actions)
print(f"\nYou chose {user}, computer chose {computer}.\n")

if user == computer:
   print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
elif user == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
