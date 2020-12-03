import os


def clsrc():
    return os.system('cls' if os.name is 'nt' else 'clear')
