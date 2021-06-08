from GameManager import GameManager


if __name__ == "__main__":
    
    flood_it_game_mananger = GameManager(game_name = "Flood-It")
    flood_it_game_mananger.init_game(number_of_rows=12, number_of_colors=5, minimum_turns=20)
    flood_it_game_mananger.start_game()