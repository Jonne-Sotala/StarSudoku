from entities.solution import Solution
from build.database_connection import DatabaseConnection
from repositories.sudoku_repository import SudokuRepository
from repositories.user_repository import UserRepository


class SolutionRepository:
    """Class that manages the solutions in the database

    Attributes:
        connection: A connection object that connects to the sqlite database.
        user_repo: A UserRepository object that can get User objects from the database.
        sudoku_repo A SudokuRepository object that can get Sudoku objects from the database.
    """

    def __init__(self, connection=None):
        """The contructor that initiates the SolutionRepository object

        Args:
            connection: Optional connection to database (used for testing)
        """
        if connection is None:
            self.connection = DatabaseConnection().connect_to_database()
        else:
            self.connection = connection
        self.user_repo = UserRepository(self.connection)
        self.sudoku_repo = SudokuRepository(self.connection)

    def create(self, solution):
        """Creates a database entry"""
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO solution (user_id, sudoku_id, is_correct, time) VALUES (?, ?, ?, ?)",
            (solution.user.id, solution.sudoku.id, solution.is_correct, solution.time))
        self.connection.commit()

    def delete_all(self):
        """Deletes all database entries"""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM solution;")
        self.connection.commit()

    def find_all(self):
        """Returns all the solutions"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM solution;")
        rows = cursor.fetchall()
        solutions = list(map(self.row_to_solution, rows))
        return solutions

    def find_last_4_solutions_by_user(self, user):
        """Returns the last 4 added solutions by a certain users"""
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM solution WHERE user_id = ? ORDER BY id DESC LIMIT 4;",
            (user.id,))
        rows = cursor.fetchall()
        solutions = list(map(self.row_to_solution, rows))
        return solutions

    def find_by_id(self, solution_id):
        """Returns a solution with a specific id"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM solution WHERE id = ?;", (solution_id,))
        row = cursor.fetchone()
        return self.row_to_solution(row)

    def row_to_solution(self, row):
        user = self.user_repo.find_by_id(row['user_id'])
        sudoku = self.sudoku_repo.find_by_id(row['sudoku_id'])
        return Solution(user, sudoku, row['is_correct'], row['time'], row['id'])
