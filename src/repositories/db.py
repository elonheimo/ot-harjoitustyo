import sqlite3
from config import DB_PATH
class DB:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(DB_PATH)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("DROP TABLE events")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS events(
            id integer primary key autoincrement,
            name TEXT,
            type TEXT,
            game_mode TEXT
        )""")

    def insert(self, name: str, event_type: str, game_mode: str):
        self.cursor.execute("""INSERT OR IGNORE INTO events VALUES(NULL,?,?,?)""",
                            (name,
                            event_type,
                            game_mode))
        self.connection.commit()

    def read(self):
        self.cursor.execute("""SELECT * FROM events""")
        rows = self.cursor.fetchall()
        return rows
    