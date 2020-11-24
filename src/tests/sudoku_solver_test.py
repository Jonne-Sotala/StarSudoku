import unittest
from entities.sudoku import Sudoku
from sudoku_solver import SudokuSolver


class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        self.sudoku = Sudoku('800930002009000040702100960200000090060000070070006005027008406030000500500062008',
                             '846937152319625847752184963285713694463859271971246385127598436638471529594362718',
                             'easy')
        self.solver = SudokuSolver(self.sudoku)

    def test_get_value_at_gets_correct_value1(self):
        row, col = 3, 3
        self.assertEqual(
            self.solver.state[row][col], self.solver.get_value_at(row, col))

    def test_get_value_at_gets_correct_value2(self):
        row, col = 6, 7
        self.assertEqual(
            self.solver.state[row][col], self.solver.get_value_at(row, col))

    def test_get_current_value_return_correct_value(self):
        current_row = self.solver.current_row
        current_col = self.solver.current_col
        current_value = self.solver.state[current_row][current_col]
        self.assertEqual(current_value, self.solver.get_current_value())

    def test_change_value_at_changes_value_correctly1(self):
        row, col, value = 0, 5, '4'
        self.solver.change_value_at(row, col, value)
        self.assertEqual(value, self.solver.get_value_at(row, col))

    def test_change_value_at_changes_value_correctly2(self):
        row, col, value = 3, 7, '7'
        self.solver.change_value_at(row, col, value)
        self.assertEqual(value, self.solver.get_value_at(row, col))

    def test_change_current_value_changes_value_correctly(self):
        value = '6'
        self.solver.change_current_value(value)
        self.assertEqual(value, self.solver.get_current_value())

    def test_remove_value_at_removes_correct_value(self):
        row, col = 0, 0
        self.solver.remove_value_at(row, col)
        self.assertEqual('0', self.solver.get_value_at(row, col))

    def test_remove_current_value_removes_value(self):
        self.solver.change_current_value('9')
        self.solver.remove_current_value()
        self.assertEqual('0', self.solver.get_current_value())

    def test_is_given_returns_true_when_value_was_given(self):
        row, col = 0, 0
        self.assertTrue(self.solver.is_given(row, col))

    def test_is_selected_returns_true_when_given_box_is_selected(self):
        row, col = self.solver.current_row, self.solver.current_col
        self.assertTrue(self.solver.is_selected(row, col))
