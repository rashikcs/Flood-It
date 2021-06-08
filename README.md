# Flood-It
Flood It is a popular one-player game that is available on many smart phones. The player is given an n × n board of tiles where each tile is given one of m colors. 
The goal of the game is to change all the tiles to the same color, preferably with the fewest number of moves possible. This repo provides a non-gui solution of 
this game through a very simple greedy strategy.
## Board Class: 
- A class used to construct and represent the Board.
  ```
  ### usage
  >>> board_obj = Board(number_of_rows, number_of_colors)
  >>> board_obj.create_board()
  >>> board_obj.print_board()
  >>> board = board_obj.get_board()
  ```

## FloodItPlayerSimulator Class: 
- A class which inherits the player class and used to represent the floodit player which tries to solve the game iteratively by selecting the best color in each turn.
  ```
  # usage
  >>> floodit_player_obj = FloodItPlayerSimulator(player_name)
  >>> floodit_player_obj.init_player(minimum_turns)
  >>> floodit_player_obj.select_color(board_obj, change_neighbour_colors, get_connected_tiles)
  ```

## FloodItGame Class: 
-  A class which inherits the game class and used to manage and initiate the **flood-it game** -> color the board of all
   connected tiles to the origin.
   ```
   ### sample usage
   >>> floodit_game_obj = FloodItGame()
   >>> floodit_game_obj.init_game(number_of_rows, number_of_colors)
   >>> floodit_game_obj.play_game(floodit_player_obj)
   ```

## GameManager Class: 
- A class acts as a facade used to interact the above-mentioned classes which create and manage games and players.
  ```
  # usage
  >>> flood_it_game_mananger = GameManager(game_name = "Flood-It")
  >>> flood_it_game_mananger.init_game(number_of_rows=12, number_of_colors=5, minimum_turns=20)
  >>> flood_it_game_mananger.start_game()

  ```