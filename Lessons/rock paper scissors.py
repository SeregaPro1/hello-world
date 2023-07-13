import random

while True:
    choices = ["rock", "paper", "scissors"]
    slice1 = slice(2, -2)

    computer = str(random.choices(choices))[slice1]
    player = None

    while player not in choices:
        player = input('rock, paper, or scissors?: ')

    if player == computer:
        print('computer: ', computer)
        print('player: ', player)
        print('Tie')

    elif player == "rock":
        if computer == '["paper"]':
            print('computer: ', computer)
            print('player: ', player)
            print('You lose')
        if computer == "scissors":
            print('computer: ', computer)
            print('player: ', player)
            print('You win')
    elif player == "paper":
        if computer == "scissors":
            print('computer: ', computer)
            print('player: ', player)
            print('You lose')
        if computer == "rock":
            print('computer: ', computer)
            print('player: ', player)
            print('You win')
    elif player == "scissors":
        if computer == "rock":
            print('computer: ', computer)
            print('player: ', player)
            print('You lose')
        if computer == "paper":
            print('computer: ', computer)
            print('player: ', player)
            print('You win')

    play_again = input("Play again? y/n: ").lower

    if play_again != "y":
        break

print('Bye!')