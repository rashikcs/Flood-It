from GameManager import GameManager


if __name__ == "__main__":

    game_name = "Flood-It"
    flood_it_game_mananger = GameManager(game_name = game_name)
    flood_it_game_mananger.init_game(game_name = game_name,
    							     number_of_rows=12,
    								 number_of_colors=5,
    								 player_name ='SimulatedPlayer' ,
    								 minimum_turns=20,
    								 skip_player_save = True)
    flood_it_game_mananger.start_games()