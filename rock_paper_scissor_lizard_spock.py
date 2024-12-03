import random

def play():
    while True:
        player = input(
            "Play Rock-Paper-Scissor-Lizard-Spock! Choose:\n"
            "r for Rock, p for Paper, s for Scissor, l for Lizard, sp for Spock:\n> "
        )
        computer = random.choice(['r', 'p', 's', 'l', 'sp'])
        if player == computer:
            print(f"You chose: {player}, computer chose: {computer}. It's a tie! Play again.\n")
        elif player_wins(player, computer):
            print(f"You chose: {player}, computer chose: {computer}. Congratulations, you won!\n")
        else:
            print(f"You chose: {player}, computer chose: {computer}. You lost! Try again.\n")
        if input("Do you want to play again? (y/n):\n> ").lower() != 'y':
            break

def player_wins(player1, player2):
    winning_combinations = {
        's': ['p', 'l'],
        'p': ['r', 'sp'],
        'r': ['l', 's'],
        'l': ['sp', 'p'],
        'sp': ['s', 'r']
    }
    return player2 in winning_combinations.get(player1, [])

play()