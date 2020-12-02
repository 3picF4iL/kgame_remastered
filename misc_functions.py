import os


def clsrc():
    return os.system('cls' if os.name is 'nt' else 'clear')

#def print_board(board):
#    for j