'''
Simple ASCII Map generator. Using part of the Prim's algorithm implementation from https://gist.github.com/gmalmquist/.
'''
import random


class Map(object):

    EMPTY = ' '
    WALL = '#'

    def neighbor_cell(self, cell):
        '''
        :param cell: cell coordinates
        :return: generated coordinates of the cell's neighbors
        '''
        i, j = cell
        for (y, x) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            yield (i+y, j+x), (i+2*y, j+2*x)

    def generate_boards(self, size):
        '''
        :param size: size of the map, prefered odd number for
        :return:
        '''
        max_height = size
        max_width = int(float(size * 1.6))

        board = {}
        space_cells = set()
        connected_cells = set()
        walls_cells = set()

        # creating walls
        for j in range(0, max_height):
            for i in range(0, max_width):
                if (j == max_height-1 and i >= 0) or (i == max_width-1 and j >= 0) or i == 0 or i == max_width-1 or j == 0 or j == max_height-1:
                    board[(j, i)] = self.WALL

        board_length_rows = max_height - 1
        board_length_columns = max_width

        # creating grid required for Prim's algorithm
        for j in range(1, board_length_rows):
            for i in range(1, board_length_columns):
                if j % 2 == 0 or i % 2 == 0:
                    board[(j, i)] = self.WALL
                else:
                    board[(j, i)] = self.EMPTY

        # all_board = ''
        # for j in range(0, board_length_rows):
        #     for i in range(0, board_length_columns):
        #         if i != board_length_columns-1:
        #             all_board += (str(board[(j, i)]))
        #         else:
        #             all_board += (str(board[(j, i)]+'\n'))

        #return print(all_board)

        for i in range(1, board_length_rows-1):
            for j in range(1, board_length_columns-1):
                if board[(i, j)] == self.EMPTY:
                    space_cells.add((i, j))
                if board[(i, j)] == self.WALL:
                    walls_cells.add((i, j))
        lines = []
        connected_cells.add((1, 1))
        # using non-optimized Prim's algorithm
        while len(connected_cells) < len(space_cells):
            doA, doB = None, None
            cns = list(connected_cells)
            random.shuffle(cns)
            for (i, j) in cns:
                if doA is not None: break
                for A, B in self.neighbor_cell((i, j)):
                    if A not in walls_cells:
                        continue
                    if (B not in space_cells) or (B in connected_cells):
                        continue
                    doA, doB = A, B
                    break
            A, B = doA, doB
            board[A] = self.EMPTY
            walls_cells.remove(A)
            space_cells.add(A)
            connected_cells.add(A)
            connected_cells.add(B)
        # put all lines togather
        for i in range(board_length_rows):
            lines.append(''.join(board[(i, j)] for j in range(board_length_columns)))

        return lines
