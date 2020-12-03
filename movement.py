'''
Class movement
'''

class Player:

    def __init__(self, pos_x, pos_y, board, avatar):
        self.x = pos_y
        self.y = pos_x
        self.avatar = avatar
        board[(pos_y, pos_x)] = avatar

        self.points = 0
        self.result = 0

    def move_up(self, board):
        print(self.x)
        print(self.y)
        print(board[(self.x-1, self.y)])
        if board[(self.x - 1, self.y)] in (" ", "k"):
            board[(self.x, self.y)] = " "
            board[(self.x-1, self.y)] = self.avatar
            self.x -= 1
            if board[(self.x - 1, self.y)] == "k":
                self.points += 1
        return print("UP")

    def move_down(self, board):
        print(self.x)
        print(self.y)
        print(board[(self.x + 1, self.y)])
        if board[(self.x + 1, self.y)] in (" ", "k"):
            board[(self.x, self.y)] = " "
            board[(self.x + 1, self.y)] = self.avatar
            self.x += 1
            if board[(self.x + 1, self.y)] == "k":
                self.points += 1
        return print("DOWN")

    def move_left(self, board):
        print(self.x)
        print(self.y)
        print(board[(self.x, self.y - 1)])
        if board[(self.x, self.y - 1)] in (" ", "k"):
            board[(self.x, self.y)] = " "
            board[(self.x, self.y - 1)] = self.avatar
            self.y -= 1
            if board[(self.x, self.y - 1)] == "k":
                self.points += 1
        return print("LEFT")

    def move_right(self, board):
        print(self.x)
        print(self.y)
        print(board[(self.x, self.y + 1)])
        if board[(self.x, self.y + 1)] in (" ", "k"):
            board[(self.x, self.y)] = " "
            board[(self.x, self.y + 1)] = self.avatar
            self.y += 1
            if board[(self.x, self.y + 1)] == "k":
                self.points += 1
        return print("RIGHT")
