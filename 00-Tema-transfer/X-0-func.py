
import random

my_list = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]
player = ["x", "0"]
winner = None
game_on = True


def print_my_list(my_list):
    print(my_list[0] + " | " + my_list[1] + " | " + my_list[2])
    print(my_list[3] + " | " + my_list[4] + " | " + my_list[5])
    print(my_list[6] + " | " + my_list[7] + " | " + my_list[8])


def first_player():
    ask_player = input('Do you want to go first: " yes/no "')
    if player in ['yes', 'Yes', 'y', 'Y']:
        return True
    else:
        return False


first_player()


def player_input(my_list):
    player_choice = int(input("Select a number between 1-9: "))
    while player_choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("Try again ! ")
        player_choice = int(input("Select a number between 1-9: "))
    while my_list[player_choice -1] != "-":
        print("Oops player is already at that spot.")
        player_choice = int(input("Select a number between 1-9: "))
    else:
        my_list[player_choice-1] = "X"


def check_lines(my_list):
    global winner
    if my_list[0] == my_list[1] == my_list[2] and my_list[0] != "-":
        winner = my_list[0]
        return True
    elif my_list[3] == my_list[4] == my_list[5] and my_list[3] != "-":
        winner = my_list[3]
        return True
    elif my_list[6] == my_list[7] == my_list[8] and my_list[6] != "-":
        winner = my_list[6]
        return True


def check_rows(my_list):
    global winner
    if my_list[0] == my_list[3] == my_list[6] and my_list[0] != "-":
        winner = my_list[0]
        return True
    elif my_list[1] == my_list[4] == my_list[7] and my_list[1] != "-":
        winner = my_list[1]
        return True
    elif my_list[2] == my_list[5] == my_list[8] and my_list[2] != "-":
        winner = my_list[2]
        return True


def check_diagonal(my_list):
    global winner
    if my_list[0] == my_list[4] == my_list[8] and my_list[0] != "-":
        winner = my_list[0]
        return True
    elif my_list[2] == my_list[4] == my_list[6] and my_list[4] != "-":
        winner = my_list[2]
        return True


def check_win(my_list):
    global game_on
    if check_lines(my_list):
        print_my_list(my_list)
        print(f"The winner is {winner}!")
        game_on = False
    elif check_rows(my_list):
        print_my_list(my_list)
        print(f"The winner is {winner}!")
        game_on = False

    elif check_diagonal(my_list):
        print_my_list(my_list)
        print(f"The winner is {winner}!")
        game_on = False


def check_tie(my_list):
    global game_on
    if "-" not in my_list:
        print_my_list(my_list)
        print("It is a tie!")
        game_on = False


def switch_player(my_list):
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


def computer(my_list):
    while player == "O":
        if my_list[4] == "-":
            my_list[4] = "0"
        elif my_list[0] == "-":
            my_list[0] = "0"
        elif my_list[2] == "-":
            my_list[2] = "0"
        elif my_list[6] == "-":
            my_list[6] = "0"
        elif my_list[8] == "-":
            my_list[8] = "0"
        else:
            options = [1, 3, 5, 7]
            computer_choice = random.choice(options)
            while my_list[computer_choice - 1] == "X":
                computer_choice = random.choice(options)
        switch_player(my_list)


while game_on:
    print_my_list(my_list)
    player_input(my_list)
    check_win(my_list)
    check_tie(my_list)
    switch_player(my_list)
    computer(my_list)
    check_win(my_list)
    check_tie(my_list)
