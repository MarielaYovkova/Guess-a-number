import random
computer_num = random.randint(1, 100)

while True:
    player_input = input('Guess a number between 1 and 100!')
    if not player_input.isdigit():
        print('Invalid input.Try again!')
        continue
    player_number = int(player_input)
    if player_number == computer_num:
        print('You guess it!')
        break
    elif player_number > computer_num:
        print('Too high!')
    else:
        print('Too low!')
