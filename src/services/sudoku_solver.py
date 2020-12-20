from repositories.sudoku_repository import SudokuRepository
import time


class SudokuSolver:
    """Class that takes care of sudoku solving in the application.

    Attributes:
        start_time: A float number that represents the starting time for starting the puzzle.
        sudoku: A sudoku object that stores the information of the current sudoku puzzle.
        state: A 2-dimensional list that stores the sudoku puzzle values in an easier way.
        current_row: An integer that tells the current row selected by user
        current_col: An integer that tells the current column selected by user
    """

    def __init__(self, sudoku=None, sudoku_repo=None):
        """The contructor that initiates the SudokuSolver object"""
        if sudoku_repo is None:
            self.sudoku_repo = SudokuRepository()
        else:
            self.sudoku_repo = sudoku_repo
        self.start_time = None
        self.sudoku = sudoku
        if sudoku:
            self.state = self.parse_str_to_sudoku_state(sudoku.initial_setup)
        else:
            self.state = None
        self.current_row = 4
        self.current_col = 4

    def get_sudokus_by_difficulty(self, difficulty):
        return self.sudoku_repo.find_by_difficulty(difficulty)

    def set_sudoku_solver(self, sudoku):
        self.start_time = time.time()
        self.sudoku = sudoku
        self.state = self.parse_str_to_sudoku_state(sudoku.initial_setup)

    def get_solving_time(self, solving_time_in_seconds=None):
        if solving_time_in_seconds is None:
            solving_time_in_seconds = self.get_solving_time_in_seconds()
        if solving_time_in_seconds <= 60:
            return str(solving_time_in_seconds)
        seconds = solving_time_in_seconds % 60
        minutes = solving_time_in_seconds // 60
        return f'{minutes}:{seconds:0=2d}'

    def get_solving_time_in_seconds(self):
        solving_time = round(time.time() - self.start_time)
        return solving_time

    def get_value_at(self, row, col):
        return self.state[row][col]

    def get_current_value(self):
        return self.state[self.current_row][self.current_col]

    def change_value_at(self, row, col, value):
        if not self.is_given(row, col):
            self.state[row][col] = value

    def change_current_value(self, value):
        if not self.is_given(self.current_row, self.current_col):
            self.state[self.current_row][self.current_col] = value

    def remove_value_at(self, row, col):
        if not self.is_given(row, col):
            self.state[row][col] = '0'

    def remove_current_value(self):
        if not self.is_given(self.current_row, self.current_col):
            self.state[self.current_row][self.current_col] = '0'

    def is_given(self, row, col):
        return self.sudoku.initial_setup[9*row + col] != '0'

    def is_selected(self, row, col):
        return row == self.current_row and col == self.current_col

    def check_answer(self):
        for row in range(9):
            for col in range(9):
                if self.state[row][col] != self.sudoku.answer[9*row + col]:
                    return False
        return True

    def get_answer(self):
        for row in range(9):
            for col in range(9):
                self.state[row][col] = self.sudoku.answer[9*row + col]

    def is_filled(self):
        for row in range(9):
            for col in range(9):
                if self.state[row][col] == '0':
                    return False
        return True

    def parse_str_to_sudoku_state(self, string):
        sudoku = []
        for i in range(9):
            sudoku.append(list(string[9*i:9*i+9]))
        return sudoku
