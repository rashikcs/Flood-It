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

## PlayerSimulator Class: 
- A class used to represent the player.
  ```
  # usage
  >>> player = PlayerSimulator(minimum_turns, player_name)
  ```

## FloodItGame Class: 
-  A class consists of player and board as attribute and used to manage and initiate the **flood-it game** -> color the board of all
  connected tiles to the origin.
  ```
  ### usage
  >>> floodit_obj = FloodItGame(number_of_rows, number_of_colors, minimum_turns, player_name))
  >>> colored_board, visited, origin_color = floodit_obj.start_flood_it()
  ```