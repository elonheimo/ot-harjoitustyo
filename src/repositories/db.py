import sqlite3
from config import DB_PATH


class DB:
    """Class, reads from and writes to to SQLite database
    """
    def __init__(self) -> None:
        """Class constructor that initialises database connection
        """
        self.connection = sqlite3.connect(DB_PATH)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Initialises a new table to database if not exists
        """
        #self.cursor.execute("DROP TABLE events")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS events(
            id integer primary key autoincrement,
            name TEXT,
            type TEXT,
            game_mode TEXT
        )""")

    def empty_table_events(self):
        """Drops table events from database and initialises a new event table
        """
        self.cursor.execute("""
            DROP TABLE IF EXISTS events
        """)
        self.create_table()

    def insert(self, name: str, event_type: str, game_mode: str):
        """Inserts a new row events table

        Args:
            name (str): Name of player
            event_type (str): must be 'WIN' or 'LOSE'
            game_mode (str): game mode must be '3x3' , '5x5' or '7x7'
        """
        self.cursor.execute("""INSERT OR IGNORE INTO events VALUES(NULL,?,?,?)""",
                            (name,
                             event_type,
                             game_mode))
        self.connection.commit()

    def read_events(self, game_mode: str):
        """Reads event from database

        Args:
            game_mode (str): must be '3x3' , '5x5' or '7x7'

        Returns:
            List where every element is a list of row values
        """
        return self.cursor.execute(f"""
        SELECT * FROM events WHERE game_mode = '{game_mode}'
        """).fetchall()
