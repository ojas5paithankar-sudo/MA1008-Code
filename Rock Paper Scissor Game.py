import random
choices = ["ROCK", "PAPER", "SCISSORS"]

decision = random.choice(choices)

flag = False
while flag == False:
  playerInput = input("Rock, Paper, or Scissors?: ")
  if playerInput.upper() == "ROCK" or playerInput.upper() == "PAPER" or playerInput.upper() == "SCISSORS":
    flag = True
  else:
    flag = False
    print("Invalid input, try again")

if decision == playerInput.upper():
  print(f"Draw! computer also chose {decision}")
elif decision == "ROCK" and playerInput.upper() != "PAPER":
  print(f"You lose! computer chose {decision}")
elif decision == "PAPER" and playerInput.upper() != "SCISSORS":
  print(f"You lose! computer chose {decision}")
elif decision == "SCISSOR" and playerInput.upper() != "ROCK":
  print(f"You lose! computer chose {decision}")
else:
  print(f"You win! computer chose {decision}")
