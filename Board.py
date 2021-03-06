import random


class Board:
    """
    A class used to construct and represent the Board

    ...

    Attributes
    ----------
    number_of_rows : int
    number_of_colors : int
    board:

    Methods
    -------
    create_board()
    print_board()
    get_board()
    """

    def __init__(self, number_of_rows: int, number_of_colors: int):

        self.number_of_rows = number_of_rows
        self.number_of_colors = number_of_colors
        self.board = []
        self.seed = 30
        self.create_board()
        
    def create_board(self,)->None:
        """
        Create board with the given rows and colors.
        """
        random.seed(self.seed)
        for row in range(self.number_of_rows):
            self.board.append([])
            for column in range(self.number_of_rows):
                self.board[row].append(
                    random.randint(
                        0, self.number_of_colors - 1))
        print("\nBoard created of {}x{} with {} colors".format(self.number_of_rows, self.number_of_rows, self.number_of_colors))

    def get_board(self,)->list:
        """
        returns the created board.
        """
        return self.board

    def print_board(self, text:str = "Showing Board.")->None:
        """
        Prints the board.
        """
        print(text)
        for row in self.board:
            print(' '.join(map(str, row)))
