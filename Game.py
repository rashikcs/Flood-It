from Board import Board
from copy import deepcopy
from Player import FloodItPlayerSimulator

class Game:
    """
    An abstract class used to represent the Game.
    Need to implement play_game() method.

    """

    @classmethod
    def play_game(self,):
        raise NotImplementedError

class FloodItGame(Game):
    """
    A class used to manage the flood-it game -> color the board of all
    connected tiles to the origin.
    ...

    Attributes
    ----------
    player : FloodItPlayerSimulator
    board_obj : Board
    name : str

    Methods
    -------
    identify_connected_tile()
    change_neighbour_colors()
    play_turn()
    get_connected_tiles()
    play_game() *** abstract method
    print_result()
    """

    def __init__(self, name:str = "Flood-It",):
        self.name = name
        print("{} game selected!!!".format(name))

    def init_game(self, number_of_rows: int = 5,
                        number_of_colors: int = 4,
                        player_name: str = "Smart Mouth", 
                        minimum_turns: int = 20,
                        skip_player_save:bool = False)->None:
        """
        Initializes board and player.
        Args:

            number_of_rows:int -> Value for the square matrix: used as board
            number_of_colors:int -> Value for the num of colors in the board
            player_name:str -> Player name
            minimum_turns:int -> minimum turns available for the player
            skip_player_save:bool -> True if coming from unit test
        """

        self.board_obj = Board(number_of_rows, number_of_colors)
        print("{} Game initialized!".format(self.name))
        self.board_obj.print_board()

        self.player = FloodItPlayerSimulator(player_name)
        self.player.init_player(minimum_turns, skip_player_save)

    def identify_connected_tile(self, x:int, y:int, matrix: list, adjacent_tiles:int, chosen_color:int, queue:set)->None:
        """
        Identifies the connected tiles and add it to queue to visit.
        Args:

            x:int -> x pos of the adjacent tiles of origin
            y:int -> y pos of the adjacent tiles of origin
            matrix:int -> Input grid/board
            chosen_color:int -> choosen color.
            queue:set -> queue of the tiles to visit
        """

        if matrix[x][y] == adjacent_tiles:
            matrix[x][y] = chosen_color
            queue.add((x, y))

    def change_neighbour_colors(self,
                      x: int = 0,
                      y: int = 0,
                      origin_color = None,
                      visited_tiles: list = [],
                      matrix: list = None,
                      chosen_color: int = 3)->tuple:
        """Returns the colored board and all visited nodes of the board.

        This function changes colors of the
        chosen adjacent tiles of the origin
        with the chosen color and returns
        the updated board.

        Args:

            x:int -> x pos of the adjacent tiles of origin
            y:int -> y pos of the adjacent tiles of origin
            visited_tiles:list -> list of positions of the visited nodes
            matrix:int -> Input grid/board
            chosen_color:int -> choosen color.

        Returns:

            matrix:list -> updated board
            visited_tiles:list -> A list with visited tiles
            origin_color:int: Initial color of the origin

        """

        queue = {(x, y)}

        if not matrix:
            matrix = deepcopy(self.board_obj.board[:])
            
        if not origin_color:
            origin_color = matrix[0][0]

        matrix[0][0] = chosen_color
        adjacent_tiles = matrix[x][y]

        while queue:
            x, y = queue.pop()

            if (x, y) not in visited_tiles:
                visited_tiles.append((x, y))

            if x + 1 < len(matrix) and \
               (x + 1, y) not in visited_tiles and \
               (x + 1, y) not in queue:

                self.identify_connected_tile(x+1, y, matrix, adjacent_tiles, chosen_color, queue)

            if x - 1 >= 0 and \
               (x - 1, y) not in visited_tiles and \
               (x - 1, y) not in queue:

                self.identify_connected_tile(x-1, y, matrix, adjacent_tiles, chosen_color, queue)


            if y - 1 >= 0 and \
               (x, y - 1) not in visited_tiles and \
               (x, y - 1) not in queue:

                self.identify_connected_tile(x, y-1, matrix, adjacent_tiles, chosen_color, queue)

            if y + 1 < len(matrix[0]) and \
               (x, y + 1) not in visited_tiles and \
               (x, y + 1) not in queue:

                self.identify_connected_tile(x, y+1, matrix, adjacent_tiles, chosen_color, queue)
                    
            if adjacent_tiles == origin_color:
                matrix[x][y] = chosen_color

        return matrix, visited_tiles, origin_color

    def play_turn(self, chosen_color:int)->list:
        """
        Returns the board according to the changes of the chosen color

        Args:

            chosen_color:int -> choosen color.

        Returns:

            colored_board:list: updated board
        """
        colored_board, visited, origin_color = self.change_neighbour_colors(x=0,
                                                                  y=1,
                                                                  visited_tiles=[],
                                                                  chosen_color=chosen_color)
        colored_board, _, _ = self.change_neighbour_colors(x=1,
                                                 y=0,
                                                 origin_color=origin_color,
                                                 visited_tiles=visited,
                                                 matrix=colored_board,
                                                 chosen_color=chosen_color)
        return colored_board

    def get_connected_tiles(self, x=0, y=0, matrix=[]) -> int:
        """Returns the count of connected tiles from origin.

        This function takes the board as a matrix, and
        calculates the total tiles connected to the origin.

        Args:

            x:int -> x pos of the adjacent tiles of origin
            y:int -> y pos of the adjacent tiles of origin
            visited_tiles:list -> list of positions of the visited nodes
            matrix:int -> Input grid/board

        Returns:

            tile_count:int -> Count of the tiles connected to origin

        """

        queue = {(x, y)}
        tile_count = 1
        visited_nodes = []
        while queue:
            x, y = queue.pop()
            visited_nodes.append((x, y))
            if x + 1 < len(matrix) and \
               (x + 1, y) not in visited_nodes and \
               (x + 1, y) not in queue:

                if matrix[x + 1][y] == matrix[x][y]:
                    tile_count += 1
                    queue.add((x + 1, y))

            if x - 1 >= 0 and \
               (x - 1, y) not in visited_nodes and \
               (x - 1, y) not in queue:

                if matrix[x - 1][y] == matrix[x][y]:
                    tile_count += 1
                    queue.add((x - 1, y))

            if y - 1 >= 0 and \
               (x, y - 1) not in visited_nodes and \
               (x, y - 1) not in queue:

                if matrix[x][y - 1] == matrix[x][y]:
                    tile_count += 1
                    queue.add((x, y - 1))

            if y + 1 < len(matrix[0]) and \
               (x, y + 1) not in visited_nodes and \
               (x, y + 1) not in queue:

                if matrix[x][y + 1] == matrix[x][y]:
                    tile_count += 1
                    queue.add((x, y + 1))
                    
        return tile_count

    def play_game(self,)->int:
        """Colors the board choosing the best available choice by iterating all available colors.

        This function iteratively finds out the color resulting the maximum tile conection
        and stops when all the tiles colored using the same color.

        Returns:

            turn_count:list: turns needed to end the game

        """
        tiles_connected = 0
        turn_count = 0

        while tiles_connected != self.board_obj.number_of_rows**2:
            chosen_color, colors_with_connected_tiles = self.player.select_color(self.board_obj,
                                                                                 self.change_neighbour_colors,
                                                                                 self.get_connected_tiles)
            self.board_obj.board = self.play_turn(chosen_color)
            tiles_connected = colors_with_connected_tiles[chosen_color]
            turn_count += 1

            print(
                "\nTurn {}. Colored board with index {} and maximum connection {}.".format(
                    turn_count,
                    chosen_color,
                    tiles_connected))

            self.board_obj.print_board()

            if turn_count > self.player.minimum_turns:
                break


        print("Total Turns made in the game: ", turn_count)
        self.print_result(turn_count)

        return turn_count

    def print_result(self, minimum_turn_needed)->None:
        """
        Print result of the game.
        Args:
            minimum_turn_needed:int
        """
        
        if minimum_turn_needed <= self.player.minimum_turns:
            print("Player:{} wins the game!!".format(self.player.name))
        else:
            print("Player:{} loses!!".format(self.player.name))
