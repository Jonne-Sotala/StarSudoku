from entities.sudoku import Sudoku
from build.database_connection import DatabaseConnection


class SudokuRepository:
    """Class that manages the sudokus in the database

    Attributes:
        connection: A connection object that connects to the sqlite database.
    """

    def __init__(self, connection=None):
        """The contructor that initiates the SudokuRepository object

        Args:
            connection: Optional connection to database (used for testing)
        """
        if connection is None:
            self.connection = DatabaseConnection().connect_to_database()
        else:
            self.connection = connection

    def create(self, sudoku):
        """Creates a database entry"""
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO sudoku (name, initial_setup, answer, difficulty) VALUES (?, ?, ?, ?);",
            (sudoku.name, sudoku.initial_setup, sudoku.answer, sudoku.difficulty))
        self.connection.commit()

    def delete(self, sudoku):
        """Deletes a specific sudoku from the database"""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM sudoku WHERE id = ?;", (sudoku.id,))
        self.connection.commit()

    def delete_by_id(self, sudoku_id):
        """Deletes a sudoku with a specific id from the database"""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM sudoku WHERE id = ?;", (sudoku_id,))
        self.connection.commit()

    def delete_all(self):
        """Deletes all of the database entries"""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM sudoku;")
        self.connection.commit()

    def find_all(self):
        """Returns a list of all the sudoku objects from the database"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM sudoku;")
        rows = cursor.fetchall()
        sudokus = list(map(self.row_to_sudoku, rows))
        return sudokus

    def find_by_difficulty(self, difficulty):
        """Returns a list of all the sudoku objects with specific difficulty from the database"""
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM sudoku WHERE difficulty = ?;", (difficulty,))
        rows = cursor.fetchall()
        sudokus = list(map(self.row_to_sudoku, rows))
        return sudokus

    def find_by_id(self, sudoku_id):
        """Returns a sudoku with a specific id"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM sudoku WHERE id = ?;", (sudoku_id,))
        row = cursor.fetchone()
        return self.row_to_sudoku(row)

    def row_to_sudoku(self, row):
        return Sudoku(row['name'], row['initial_setup'], row['answer'],
                      row['difficulty'], row['id'])
