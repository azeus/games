import random

def play():
    player = input("play rock-paper-scissor-lizard-spock! choose r for rock, p for paper, s for scissor, l for lizard and sp for spock!\n")
    computer = random.choice(['r','p','s','l','sp'])

    if player == computer:
        return 'you chose : {p} and computer chose :{c} It is a Tie, Play again!\n'.format(p=player,c=computer)

    if player_wins(player, computer):
        return 'you chose : {p} and computer chose :{c} Congratulations, You won! Play again\n'.format(p=player,c=computer)
    
    return 'you chose : {p} and computer chose :{c} You lost!, Play again!\n'.format(p=player,c=computer)

'''
scissors > paper
paper > rock
rock > lizard
lizard > spock
spock > scissors
scissors > lizard
lizard > paper
paper > spock
spock > rock
rock > scissors
'''
def player_wins(player1, player2):
    if (player1 == 's' and player2 == 'p') or (player1 == 'p' and player2 == 'r')\
    or (player1 == 'r' and player2 == 'l') or (player1 == 'l' and player2 == 'sp')\
    or (player1 == 'sp' and player2 == 's') or (player1 == 's' and player2 == 'l')\
    or (player1 == 'l' and player2 == 'p') or (player1 == 'p' and player2 == 'sp')\
    or (player1 == 'sp' and player2 == 'r') or (player1 == 'r' and player2 == 's'):
        return True

print(play())