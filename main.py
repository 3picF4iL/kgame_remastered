'''
Main Game file

Keys Game Remastered
source from KeysGame ND_CW
'''

from movement import Player
from map_generator import Map
from interface_creator import InterfaceCreator
from misc_functions import clsrc
from msvcrt import getch
from variables import *

_map = Map()  # map object created

_map.generate_boards(map_size, symbol, items_to_collect)   # generating map with argument corresponded to the desired map size,
                                    # symbol to collect, amount of the symbols
interface = InterfaceCreator(_map.size_map_od)  # generating interface layout depends of the map size
target_map = _map.generated_map  # creating variable target_map that can be used to make changes by players

player_1 = Player(1, 1, target_map, player_1_avatar)  # player 1 created
player_2 = Player(_map.size_map_od-2, _map.size_map-2, target_map, player_2_avatar)  # player 2 created

moving = {
        53: player_2.move_down,
        56: player_2.move_up,
        52: player_2.move_left,
        54: player_2.move_right,
        115: player_1.move_down,
        119: player_1.move_up,
        97: player_1.move_left,
        100: player_1.move_right
}

while not end_game:
    clsrc()  # clear the console
    interface.print_interface()  # printing interface
    print(_map.generated_map)
    _map.print_map(target_map)  # printing map
    get_key = ord(getch())  # get input key from user keyboard
    if get_key is 27:
        break
    moving[get_key](target_map)
    # if player_1.collision(player_1.x, player_1.y, player_2.x, player_2.y):
    #     print("Collision")
    #     get_key2 = ord(getch())
    interface.p1Points = player_1.points
    interface.p2Points = player_2.points
    if interface.check_score(_map.symbol_amount):
        interface.check_win()
        target_map = _map.generate_boards(map_size, symbol, items_to_collect)
        player_1.respawn(target_map)
        player_2.respawn(target_map)

    print(f"Position X player 2: {player_2.x}\nPosition Y player 2: {player_2.y}")
    print(f"Position X player 1: {player_1.x}\nPosition Y player 1: {player_1.y}")


