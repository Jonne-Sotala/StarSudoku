from entities.sudoku import Sudoku
from build.database_connection import DatabaseConnection


class SudokuRepository:
    def __init__(self, connection=None):
        if connection is None:
            self.connection = DatabaseConnection().connect_to_database()
        else:
            self.connection = connection

    def create(self, sudoku):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO sudoku (initial_setup, answer, difficulty) VALUES (?, ?, ?);",
            (sudoku.initial_setup, sudoku.answer, sudoku.difficulty))
        self.connection.commit()

    def delete(self, sudoku):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM sudoku WHERE id = ?;", (sudoku.id,))
        self.connection.commit()

    def delete_by_id(self, sudoku_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM sudoku WHERE id = ?;", (sudoku_id,))
        self.connection.commit()

    def find_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM sudoku;")
        rows = cursor.fetchall()
        sudokus = list(map(self.row_to_sudoku, rows))
        return sudokus

    def find_by_difficulty(self, difficulty):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM sudoku WHERE difficulty = ?;", (difficulty,))
        rows = cursor.fetchall()
        sudokus = list(map(self.row_to_sudoku, rows))
        return sudokus

    def find_by_id(self, sudoku_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM sudoku WHERE id = ?;", (sudoku_id,))
        row = cursor.fetchone()
        return self.row_to_sudoku(row)

    def row_to_sudoku(self, row):
        return Sudoku(row['initial_setup'], row['answer'],
                      row['difficulty'], row['id'])
