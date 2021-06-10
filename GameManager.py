from Player import FloodItPlayerSimulator
from Game import FloodItGame


class GameManager:
    """
    A class used to manage games

    ...

    Attributes
    ----------
    game : dict
    game_arguments: list

    Methods
    -------
    add_game()
    get_game()
    init_game()
    start_games()
    """

    game = {}
    active_games = []
    game_arguments = {'Flood-It':['number_of_rows',
                                  'number_of_colors',
                                  'player_name',
                                  'minimum_turns',
                                  'skip_player_save']}

    def __init__(self, game_name:str):
        self.add_game(game_name)

    def add_game(self, game_name:str)->None:
        """
        Adds the game to the dict

        Args:

            game_name:str
        """
        self.game[game_name] = self.get_game(game_name)

    def get_game(self, game_name:str)->object:
        """
        returns the game object if found.
        """
        if game_name in self.game.keys():
            return self.game[game_name]
        elif game_name=='Flood-It':
            return FloodItGame()
        else:
            raise NotImplementedError 

    def found_game(self, game_name:str)->bool:
        """
        Returns if the game is already exists or not
        """

        if game_name in self.game.keys() and \
           game_name in self.game_arguments.keys():
            return True
        else:
            return False

    def init_floodIt_game(self, game_name:str, kwargs:dict):

        self.game[game_name].init_game(kwargs['number_of_rows'],
                            kwargs['number_of_colors'],
                            kwargs['player_name'],
                            kwargs['minimum_turns'],
                            kwargs['skip_player_save'])

        self.create_game_id(game_name, kwargs['player_name'])

    def create_game_id(self, game_name, player_name)->None:
        """
        Creates game ID by concating game and player name.
        """
        game_id = game_name+'_'+player_name

        if game_id not in self.active_games:
            self.active_games.append(game_id)
        else:
            raise ValueError('Duplicate ID found!!')

    def init_game(self, **kwargs)->None:
        """
        Finds and initializes the games with appropiate keywords or raise errors otherwise.

        Args:

            ***Flood-It Game***
            number_of_rows:int -> Value for the square matrix board
            number_of_colors:int -> Value for the num of colors in board
            player_name:str -> Player name
            minimum_turns:int -> minimum turns available for the player

        """
        game_name = kwargs.pop('game_name')

        if self.found_game(game_name):

            invalid_arguments = set(kwargs.keys()) - set(self.game_arguments[game_name])

            if game_name == "Flood-It" and \
               not invalid_arguments:

                self.init_floodIt_game(game_name, kwargs)
            else:
                raise ValueError("Invalid argument detected while initializing the game.")
        else:
            raise ValueError("Game not found!! Try adding the game using add_game()")            


    def start_games(self, )->None:
        """
        Starts all the active games.
        """
        if not self.active_games:
            print("Sorry! There are no active games")

        for game_id in self.active_games:
            game_name = game_id.split('_')[0]
            print('\nStarting the game: {}, Player Name: {}'.format(game_name,
                                                                    self.game[game_name].player.name))
            self.game[game_name].play_game()
            self.active_games.remove(game_id)

