from repositories.db import DB


class HighscoreRepository:
    """Class for altering and accesssing database table events
    """
    def __init__(self) -> None:
        """Class constructor that created new DB object
        """
        self.database = DB()

    def add_event(self, name: str, event_type: str, game_mode: str):
        """Calls DB object to insert new row to 'events' table

        Args:
            name (str): name of player
            event_type (str): must be 'WIN' or 'LOSE'
            game_mode (str): must be '3x3' , '5x5' or '7x7'
        """
        self.database.insert(name, event_type, game_mode)

    def clear_highscores(self):
        """Calls DB object to clear 'events' table from database
        """
        self.database.empty_table_events()

    def get_highscores(self, game_mode: str) -> list:
        """Returns top 5 player by game_mode

        Args:
            game_mode (str): must be '3x3' , '5x5' or '7x7'

        Returns:
            list: Top 5 players. example element ['Name',6]
        """
        events = self.database.read_events(game_mode)
        player_wins = {}
        for event in events:
            name = event[1]
            event_type = event[2]
            if name not in player_wins:
                player_wins[name] = 0
            if event_type == "WIN":
                player_wins[name] += 1
            if event_type == "LOSE":
                player_wins[name] -= 1
        lista = list(player_wins.items())
        lista.sort(key=lambda item: item[1], reverse=True)
        if len(lista) <= 5:
            return lista[: len(lista)]
        return lista[: 5]
