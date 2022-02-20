from random import choice
player_name = input('Your name is: ')
print('Welcome: `Rock - Paper - Scissors` ')
game_on = True
while game_on:
    comp_choice = None
    user_choice = None
    while comp_choice == user_choice:
        user_choice = input('Chose from: "R/P/S"').lower()
        options = ['r', 'p', 'so']
        while user_choice not in options:
            user_choice = input('Choose from: "R/P/S"').lower()
        print('Tie, choose again! \n')

        comp_choice = choice(options)
        print(comp_choice)
    print(f'Computer choice was: {comp_choice}')
    print(f'{player_name} choice was {user_choice}')
    if user_choice == 'r':
        if comp_choice == 'p':
            print(f'You lost!')
        else:
            print('You won!')
    elif user_choice == 'p':
        if comp_choice == 's':
            print(f'You lost!')
        else:
            print('You won!')
    else:
        if comp_choice == 'r':
            print("You lost!")
        else:
            print('You won')
    game_status = input('Do yo want to play more? y/n ')
    while game_status not in 'yn':
        game_status = input('Do yo want to play more? y/n ')
    if game_status != 'y':
        game_on = False
