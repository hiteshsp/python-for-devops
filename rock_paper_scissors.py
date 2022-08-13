import random

def get_choices():
  player_choice = input("Enter your choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = { "player": player_choice, "computer": computer_choice }
  return choices

def check_win(player, computer):
  print(f"You chose {player}, Computer chose {computer}")
  if player == computer:
      return "It's a tie."
  elif player == "rock":
      if computer == "paper":
        return "Paper covers rock. You lose."
      if computer == "scissors":
        return "Rock smashes scissors. You Win!"
  elif player == "paper":
      if computer == "rock":
        return "Paper covers rock. You Win!"
      if computer == "scissors":
        return "Scissors cuts paper. You lose."    
  elif player == "scissors":
      if computer == "paper":
        return "Scissors cut Paper. You Win!"
      if computer == "rock":
        return "Rock smashes scissors. You lose."

choices = get_choices()
print(check_win(choices["player"], choices["computer"]))