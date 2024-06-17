import random

user_wins = 0
computer_wins = 0

options = ["r","p","s"]

print("Type your choice \nrock : r \npaper : p\nscissors : s")

while True:
    user_input = input("Type r / p / s  or Q to Quit:").lower()
    if user_input =="q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")

    if user_input == "r" and computer_pick == "s":
        print("You Won!")
        user_wins +=1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins+=1

print("You won", user_wins,"Times.")
print("Computer won", computer_wins,"Times.")
print("Goodbye!")
