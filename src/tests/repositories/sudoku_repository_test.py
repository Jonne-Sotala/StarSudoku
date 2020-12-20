import unittest
from build.database_connection import DatabaseConnection
from repositories.sudoku_repository import SudokuRepository
from entities.sudoku import Sudoku


class TestSudokuRepository(unittest.TestCase):
    def setUp(self):
        connection = DatabaseConnection(test=True).connect_to_database()
        self.sudoku_repo = SudokuRepository(connection)
        self.sudoku_repo.delete_all()
        self.sudoku1 = Sudoku('Easy 1',
                              '800930002009000040702100960200000090060000070070006005027008406030000500500062008',
                              '846937152319625847752184963285713694463859271971246385127598436638471529594362718',
                              'easy')
        self.sudoku2 = Sudoku('Easy 2',
                              '000006080009105372080700016000000034000351000730000000610008020823904600070600000',
                              '157236489469185372382749516591867234246351798738492165614578923823914657975623841',
                              'easy')
        self.sudoku3 = Sudoku('Medium 1',
                              '009000000427060098000290370005000030003519600040000200032076000850030724000000900',
                              '369758412427163598518294376795642831283519647641387259932476185856931724174825963',
                              'medium')

    def test_create(self):
        self.sudoku_repo.create(self.sudoku1)
        sudokus = self.sudoku_repo.find_all()
        self.assertEqual(1, len(sudokus))
        self.assertEqual(self.sudoku1.initial_setup, sudokus[0].initial_setup)

    def test_delete(self):
        self.sudoku_repo.create(self.sudoku1)
        sudoku_to_del = self.sudoku_repo.find_all()[0]
        self.sudoku_repo.delete(sudoku_to_del)
        sudokus = self.sudoku_repo.find_all()
        self.assertEqual(0, len(sudokus))

    def test_delete_by_id(self):
        self.sudoku_repo.create(self.sudoku1)
        sudoku_to_delete = self.sudoku_repo.find_all()[0]
        self.sudoku_repo.delete_by_id(sudoku_to_delete.id)
        sudokus = self.sudoku_repo.find_all()
        self.assertEqual(0, len(sudokus))

    def test_find_all(self):
        self.sudoku_repo.create(self.sudoku1)
        self.sudoku_repo.create(self.sudoku2)
        sudokus = self.sudoku_repo.find_all()
        self.assertEqual(2, len(sudokus))
        self.assertEqual(self.sudoku1.initial_setup, sudokus[0].initial_setup)
        self.assertEqual(self.sudoku2.initial_setup, sudokus[1].initial_setup)

    def test_find_by_id(self):
        self.sudoku_repo.create(self.sudoku1)
        sudoku_to_find = self.sudoku_repo.find_all()[0]
        sudoku = self.sudoku_repo.find_by_id(sudoku_to_find.id)
        self.assertEqual(sudoku_to_find.id, sudoku.id)

    def test_find_by_difficulty(self):
        self.sudoku_repo.create(self.sudoku1)
        self.sudoku_repo.create(self.sudoku2)
        self.sudoku_repo.create(self.sudoku3)
        easy_sudokus = self.sudoku_repo.find_by_difficulty('easy')
        medium_sudokus = self.sudoku_repo.find_by_difficulty('medium')
        hard_sudokus = self.sudoku_repo.find_by_difficulty('hard')
        self.assertEqual(2, len(easy_sudokus))
        self.assertEqual(1, len(medium_sudokus))
        self.assertEqual(0, len(hard_sudokus))
