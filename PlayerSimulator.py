from Board import Board

from FloodItGame import FloodItGame


class PlayerSimulator:
    """
    A class used to play the game as a player

    ...

    Attributes
    ----------
    minimum_turns : int
    flood_it_game : FloodItGame

    Methods
    -------
    init_game()
    play_flood_it()
    """

    def __init__(self,):

        self.minimum_turns = None
        self.flood_it_game = None

    def init_game(self, flood_it_game: FloodItGame, minimum_turns: int):

        self.minimum_turns = minimum_turns
        self.flood_it_game = flood_it_game

        print("New Game Initialized!")

    def get_result(self, minimum_turn_needed):

        if minimum_turn_needed <= self.minimum_turns:
            print("Player wins the game!!")
        else:
            print("Player loses!!")

    def play_flood_it(self,):
        """Colors the board choosing the best available choice by iterating all available colors.

        This function iteratively finds out the color resulting the maximum tile conection
        and stops when all the tiles colored using the same color.


        """
        tiles_connected = 0
        minimum_turn_needed = 0

        while tiles_connected != self.flood_it_game.number_of_rows * \
                self.flood_it_game.number_of_rows:
            chosen_color, colors_with_connected_tiles = self.flood_it_game.select_color()

            colored_board, visited, origin_color = self.flood_it_game.change_colors(
                x=0, y=1, visited_tiles=[], chosen_color=chosen_color)
            colored_board, _, _ = self.flood_it_game.change_colors(x=1,
                                                                   y=0,
                                                                   origin_color=origin_color,
                                                                   visited_tiles=visited,
                                                                   matrix=colored_board,
                                                                   chosen_color=chosen_color)
            minimum_turn_needed += 1
            self.flood_it_game.board = colored_board
            tiles_connected = colors_with_connected_tiles[chosen_color]
            print(
                "\nTurn {}. Colored board with index {} and maximum connection {}.".format(
                    minimum_turn_needed,
                    chosen_color,
                    tiles_connected))
            self.flood_it_game.print_board()

        print(
            "Turns needed to finish the game: ",
            minimum_turn_needed)
        self.get_result(minimum_turn_needed)

        return minimum_turn_needed
