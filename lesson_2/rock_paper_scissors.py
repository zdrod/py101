# Rock, Paper, (S)cissors
""" A game everyone knows and loves. """

import random

VALID_CHOICES = {
    'r': '(r)ock',
    'p': '(p)aper',
    's': '(s)cissors',
    'l': '(l)izard',
    'c': '(c)ommander spock'
}

last_printed_string = ""

def prompt(message):
    """adds formatting to messages and stores message"""
    global last_printed_string
    print(f'==> {message}')
    last_printed_string = message

def get_clean_choice():
    """Gets a valid choice and cleans up formatting"""
    while True:
        prompt(f'Choose one: {', '.join(VALID_CHOICES.values())}')
        player_pick = input()

        while player_pick not in VALID_CHOICES:
            prompt("That's not a valid choice.")
            player_pick = input()
        player_pick = VALID_CHOICES[player_pick]
        return player_pick.replace("(", "").replace(")", "")

def display_winner(player, computer):  #Could  change to dict, also could return a value on win/lose/tie
    """Takes input from player and computer and prints a script"""
    if player == 'rock' and computer in ('scissors', 'lizard'):
        prompt(f'{choice} crushes {computer_choice}. You win!')
    elif player == 'paper' and computer in ('rock', 'commander spock'):
        prompt(f'{choice} beats {computer_choice}. You win!')
    elif player == 'scissors' and computer in ('paper', 'lizard'):
        prompt(f'{choice} cuts {computer_choice}. You win!')
    elif player == 'commander spock' and computer in ('scissors', 'rock'):
        prompt(f'{choice} melts {computer_choice}, with a laser. You win!')
    elif player == 'lizard' and computer in ('commander spock', 'paper'):
        prompt(f'{choice} beats {computer_choice}. You win!')
    elif player == computer:
        prompt("It's a tie!")
    else:
        prompt("You lose!")

while True:
    score_computer = 0
    score_player = 0
    while score_player < 3 and score_computer < 3:

        choice = get_clean_choice()

        computer_choice_dirty = random.choice(list(VALID_CHOICES.values()))
        computer_choice = computer_choice_dirty.replace("(", "").replace(")", "")

        prompt(f'You chose {choice}, computer chose {computer_choice}')

        display_winner(choice, computer_choice)

        if last_printed_string[-4:] == 'win!':
            score_player += 1
        elif last_printed_string[-5:] == 'lose!':
            score_computer += 1

        prompt(f'The score is Player:{score_player}, Computer:{score_computer}')
        prompt("")

    if score_player > score_computer:
        prompt('You are the grand champ!')
    else:
        prompt('The computer is the grand champ!')

    prompt('Do you want to play again? (y/n)?')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()
    if answer[0] == 'n':
        break
