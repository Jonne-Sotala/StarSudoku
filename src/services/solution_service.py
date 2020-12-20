from entities.solution import Solution
from repositories.solution_repository import SolutionRepository


class SolutionService:
    """Class that the application uses to store information about solutions and connect to the database.

    Attributes:
        current_solution: A Solution object that represents the current selected solution at history menu. 
        solution_repo: A SolutionRepository object that enables this class to connect to the database.
    """

    def __init__(self):
        self.current_solution = None
        self.solution_repo = SolutionRepository()

    def save_solution(self, user_id, sudoku_id, is_correct, time):
        self.solution_repo.create(
            Solution(user_id, sudoku_id, is_correct, time))

    def get_last_4_solutions_by_user(self, user):
        return self.solution_repo.find_last_4_solutions_by_user(user)
