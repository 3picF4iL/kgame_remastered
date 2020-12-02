'''
Main Game file

Keys Game Remastered
source from KeysGame ND_CW
'''

from movement import *
from map_generator import *
from misc_functions import *
from msvcrt import getch

player_1 = Player()
_map = Map().generate_boards(32)
end_game = False
#_map.generate_walls(generated_map)
print('\n'.join(_map))
print('\n')
print('\n'.join(Map().generate_boards(16)))

# while not end_game:
#     clsrc()
#
#     get_key = ord(getch())
#
#     if get_key is 53:
#         player_1.move_down()
#     elif get_key is 56:
#         player_1.move_up()
#     elif get_key is 52:
#         player_1.move_left()
#     elif get_key is 54:
#         player_1.move_right()
#     elif get_key is 27:
#         break