import unittest


import unittest
from build.database_connection import DatabaseConnection
from entities.solution import Solution
from entities.sudoku import Sudoku
from entities.user import User
from repositories.solution_repository import SolutionRepository
from repositories.sudoku_repository import SudokuRepository
from repositories.user_repository import UserRepository
from services.solution_service import SolutionService


class TestSolutionService(unittest.TestCase):
    def setUp(self):
        connection = DatabaseConnection(test=True).connect_to_database()
        self.user_repo = UserRepository(connection)
        self.user_repo.delete_all()
        self.sudoku_repo = SudokuRepository(connection)
        self.sudoku_repo.delete_all()
        self.solution_repo = SolutionRepository(connection)
        self.solution_repo.delete_all()
        self.solution_service = SolutionService(
            self.solution_repo, self.user_repo, self.sudoku_repo)

        self.user_jonne = User('Jonne')
        self.user_pekka = User('Pekka')
        self.sudoku1 = Sudoku('Easy 1',
                              '800930002009000040702100960200000090060000070070006005027008406030000500500062008',
                              '846937152319625847752184963285713694463859271971246385127598436638471529594362718',
                              'easy')
        self.sudoku2 = Sudoku('Easy 2',
                              '800930002009000040702100960200000090060000070070006005027008406030000500500062008',
                              '846937152319625847752184963285713694463859271971246385127598436638471529594362718',
                              'easy')

        self.user_repo.create(self.user_jonne)
        self.sudoku_repo.create(self.sudoku1)

        self.user_jonne = self.user_repo.find_all()[0]
        self.sudoku1 = self.sudoku_repo.find_all()[0]
        self.solution1 = Solution(self.user_jonne, self.sudoku1, True, 60)
        self.solution2 = Solution(self.user_jonne, self.sudoku1, False, 120)
        self.solution3 = Solution(self.user_jonne, self.sudoku1, True, 180)
        self.solution4 = Solution(self.user_jonne, self.sudoku1, False, 240)
        self.solution5 = Solution(self.user_jonne, self.sudoku1, True, 300)

    def test_save_solution(self):
        self.solution_service.save_solution(
            self.solution1.user.id,
            self.solution1.sudoku.id,
            self.solution1.is_correct,
            self.solution1.time)
        solutions = self.solution_repo.find_all()
        self.assertEqual(1, len(solutions))
        self.solution_service.save_solution(
            self.solution2.user.id,
            self.solution2.sudoku.id,
            self.solution2.is_correct,
            self.solution2.time)
        solutions = self.solution_repo.find_all()
        self.assertEqual(2, len(solutions))

    def test_get_last_4_solutions_by_user(self):
        self.solution_service.save_solution(
            self.solution1.user.id,
            self.solution1.sudoku.id,
            self.solution1.is_correct,
            self.solution1.time)
        self.solution_service.save_solution(
            self.solution2.user.id,
            self.solution2.sudoku.id,
            self.solution2.is_correct,
            self.solution2.time)
        self.solution_service.save_solution(
            self.solution3.user.id,
            self.solution3.sudoku.id,
            self.solution3.is_correct,
            self.solution3.time)
        self.solution_service.save_solution(
            self.solution4.user.id,
            self.solution4.sudoku.id,
            self.solution4.is_correct,
            self.solution4.time)
        self.solution_service.save_solution(
            self.solution5.user.id,
            self.solution5.sudoku.id,
            self.solution5.is_correct,
            self.solution5.time)
        solutions = self.solution_service.get_last_4_solutions_by_user(
            self.user_jonne)
        self.assertEqual(4, len(solutions))
        self.assertEqual(300, solutions[0].time)
        self.assertEqual(120, solutions[3].time)
