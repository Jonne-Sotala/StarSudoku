from entities.user import User
from build.database_connection import DatabaseConnection


class UserRepository:
    """Class that manages the users in the database

    Attributes:
        connection: A connection object that connects to the sqlite database.
    """

    def __init__(self, connection=None):
        if connection is None:
            self.connection = DatabaseConnection().connect_to_database()
        else:
            self.connection = connection

    def create(self, user):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO user (username) VALUES (?);", (user.username,))
        self.connection.commit()

    def delete(self, user):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM user WHERE id = ?;", (user.id,))
        self.connection.commit()

    def delete_by_id(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM user WHERE id = ?;", (user_id,))
        self.connection.commit()

    def delete_all(self):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM user;")
        self.connection.commit()

    def find_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM user;")
        rows = cursor.fetchall()
        users = list(map(self.row_to_user, rows))
        return users

    def find_by_id(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM user WHERE id = ?;", (user_id,))
        row = cursor.fetchone()
        return self.row_to_user(row)

    def row_to_user(self, row):
        return User(row['username'], id=row['id'])
