import sqlite3
from build.settings import DATABASE_PATH
from build.settings import TEST_DATABASE_PATH


class DatabaseConnection():
    def __init__(self, test=False):
        self.test = test
        self.connection = None

    def connect_to_database(self):
        if self.test:
            self.connection = sqlite3.connect(TEST_DATABASE_PATH)
        else:
            self.connection = sqlite3.connect(DATABASE_PATH)
        self.connection.row_factory = sqlite3.Row
        return self.connection

    def close_database_connection(self):
        self.connection.close()
