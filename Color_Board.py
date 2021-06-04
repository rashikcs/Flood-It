from Board import Board
from copy import deepcopy

class Color_Board(Board):
    """
    A class used to color the board with an objective
    of minimum turns to color the whole board.
    ...

    Attributes
    ----------
    minimum_turn_needed : int

    board:

    Methods
    -------
    change_colors()
    get_connected_tiles()
    select_color()
    start_game()
    """

    def __init__(self, number_of_rows: int, number_of_colors: int):
        Board.__init__(self, number_of_rows, number_of_colors)
        Board.create_board(self,)

    def get_connected_tiles(self, x=0, y=0, matrix=[]) -> int:
        """Returns the count of connected tiles till origin.

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

    def change_colors(self,
                      x: int = 0,
                      y: int = 0,
                      origin_color = None,
                      visited_tiles: list = [],
                      matrix: list = None,
                      chosen_color: int = 3):
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
        connected_neighbours = 1

        if not matrix:
            matrix = deepcopy(self.board[:])
            
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

                if matrix[x + 1][y] == adjacent_tiles:
                    matrix[x][y] = chosen_color
                    matrix[x + 1][y] = chosen_color
                    queue.add((x + 1, y))

            if x - 1 >= 0 and \
               (x - 1, y) not in visited_tiles and \
               (x - 1, y) not in queue:

                if matrix[x - 1][y] == adjacent_tiles:
                    matrix[x][y] = chosen_color
                    matrix[x - 1][y] = chosen_color

                    if matrix[x - 1][y] == adjacent_tiles:
                        connected_neighbours += 1
                    queue.add((x - 1, y))

            if y - 1 >= 0 and \
               (x, y - 1) not in visited_tiles and \
               (x, y - 1) not in queue:

                if matrix[x][y - 1] == adjacent_tiles:
                    matrix[x][y] = chosen_color
                    matrix[x][y - 1] = chosen_color
                    queue.add((x, y - 1))

            if y + 1 < len(matrix[0]) and \
               (x, y + 1) not in visited_tiles and \
               (x, y + 1) not in queue:
               
                if matrix[x][y + 1] == adjacent_tiles:
                    matrix[x][y] = chosen_color
                    matrix[x][y + 1] = chosen_color
                    queue.add((x, y + 1))
                    
            if adjacent_tiles == origin_color:
                matrix[x][y] = chosen_color

        return matrix, visited_tiles, origin_color

    def select_color(self, ):
        """Returns the index of the color resulted the maximum connection
           and associated array holding the values.

        This function finds out the color resulting the maximum tile conection
        and returns the values.

        Returns:
            chosen color:int -> Colors resulting maximum connection
            colors_with_connected_tiles:list -> colors and associated number of connections

        """
        colors_with_connected_tiles = [0] * self.number_of_colors

        for i in range(0, self.number_of_colors):

            colored_board = []

            colored_board, visited, origin_color = self.change_colors(x=0,
                                                        y=1,
                                                        visited_tiles=[],
                                                        matrix=None,
                                                        chosen_color=i)

            colored_board, _, _ = self.change_colors(x=1,
                                                  y=0,
                                                  visited_tiles=visited,
                                                  origin_color = origin_color,
                                                  matrix=colored_board,
                                                  chosen_color=i)

            colors_with_connected_tiles[i] = self.get_connected_tiles(
                x=0, y=0, matrix=colored_board)
            
            
        #print("color index", colors_with_connected_tiles)

        return colors_with_connected_tiles.index(
            max(colors_with_connected_tiles)), colors_with_connected_tiles

    def start_game(self,):
        """Colors the board choosing the best available choice by iterating all available colors.

        This function iteratively finds out the color resulting the maximum tile conection
        and stops when all the tiles colored using the same color. 


        """
        tiles_connected = 0
        minimum_turn_needed = 1

        while tiles_connected != 25:
            chosen_color, colors_with_connected_tiles = self.select_color()

            colored_board, visited, origin_color = self.change_colors(x=0,
                                                        y=1,
                                                        visited_tiles=[],
                                                        chosen_color=chosen_color)
            colored_board, _, _ = self.change_colors(x=1,
                                                  y=0,
                                                  origin_color = origin_color,
                                                  visited_tiles=visited,
                                                  matrix=colored_board,
                                                  chosen_color=chosen_color)
            self.board = colored_board
            tiles_connected = colors_with_connected_tiles[chosen_color]
            print(
                "\nColored board with index {} and maximum connection {}.".format(
                    chosen_color, tiles_connected))
            minimum_turn_needed += 1
            self.print_board()

        print(
            "Minimum turns needed to finish the game: ",
            minimum_turn_needed)

        return minimum_turn_needed