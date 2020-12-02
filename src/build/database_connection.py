import sqlite3
from build.settings import DATABASE_PATH


class DatabaseConnection():
    def __init__(self):
        self.connection = None

    def connect_to_database(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.connection.row_factory = sqlite3.Row
        return self.connection

    def close_database_connection(self):
        self.connection.close()
