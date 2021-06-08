from Board import Board
from FloodItGame import FloodItGame
import unittest


class TestClassMethods(unittest.TestCase):
    """
    A class which is used to test the methods towards building the flood-it game.
    ...

    Attributes
    ----------
    # Test 1 results
    FloodItGame_test_1 : Board -> Board class with 3 colors and 5 rows

    create_board_result_test_1: list -> expected matrix of created boards
                                        with 3 colors and 5 rows

    FloodItGame_change_neighbour_colors_return1_test_1: list -> expected board after 1st
                                                step of change _colors()
                                                method of the FloodItGame
                                                class

    FloodItGame_change_neighbour_colors_return2_test_1:list -> visited tiles after 1st step
                                                of change _colors() method of
                                                the FloodItGame class

    FloodItGame_change_neighbour_colors_return3_test_1: int -> color of origin after 1st step
                                                of change _colors() methods of
                                                the FloodItGame class

    # Test 2 results
    FloodItGame_test_2 : Board -> Board class with 4 colors and 5 rows

    create_board_result_test_2: list -> expected matrix of created boards
                                        with 4 colors and 5 rows
    FloodItGame_change_neighbour_colors_return1_test_2: list -> expected board after 1st
                                                step of change_neighbour_colors()
                                                method of the FloodItGame
                                                class
    FloodItGame_change_neighbour_colors_return2_test_2:list -> visited tiles after 1st step
                                                of change _colors() method of
                                                the FloodItGame class
    FloodItGame_change_neighbour_colors_return3_test_2: int -> color of origin after 1st step
                                                of change _colors() methods of
                                                the FloodItGame class



    Methods
    -------
    test_Board_create_board_method()
    test_FloodItGame_change_neighbour_colors_method()
    test_FloodItGame_get_connected_neighbour_method()
    test_PlayerSimulator_play_flood_it_method()

    """


    # Results for the 1st test
    create_board_result_test_1 = [[2, 1, 2, 0, 2],
                                  [2, 0, 1, 0, 1],
                                  [1, 2, 0, 0, 1],
                                  [0, 2, 0, 0, 0],
                                  [0, 2, 2, 1, 2]]
    FloodItGame_change_neighbour_colors_return1_test_1 = [[1, 1, 2, 0, 2],
                                                [2, 0, 1, 0, 1],
                                                [1, 2, 0, 0, 1],
                                                [0, 2, 0, 0, 0],
                                                [0, 2, 2, 1, 2]]

    FloodItGame_change_neighbour_colors_return2_test_1 = [(0, 1), (0, 0)]
    FloodItGame_change_neighbour_colors_return3_test_1 = 2

    # Results for the 2nd test
    create_board_result_test_2 = [[2, 0, 1, 2, 0],
                                  [3, 3, 1, 0, 3],
                                  [0, 1, 0, 0, 1],
                                  [3, 2, 0, 3, 0],
                                  [1, 2, 3, 0, 2]]
    FloodItGame_change_neighbour_colors_return1_test_2 = [[1, 0, 1, 2, 0],
                                                [3, 3, 1, 0, 3],
                                                [0, 1, 0, 0, 1],
                                                [3, 2, 0, 3, 0],
                                                [1, 2, 3, 0, 2]]

    FloodItGame_change_neighbour_colors_return2_test_2 = [(0, 1)]
    FloodItGame_change_neighbour_colors_return3_test_2 = 2

    def test_Board_create_board_method(self):
        """
        method to check create_board() method of the Board class
        """

        self.assertEqual(FloodItGame_test_1.board_obj.get_board(),
                         self.create_board_result_test_1)

        FloodItGame_test_1.board_obj.print_board(
            '\nCreated Board with {} colors.'.format(
                FloodItGame_test_1.board_obj.number_of_colors))


        self.assertEqual(FloodItGame_test_2.board_obj.get_board(),
                         self.create_board_result_test_2)

        FloodItGame_test_2.board_obj.print_board(
            '\nCreated Board with {} colors.'.format(
                FloodItGame_test_2.board_obj.number_of_colors))

    def test_FloodItGame_change_neighbour_colors_method(self):
        """
        method to check change_neighbour_colors() method of the FloodItGame class
        """
        colored_board, visited, origin_color = FloodItGame_test_1.change_neighbour_colors(x=0,
                                                                                     y=1,
                                                                                     visited_tiles=[],
                                                                                     chosen_color=1)
        self.assertEqual(colored_board, self.FloodItGame_change_neighbour_colors_return1_test_1)
        self.assertEqual(visited, self.FloodItGame_change_neighbour_colors_return2_test_1)
        self.assertEqual(origin_color, self.FloodItGame_change_neighbour_colors_return3_test_1)

        colored_board, visited, origin_color = FloodItGame_test_2.change_neighbour_colors(x=0,
                                                                                     y=1,
                                                                                     visited_tiles=[],
                                                                                     chosen_color=1)
        self.assertEqual(colored_board, self.FloodItGame_change_neighbour_colors_return1_test_2)
        self.assertEqual(visited, self.FloodItGame_change_neighbour_colors_return2_test_2)
        self.assertEqual(origin_color, self.FloodItGame_change_neighbour_colors_return3_test_2)

    def test_FloodItGame_get_connected_neighbour_method(self):
        """
        method to check get_connected_neighbour() method of the FloodItGame class

        """

        # Testing for board with 3 colors
        colored_board, visited, origin_color = FloodItGame_test_1.change_neighbour_colors(x=0,
                                                                                     y=1,
                                                                                     visited_tiles=[],
                                                                                     chosen_color=1)
        colored_board, _, _ = FloodItGame_test_1.change_neighbour_colors(x=1,
                                                                    y=0,
                                                                    visited_tiles=visited,
                                                                    origin_color=origin_color,
                                                                    matrix=colored_board,
                                                                    chosen_color=1)
        self.assertEqual(FloodItGame_test_1.get_connected_tiles(x=0, y=0, matrix=colored_board),
                         4)

        # Testing for board with 4 colors
        colored_board, visited, origin_color = FloodItGame_test_2.change_neighbour_colors(x=0,
                                                                                     y=1,
                                                                                     visited_tiles=[],
                                                                                     chosen_color=1)
        colored_board, _, _ = FloodItGame_test_2.change_neighbour_colors(x=1,
                                                                    y=0,
                                                                    visited_tiles=visited,
                                                                    origin_color=origin_color,
                                                                    matrix=colored_board,
                                                                    chosen_color=1)
        self.assertEqual(FloodItGame_test_2.get_connected_tiles(x=0,
                                                                     y=0,
                                                                     matrix=colored_board),
                         1)

    def test_PlayerSimulator_play_flood_it_method(self):
        """
        method to check start_flood_it() method of the FloodItGame class
        """

        self.assertEqual(FloodItGame_test_1.start_flood_it(), 5)
        self.assertEqual(FloodItGame_test_2.start_flood_it(), 7)


if __name__ == "__main__":
    
    FloodItGame_test_1 = FloodItGame(5, 3, 20)
    FloodItGame_test_2 = FloodItGame(5, 4, 20)

    unittest.main()
