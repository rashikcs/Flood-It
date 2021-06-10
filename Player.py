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
    player_exists()
    add_player()
    """
    def __init__(self, name:str = "SmartPlayer"):
        self.name = name

    def player_exists(self, name:str, player_list:list)->bool:
        """This function checks if the name already exists in the
           db/players.txt: used as a db.

        Args:

            name:str
            player_list:list -> existing player names in the files
        
        Return:

            bool

        """      
        if name.lower()+"\n" in player_list:
            return True
        else:
            False

    def add_player(self, name:str, skip_player_save:bool = False)->None:
        """Adds player to the db/players.txt file

        Args:

            name:str
            skip_player_save:bool -> True if coming from unit test
        """ 
        players_file = open("db/players.txt" , "r+")
        player_list = list(map(str.lower,players_file.readlines()))

        if self.player_exists(name, player_list):
            raise ValueError("Name '{}' exists already!!!".format(name))
        else:
            if not skip_player_save:
                players_file.write(name+"\n")
            self.name = name
        players_file.close()

    @classmethod
    def init_player(self,):
        raise NotImplementedError


class FloodItPlayerSimulator(Player):
    """
    A class used to represent the flood-it player and select color in each turn.

    ...

    Attributes
    ----------
    minimum_turns : int
    name : str

    Methods
    -------
    select_color()
    """

    def __init__(self, name:str = "Smart Mouth", minimum_turns: int = 20):
        Player.__init__(self, name)
        #self.init_player(minimum_turns)

    def init_player(self, minimum_turns:int, skip_player_save:bool = False)->None:
        """This function initializes player name and minimum turns for the game

        Args:

            minimum_turns:int
            skip_player_save:bool -> True if coming from unit test

        """        
        self.minimum_turns = minimum_turns
        self.add_player(self.name, skip_player_save)

        print("\nPlayer: {} initialized.\nMinimum Turns: {}".format(self.name, self.minimum_turns))

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

