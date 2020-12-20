from entities.solution import Solution
from repositories.solution_repository import SolutionRepository
from repositories.sudoku_repository import SudokuRepository
from repositories.user_repository import UserRepository


class SolutionService:
    """Class that the application uses to store information about solutions and connect to the database.

    Attributes:
        current_solution: A Solution object that represents the current selected solution at history menu. 
        solution_repo: A SolutionRepository object that enables this class to connect to the database.
    """

    def __init__(self, solution_repo=None, user_repo=None, sudoku_repo=None):
        """The contructor that initiates the SolutionService object"""
        self.current_solution = None
        if solution_repo is None:
            self.solution_repo = SolutionRepository()
        else:
            self.solution_repo = solution_repo
        if user_repo is None:
            self.user_repo = UserRepository()
        else:
            self.user_repo = user_repo
        if sudoku_repo is None:
            self.sudoku_repo = SudokuRepository()
        else:
            self.sudoku_repo = sudoku_repo

    def save_solution(self, user_id, sudoku_id, is_correct, time):
        """Saves a solution to the database"""
        user = self.user_repo.find_by_id(user_id)
        sudoku = self.sudoku_repo.find_by_id(sudoku_id)
        self.solution_repo.create(
            Solution(user, sudoku, is_correct, time))

    def get_last_4_solutions_by_user(self, user):
        """Returns a list of last 4 solutions by a user"""
        return self.solution_repo.find_last_4_solutions_by_user(user)
