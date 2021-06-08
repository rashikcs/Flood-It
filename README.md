# Flood-It
Flood It is a popular one-player game that is available on many smart phones.

## Board Class: 
- A class used to construct and represent the Board.
	```
  ### usage
  >>> board_obj = Board(number_of_rows, number_of_colors)
  >>> board_obj.create_board()
  >>> board_obj.print_board()
  >>> board = board_obj.get_board()
  ```

## FloodItGame Class: 
- A class used to color the board of all
  connected tiles to the origin.
	```
  ### usage
  >>> floodit_obj = FloodItGame(number_of_rows, number_of_colors)
  >>> colored_board, visited, origin_color = floodit_obj.change_colors(origin_x,
                                                                       origin_y,
                                                                       origin_color,
                                                                       visited_tiles,
                                                                       board_obj.board,
                                                                       chosen_color)
                      
  >>> tile_count = floodit_obj.get_connected_tiles( origin_x, origin_y, colored_board))
  >>> color_with_most_connection, colors_with_connected_tiles_list = floodit_obj.select_color()
	```

## PlayerSimulator Class: 
- A class used to play the game as a player.
	```
  # usage
  >>> player = PlayerSimulator()
  >>> player.init_game(number_of_rows, number_of_colors, minimum_turns_avialable)
  >>> player.play_flood_it()
  >>> player.get_results(turns_used:int)
	```