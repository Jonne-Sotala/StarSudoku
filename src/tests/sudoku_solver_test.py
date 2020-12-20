import unittest
from entities.sudoku import Sudoku
from services.sudoku_solver import SudokuSolver


class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        self.sudoku = Sudoku('Easy 1',
                             '800930002009000040702100960200000090060000070070006005027008406030000500500062008',
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
        row, col, value = 3, 6, '7'
        self.solver.change_value_at(row, col, value)
        self.assertEqual(value, self.solver.get_value_at(row, col))

    def test_change_value_at_doesnt_change_given_value(self):
        row, col, value = 0, 0, '1'
        self.solver.change_value_at(row, col, value)
        self.assertEqual('8', self.solver.get_value_at(row, col))

    def test_change_current_value_changes_value_correctly(self):
        value = '6'
        self.solver.change_current_value(value)
        self.assertEqual(value, self.solver.get_current_value())

    def test_change_current_value_doesnt_change_given_value(self):
        value = '1'
        self.solver.current_col = 0
        self.solver.current_row = 0
        self.solver.change_current_value(value)
        self.assertEqual('8', self.solver.get_current_value())

    def test_remove_value_at_removes_correct_value(self):
        row, col = 0, 1
        self.solver.change_value_at(row, col, '5')
        self.solver.remove_value_at(row, col)
        self.assertEqual('0', self.solver.get_value_at(row, col))

    def test_remove_value_at_doesnt_remove_given_value(self):
        row, col = 0, 0
        self.solver.remove_value_at(row, col)
        self.assertEqual('8', self.solver.get_value_at(row, col))

    def test_remove_current_value_removes_value(self):
        self.solver.change_current_value('9')
        self.solver.remove_current_value()
        self.assertEqual('0', self.solver.get_current_value())

    def test_remove_current_value_doesnt_remove_given_value(self):
        row, col = 0, 0
        self.solver.current_row = row
        self.solver.current_col = col
        self.solver.remove_current_value()
        self.assertEqual('8', self.solver.get_current_value())

    def test_is_given_returns_true_when_value_was_given(self):
        row, col = 0, 0
        self.assertTrue(self.solver.is_given(row, col))

    def test_is_selected_returns_true_when_given_box_is_selected(self):
        row, col = self.solver.current_row, self.solver.current_col
        self.assertTrue(self.solver.is_selected(row, col))

    def test_check_answer_returns_true_when_correct(self):
        self.solver.get_answer()
        self.assertTrue(self.solver.check_answer())

    def test_check_answer_returs_false_when_incorrect(self):
        self.solver.state[0][1] = 5
        self.assertFalse(self.solver.check_answer())

    def test_get_answer_fills_sudoku_with_right_answer(self):
        self.solver.get_answer()
        self.assertTrue(self.solver.check_answer())
