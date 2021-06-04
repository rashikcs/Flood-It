from Color_Board import Color_Board
import unittest

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


class TestfirstStep(unittest.TestCase):

    def test_create_board_method(self):
        self.assertEqual(
            color_board_test_1.get_board(),
            create_board_result_test_1)
        self.assertEqual(
            color_board_test_2.get_board(),
            create_board_result_test_2)

    def test_change_colors_method(self):

        colored_board, visited, origin_color = color_board_test_1.change_colors(
            x=0, y=1, visited_tiles=[], chosen_color=1)
        self.assertEqual(colored_board, change_colors_result_board_test_1)
        self.assertEqual(visited, change_colors_result_visited_test_1)
        self.assertEqual(origin_color, change_colors_result_origin_test_1)

        colored_board, visited, origin_color = color_board_test_2.change_colors(
            x=0, y=1, visited_tiles=[], chosen_color=1)
        self.assertEqual(colored_board, change_colors_result_board_test_2)
        self.assertEqual(visited, change_colors_result_visited_test_2)
        self.assertEqual(origin_color, change_colors_result_origin_test_2)

    def test_get_connected_neighbour_method(self):

        # Testing for board with 4 colors
        colored_board, visited, origin_color = color_board_test_1.change_colors(
            x=0, y=1, visited_tiles=[], chosen_color=1)
        colored_board, _, _ = color_board_test_1.change_colors(x=1,
                                                               y=0,
                                                               visited_tiles=visited,
                                                               origin_color=origin_color,
                                                               matrix=colored_board,
                                                               chosen_color=1)
        self.assertEqual(
            color_board_test_1.get_connected_tiles(
                x=0, y=0, matrix=colored_board), 4)

        # Testing for board with 4 colors
        colored_board, visited, origin_color = color_board_test_2.change_colors(
            x=0, y=1, visited_tiles=[], chosen_color=1)
        colored_board, _, _ = color_board_test_2.change_colors(x=1,
                                                               y=0,
                                                               visited_tiles=visited,
                                                               origin_color=origin_color,
                                                               matrix=colored_board,
                                                               chosen_color=1)
        self.assertEqual(
            color_board_test_2.get_connected_tiles(
                x=0, y=0, matrix=colored_board), 6)

    def test_start_game_method(self):
        self.assertEqual(color_board_test_1.start_game(), 6)
        self.assertEqual(color_board_test_2.start_game(), 7)


if __name__ == "__main__":
    
    color_board_test_1 = Color_Board(5, 3)
    color_board_test_1.print_board(
        '\nPrint Board with {} colors.'.format(
            color_board_test_1.number_of_colors))

    color_board_test_2 = Color_Board(5, 4)
    color_board_test_2.print_board(
        '\nPrint Board with {} colors.'.format(
            color_board_test_1.number_of_colors))

    unittest.main()
