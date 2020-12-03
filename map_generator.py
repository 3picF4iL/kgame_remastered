'''
Simple ASCII Map generator. Using part of the Prim's algorithm implementation from https://gist.github.com/gmalmquist/.
'''
import random


class Map(object):

    EMPTY = ' '
    WALL = '#'
    generated_map = {}
    size_map = 0
    size_map_od = 0  # additional var for other dimension
    generated_map_string = ""

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
        :return: saved generated map to the global var
        '''
        if size % 2 == 0:
            self.size_map = size+1  # preventing from 'double walled' borders
        else:
            self.size_map = size

        max_height = self.size_map

        max_width = int(float(size * 1.6))
        if max_width % 2 == 0:
            max_width += 1  # preventing from 'double walled' borders

        self.size_map_od = max_width  # updating global var

        board = {}
        space_cells = set()
        connected_cells = set()
        walls_cells = set()

        # creating walls
        for j in range(0, max_height):
            for i in range(0, max_width):
                if (j == max_height - 1 and i >= 0) or (i == max_width - 1 and j >= 0) or i == 0 or i == max_width - 1 or j == 0 or j == max_height - 1:
                    board[(j, i)] = self.WALL

        board_length_rows = max_height - 1
        board_length_columns = max_width - 1

        # creating grid required for Prim's algorithm
        for j in range(1, board_length_rows):
            for i in range(1, board_length_columns):
                if (j % 2 == 0 and j != board_length_rows % 2) or (i % 2 == 0 and i != board_length_rows % 2):
                    board[(j, i)] = self.WALL
                else:
                    board[(j, i)] = self.EMPTY

        # checking each cell for EMPTY or a WALL and adding coordinates to separate set
        for i in range(1, board_length_rows):
            for j in range(1, board_length_columns):
                if board[(i, j)] == self.EMPTY:
                    space_cells.add((i, j))
                if board[(i, j)] == self.WALL:
                    walls_cells.add((i, j))

        connected_cells.add((1, 1))
        # using non-optimized Prim's algorithm to make maze
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

        self.generated_map = board
        # saving generated map to variable

    def generate_string_map(self, read_map):
        lines = []
        for i in range(self.size_map):
            lines.append(''.join(read_map[(i, j)] for j in range(self.size_map_od)))
        self.generated_map_string = lines

    def print_map(self, read_map=None):
        if read_map is None:
            read_map = self.generated_map
        self.generate_string_map(read_map)
        string_map = self.generated_map_string
        print('\n'.join(string_map))
