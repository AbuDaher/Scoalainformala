
import random
computer_wins = 0
player_wins = 0
player_name = input("Your name is: ")


def player_options():
    user_choice = input("Choose from Rock, Paper or Scissors: ")
    global user_choice
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "P", "p"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "S", "s"]:
        user_choice = "s"
    else:
        print("Invalid choice")
        player_options()
    return user_choice


def computer_options():
    comp_choice = random.randint(1, 3)
    global comp_choice
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
    user_choice = player_options()
    comp_choice = computer_options()
    if user_choice == "r":
        if comp_choice == "r":
            print("Your choice was rock, computer chose rock, tied. ")
        elif comp_choice == "p":
            print("Your choice was rock, computer chose paper, you lost. ")
            computer_wins += 1
        elif comp_choice == "s":
            print("Your choice was rock, computer chose scissors, you won. ")
            player_wins += 1
    elif user_choice == "p":
        if comp_choice == "p":
            print("Your choice was paper, computer chose paper, tied. ")
        elif comp_choice == "s":
            print("Your choice was paper, computer chose scissors, you lost. ")
            computer_wins += 1
        elif comp_choice == "r":
            print("Your choice was paper, computer chose rock, you won. ")
            player_wins += 1
    elif user_choice == "s":
        if comp_choice == "s":
            print("Your choice was scissors, computer chose scissors, tied. ")
        elif comp_choice == "r":
            print("Your choice was scissors, computer chose rock, you lost. ")
            computer_wins += 1
        elif comp_choice == "p":
            print("Your choice was scissors, computer chose paper, you won. ")
            player_wins += 1

    print("Player wins : " + str(player_wins))
    print("Computer wins :" + str(computer_wins))

    user_choice = input("Do you want to play again ? (y/n) ")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        print("Good bye !")
        break
    else:
        print("Invalid choice")
        input("Do you want to play again ? (y/n) ")
