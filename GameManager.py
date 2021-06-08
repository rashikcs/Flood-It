from Player import FloodItPlayerSimulator
from Game import FloodItGame


class GameManager:
    """
    A class used to manage the game and player

    ...

    Attributes
    ----------
    game : Game
    player : Player
    game_arguments: list

    Methods
    -------
    init_game()
    get_player()
    get_game()
    start_game()
    """

    game = None
    player = None
    game_arguments = {'Flood-It':['number_of_rows', 'number_of_colors', 'minimum_turns']}

    def __init__(self, game_name:str, player_name:str = "Smart mouth"):

        self.game = self.get_game(game_name)
        self.player = self.get_player(game_name, player_name)

    def get_game(self, game_name:str)->object:
        """
        returns the created game object.
        """
        if self.game:
            return self.game
        elif game_name=='Flood-It':
            print("Flood-It game selected!!!")
            return FloodItGame()
        else:
            raise ValueError("Passed Game not found")

    def get_player(self, game_name:str, player_name)->object:
        """
        returns the created player object.
        """
        if self.player:
            return self.player
        elif game_name=='Flood-It':
            return FloodItPlayerSimulator(player_name)
        else:
            raise ValueError("Passed Game not found")

    def init_game(self, **kwargs)->None:
        """
        Initializes the game with appropiate associated keywords or raise errors otherwise.
        """

        invalid_arguments = set(kwargs.keys()) - set(self.game_arguments[self.game.name])

        if self.game.name == "Flood-It" and not invalid_arguments:
            self.game.init_game(kwargs['number_of_rows'], kwargs['number_of_colors'])
            self.player.init_player(kwargs['minimum_turns'])          
        else:
            raise ValueError("Invalid argument detected while initializing the game.")


    def start_game(self, )->None:
        """
        Starts the game and shows result.
        """
        print('\nStarting the game: {}, Player Name: {}'.format(self.game.name, self.player.name))
        self.game.play_game(self.player)
