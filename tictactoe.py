# Milestone Project 1: Tic Tac Toe Game

"""
Here are the requirements:

- 2 players should be able to play the game (both sitting at the same computer)
- The board should be printed out every time a player makes a move
- You should be able to accept input of the player position and then place a symbol on the board

Gameplan:

1. Ask player 1 if they want to be X or O
    - Start with random coinflip, heads = player 1, tails = player 2
    - Take in their input and assign accordingly to player 1, player 2 gets the opposite
    - Must check to make sure user inputs correct value
    - print('Player 1 will go first) after selection

2. Ask user if they are ready to play (Enter yes or no)
3. Ask user to choose position on board (1-9)
    - must be 1-9, position must be free, if position ends game, end the game.
    - taking turns is within a while loop
"""
import random

from sqlalchemy import true


player1 = ''
player2 = ''
player_start = ''
board = [1,2,3,4,5,6,7,8,9]
previous_player = ''

# Defines and prints the game board
def game_board(board):
    print('   |   |   ')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('   |   |   ')
    print('\n')

# Randomly select the player who starts
def player_pick():
    if random.randrange(2) == 1:
        player_start = 'Player 2'
    else:
        player_start = 'Player 1'

    return player_start

# Starts the game, randomly determines a player to start, then asks player to choose if
# they want to be X or O.
def game_start(player1,player2,player_start):
    choice = 'wrong'

    while choice not in ['X','O']:

        choice = input(f"{player_start}: Do you want to be X or O? ").upper()

        if choice not in ['X','O']:
            print('Sorry, invalid choice! Please enter only X or O.\n')
        else:
            if player_start == 'Player 1' and choice == 'X':
                player1 = 'X'
                player2 = 'O'

            elif player_start == 'Player 2' and choice == 'O':
                player1 = 'X'
                player2 = 'O'
            
            else:
                player1 = 'O'
                player2 = 'X'

            print(f'{player_start} will go first.\n')
    
    return player1,player2

def check_stale(board):
    return any(num for num in board if isinstance(num,int))

# Checks to see if there is 3 in a row, if there is the game ends. If there are still open spaces, continue the game.
def win_check(board,player_start,player1,player2):
    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[0] == 'O' and board[1] == 'O' and board[2] == 'O'):
        print('Congratulations! You have won the game!')
        return True
    elif (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O'):
        print('Congratulations! You have won the game!')
        return True
    elif (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O'):
        print('Congratulations! You have won the game!')
        return True
    elif (board[6] == 'X' and board[3] == 'X' and board[0] == 'X') or (board[6] == 'O' and board[3] == 'O' and board[0] == 'O'):
        print('Congratulations! You have won the game!')
        return True
    elif (board[7] == 'X' and board[4] == 'X' and board[1] == 'X') or (board[7] == 'O' and board[4] == 'O' and board[1] == 'O'):
        print('Congratulations! You have won the game!')
        return True
    elif (board[8] == 'X' and board[5] == 'X' and board[2] == 'X') or (board[8] == 'O' and board[5] == 'O' and board[2] == 'O'):
        print('Congratulations! You have won the game!')
        return True
    elif (board[6] == 'X' and board[4] == 'X' and board[2] == 'X') or (board[6] == 'O' and board[4] == 'O' and board[2] == 'O'):
        print('Congratulations! You have won the game!')
        return True
    elif (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (board[0] == 'O' and board[4] == 'O' and board[8] == 'O'):
        print('Congratulations! You have won the game!')
        return True
    else:
        return False

def start(board,player1,player2,player_start):

    while True:
        choice = 'wrong'
        if player_start == 'Player 1':
            while choice not in range(1,10):
                choice = int(input('Player 1: Choose your next position: (1-9)\n'))
                
                if choice not in range(1,10):
                    print('Sorry, invalid choice! Please choose a nunmber between 1 and 9.')
                elif board[choice - 1] == 'X' or board[choice - 1] == 'O':
                    print('Sorry, that spot has already been filled! Please choose another number.')
                    continue

                board[choice - 1] = player1
                player_start = 'Player 2'
        else:
            while choice not in range(1,10):
                choice = int(input('Player 2: Choose your next position: (1-9)\n'))

                if choice not in range(1,10):
                    print('Sorry, invalid choice! Please choose a nunmber between 1 and 9.')
                elif board[choice - 1] == 'X' or board[choice - 1] == 'O':
                    print('Sorry, that spot has already been filled! Please choose another number.')
                    continue
                
                board[choice - 1] = player2
                player_start = 'Player 1'

        game_board(board)

        if win_check(board,player_start,player1,player2):
            return False

        if check_stale(board) is False:
            print('Stalemate!')
            return False



def ready(player_start,player1,player2):
    choice = 'wrong'

    while choice not in ['YES','NO']:
        choice = input('Are you ready to play? Enter Yes or No.\n').upper()
        print('\n')

        if choice == 'YES':
            start(board,player1,player2,player_start)
        elif choice == 'NO':
            return 'NO'
        else:
            print('Please enter a valid response\n')




#Game functions:

print('Welcome to Tic Tac Toe!\n')
player_start = player_pick()
player1,player2 = game_start(player1,player2,player_start)
ready(player_start,player1,player2)