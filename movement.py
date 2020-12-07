'''
Class movement
'''

import math


class Player:

    key = False

    def __init__(self, pos_x, pos_y, board, avatar):
        self.x = pos_y
        self.y = pos_x
        self.x_init = pos_y
        self.y_init = pos_x
        self.avatar = avatar
        self.board = board
        board[(pos_y, pos_x)] = avatar

        self.points = 0

    def move_up(self, board):
        if board[(self.x - 1, self.y)] in (" ", "k"):
            if board[(self.x - 1, self.y)] == "k": self.key = True
            board[(self.x, self.y)] = " "
            board[(self.x-1, self.y)] = self.avatar
            self.x -= 1
            if self.key:
                self.points += 1
                self.key = False
            return True
        else:
            return False

    def move_down(self, board):
        if board[(self.x + 1, self.y)] in (" ", "k"):
            if board[(self.x + 1, self.y)] == "k": self.key = True
            board[(self.x, self.y)] = " "
            board[(self.x + 1, self.y)] = self.avatar
            self.x += 1
            if self.key:
                self.points += 1
                self.key = False
            return True
        else:
            return False

    def move_left(self, board):
        if board[(self.x, self.y - 1)] in (" ", "k"):
            if board[(self.x, self.y - 1)] == "k": self.key = True
            board[(self.x, self.y)] = " "
            board[(self.x, self.y - 1)] = self.avatar
            self.y -= 1
            if self.key:
                self.points += 1
                self.key = False
            return True
        else:
            return False

    def move_right(self, board):
        if board[(self.x, self.y + 1)] in (" ", "k"):
            if board[(self.x, self.y + 1)] == "k": self.key = True
            board[(self.x, self.y)] = " "
            board[(self.x, self.y + 1)] = self.avatar
            self.y += 1
            if self.key:
                self.points += 1
                self.key = False
            return True
        else:
            return False

    def collision(self, x1, y1, x2, y2):
        try:
            if (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)) <= 1:  #
                return True
            else:
                return False
        except TypeError:
            print("Incorrect type of forwarded params of the collision method")

    def respawn(self, board):
        board[(self.x, self.y)] = ' '
        board[(self.x_init, self.y_init)] = self.avatar
        self.x = self.x_init
        self.y = self.y_init
        self.points = 0

