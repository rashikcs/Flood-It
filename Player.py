from Board import Board


class Player:
    """
    A class used to represent players

    ...

    Attributes
    ----------
    name : str

    Methods
    -------
    select_color()
    """
    def __init__(self, name:str = "SmartPlayer"):
        self.name = name

    @classmethod
    def init_player(self,):
        raise NotImplementedError


class FloodItPlayerSimulator(Player):
    """
    A class used to represent the flood it player.

    ...

    Attributes
    ----------
    minimum_turns : int
    name : str

    Methods
    -------
    select_color()
    """

    def __init__(self, name:str = "Smart Mouth"):
        Player.__init__(self, name)

    def init_player(self, minimum_turns: int = 20)->None:

        self.minimum_turns = minimum_turns
        print("\n{} player initialized.\nMinimum Turns: {}".format(self.name, self.minimum_turns))

    def select_color(self, board_obj: Board, change_neighbour_colors, get_connected_tiles)->tuple:
        """Returns the index of the color resulted the maximum connection
           and associated array holding the connection with each color.

        This function finds out the color resulting the maximum tile conection
        and returns the values.

        Args:

            board_obj:Board -> Instance of Board Class
            change_neighbour_colors -> change_neighbour_colors() method of FloodItGame class
            get_connected_tiles -> get_connected_tiles() method of FloodItGame class

        Returns:
            chosen color:int -> Colors resulting maximum connection
            colors_with_connected_tiles:list -> colors and associated number of connections

        """
        colors_with_connected_tiles = [0] * board_obj.number_of_colors

        for i in range(0, board_obj.number_of_colors):

            colored_board = []

            colored_board, visited, origin_color = change_neighbour_colors(x=0,
                                                        y=1,
                                                        visited_tiles=[],
                                                        matrix=None,
                                                        chosen_color=i)

            colored_board, _, _ = change_neighbour_colors(x=1,
                                                  y=0,
                                                  visited_tiles=visited,
                                                  origin_color = origin_color,
                                                  matrix=colored_board,
                                                  chosen_color=i)

            colors_with_connected_tiles[i] = get_connected_tiles(
                x=0, y=0, matrix=colored_board)

        return colors_with_connected_tiles.index(
            max(colors_with_connected_tiles)), colors_with_connected_tiles

