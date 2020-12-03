'''
Created on 17 kwi 2018

@author: JakubF
@refactor: KamilG
'''

class InterfaceCreator(object):
    '''
    Class generating an interface with results

    general use:
        create class instantiation
        change points with points_increase/decrease methods

        increase result with score_increase
        return string with interface with:
            return_interface

        and print it with:
            print_interface

        The line functions are used in the return_interface method
        each of them print a different part
    '''

    def __init__(self, board_size, board_symbol="*"):

        '''
        Constructor
        Take 2 parameters
        :param:
            board_size variable store how many chars will be print in one line,
            has to be converted to int

            board_symbol variable store the symbol that will be used to print lines,
            has to be shorter than board_size/2 - 6(the widest interface point)

            private variables are used to keep this information

        '''
        try:
            self._board_size = int(board_size)
            self._board_symbol = str(board_symbol)
            if self._board_size < (len(self._board_symbol) * 2 + 6):
                raise AssertionError
            self.set_up_int()
        except ValueError:
            print("The size of the board should be convertable to int")
            raise ValueError
        except AssertionError:
            print("The length of the symbol cannot be lengthier than the size of the map side")
            raise AssertionError

    def set_up_int(self):
        '''
        sets up the initial statistics
        players points p1Points,p2Points
        general result score
        '''
        self.p1Points = 0
        self.p2Points = 0
        self.score = "|"

    def points_increase(self, side):
        '''
        increases Player points by 1
        :param:
            side :bool
        Player1 if TRUE
        Player2 if FALSE
        '''
        if side:
            self.p1Points += 1
        else:
            self.p2Points += 1

    def points_decrease(self, side):
        '''
        decreases Player points by 1 if they are greater than 0
        :param:
            side :bool
        Player1 if TRUE
        Player2 if FALSE
        '''
        if side and self.p1Points > 0:
            self.p1Points -= 1
        elif side is False and self.p2Points > 0:
            self.p2Points -= 1

    def score_increase(self, side):
        '''
        increases the general result of the Player by 1 and then resets points
        both of the Players
        result is presented with 'star' symbol on both sides
        :param:
            side :bool
        Player1 if TRUE
        Player2 if FALSE
        '''
        if side:
            self.score = "*" + self.score
        else:
            self.score = self.score + "*"
        self.p2Points = 0
        self.p1Points = 0

    def return_interface(self):
        '''
        function returns string value created with other line functions
        present the general interface layout
        '''
        string_interface = self.line_breaker()
        string_interface += self.line_sides()
        string_interface += self.line_score()
        string_interface += self.line_sides()
        string_interface += self.line_points()
        string_interface += self.line_sides()
        string_interface += self.line_breaker()
        return string_interface

    def print_interface(self):
        '''
        functions printing interface layout
        calls a function that creates an interface
        '''
        print(self.return_interface())

    def line_breaker(self):
        '''
        function printing interface
        creating line
        :returns string
        '''
        text = self._board_symbol * self._board_size
        return text[:self._board_size] + "\n"

    def line_sides(self):
        '''
        funtions printing interface
        creates sides walls of the interface
        :returns string
        '''
        return self._board_symbol + (
                    " " * (self._board_size - 2 * len(self._board_symbol))) + self._board_symbol + "\n"

    def line_score(self):
        '''
        funtions printing interface
        creating 2 lines space from the game result
        :returns string
        '''
        text = self._board_symbol + "SCORE".center(self._board_size - 2 * len(self._board_symbol),
                                                     ' ') + self._board_symbol + "\n"
        text += self._board_symbol + self.score.center(self._board_size - 2 * len(self._board_symbol),
                                                         ' ') + self._board_symbol + "\n"
        return text

    def line_points(self):
        '''
        funtions printing interface
        creating 2 lines space from the game points
        :returns string
        '''
        text = self._board_symbol + "P1" + (
                    " " * (self._board_size - 4 - 2 * len(self._board_symbol))) + "P2" + self._board_symbol + "\n"
        text += self._board_symbol + str(self.p1Points).zfill(3) + (
                    " " * (self._board_size - 6 - 2 * len(self._board_symbol))) + str(self.p2Points).zfill(
            3) + self._board_symbol + "\n"

        return text