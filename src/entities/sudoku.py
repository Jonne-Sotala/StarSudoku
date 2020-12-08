
class Sudoku():
    """Class that stores information about specific sudoku puzzle.

    Attributes:
        id: An integer that is a unique identifier for the sudoku puzzle.
        initial_setup: A string that represents the sudoku puzzle.
        answer: A string that shows the right answer to the sudoku.
        difficulty: A string that tells the sudoku's difficulty.
    """

    def __init__(self, initial_setup, answer, difficulty, id=None):
        """The Constructor that initiates the sudoku object"""
        self.id = id
        self.initial_setup = initial_setup
        self.answer = answer
        self.difficulty = difficulty
