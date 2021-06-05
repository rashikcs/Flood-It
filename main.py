from Color_Board import Color_Board
import unittest


class TestfirstStep(unittest.TestCase):
    """
    A class which is used to test the methods towards building the flood-it game.
    ...

    Attributes
    ----------
    color_board_test_1 : Board -> Board class with 3 colors and 5 rows

    create_board_result_test_1: list -> expected matrix of created boards
                                        with 3 colors and 5 rows

    change_colors_result_board_test_1: list -> expected board after 1st
                                                step of change _colors()
                                                method of the Color_Board
                                                class

    change_colors_result_visited_test_1:list -> visited tiles after 1st step
                                                of change _colors() method of
                                                the Color_Board class

    change_colors_result_origin_test_1: int -> color of origin after 1st step
                                                of change _colors() methods of
                                                the Color_Board class


    color_board_test_2 : Board -> Board class with 4 colors and 5 rows
    create_board_result_test_2: list -> expected matrix of created boards
                                        with 4 colors and 5 rows
    change_colors_result_board_test_2: list -> expected board after 1st
                                                step of change _colors()
                                                method of the Color_Board
                                                class
    change_colors_result_visited_test_2:list -> visited tiles after 1st step
                                                of change _colors() method of
                                                the Color_Board class
    change_colors_result_origin_test_2: int -> color of origin after 1st step
                                                of change _colors() methods of
                                                the Color_Board class



    Methods
    -------
    test_create_board_method()
    test_change_colors_method()
    test_get_connected_neighbour_method()
    test_start_game_method()

    """

    color_board_test_1 = Color_Board(5, 3)

    create_board_result_test_1 = [[2, 1, 2, 0, 2],
                                  [2, 0, 1, 0, 1],
                                  [1, 2, 0, 0, 1],
                                  [0, 2, 0, 0, 0],
                                  [0, 2, 2, 1, 2]]
    change_colors_result_board_test_1 = [[1, 1, 2, 0, 2],
                                         [2, 0, 1, 0, 1],
                                         [1, 2, 0, 0, 1],
                                         [0, 2, 0, 0, 0],
                                         [0, 2, 2, 1, 2]]

    change_colors_result_visited_test_1 = [(0, 1), (0, 0)]
    change_colors_result_origin_test_1 = 2

    color_board_test_2 = Color_Board(5, 4)
    create_board_result_test_2 = [[2, 0, 1, 2, 0],
                                  [3, 3, 1, 0, 3],
                                  [0, 1, 0, 0, 1],
                                  [3, 2, 0, 3, 0],
                                  [1, 2, 3, 0, 2]]
    change_colors_result_board_test_2 = [[1, 0, 1, 2, 0],
                                         [3, 3, 1, 0, 3],
                                         [0, 1, 0, 0, 1],
                                         [3, 2, 0, 3, 0],
                                         [1, 2, 3, 0, 2]]

    change_colors_result_visited_test_2 = [(0, 1)]
    change_colors_result_origin_test_2 = 2

    def test_create_board_method(self):
        """
        method to check create_board() method of the Board class
        """
        self.assertEqual(
            self.color_board_test_1.get_board(),
            self.create_board_result_test_1)
        self.color_board_test_1.print_board(
            '\nCreated Board with {} colors.'.format(
                self.color_board_test_1.number_of_colors))

        self.assertEqual(
            self.color_board_test_2.get_board(),
            self.create_board_result_test_2)
        self.color_board_test_2.print_board(
            '\nCreated Board with {} colors.'.format(
                self.color_board_test_2.number_of_colors))

    def test_change_colors_method(self):
        """
        method to check change_colors() method of the ColorBoard class
        """
        colored_board, visited, origin_color = self.color_board_test_1.change_colors(x=0,
                                                                                     y=1,
                                                                                     visited_tiles=[],
                                                                                     chosen_color=1)
        self.assertEqual(colored_board, self.change_colors_result_board_test_1)
        self.assertEqual(visited, self.change_colors_result_visited_test_1)
        self.assertEqual(origin_color, self.change_colors_result_origin_test_1)

        colored_board, visited, origin_color = self.color_board_test_2.change_colors(x=0,
                                                                                     y=1,
                                                                                     visited_tiles=[],
                                                                                     chosen_color=1)
        self.assertEqual(colored_board, self.change_colors_result_board_test_2)
        self.assertEqual(visited, self.change_colors_result_visited_test_2)
        self.assertEqual(origin_color, self.change_colors_result_origin_test_2)

    def test_get_connected_neighbour_method(self):
        """
        method to check get_connected_neighbour() method of the ColorBoard class

        """
        # Testing for board with 3 colors
        colored_board, visited, origin_color = self.color_board_test_1.change_colors(
            x=0, y=1, visited_tiles=[], chosen_color=1)
        colored_board, _, _ = self.color_board_test_1.change_colors(x=1,
                                                                    y=0,
                                                                    visited_tiles=visited,
                                                                    origin_color=origin_color,
                                                                    matrix=colored_board,
                                                                    chosen_color=1)
        self.assertEqual(
            self.color_board_test_1.get_connected_tiles(
                x=0, y=0, matrix=colored_board), 4)

        # Testing for board with 4 colors
        colored_board, visited, origin_color = self.color_board_test_2.change_colors(
            x=0, y=1, visited_tiles=[], chosen_color=1)
        colored_board, _, _ = self.color_board_test_2.change_colors(x=1,
                                                                    y=0,
                                                                    visited_tiles=visited,
                                                                    origin_color=origin_color,
                                                                    matrix=colored_board,
                                                                    chosen_color=1)
        self.assertEqual(
            self.color_board_test_2.get_connected_tiles(
                x=0, y=0, matrix=colored_board), 1)

    def test_start_game_method(self):
        """
        method to check start_game() method of the ColorBoard class
        """
        self.assertEqual(self.color_board_test_1.start_game(), 5)
        self.assertEqual(self.color_board_test_2.start_game(), 7)


if __name__ == "__main__":
    unittest.main()
