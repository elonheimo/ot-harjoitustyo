from repositories.db import DB


class HighscoreRepository:
    def __init__(self) -> None:
        self.database = DB()

    def add_event(self, name, event_type, game_mode):
        self.database.insert(name, event_type, game_mode)

    def clear_highscores(self):
        self.database.empty_table_events()

    def get_highscores(self, game_mode):
        """
        Returns the top 0 to 5 players in a list
        """
        events = self.database.cursor.execute(f"""
        SELECT * FROM events WHERE game_mode = '{game_mode}'
        """).fetchall()
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
