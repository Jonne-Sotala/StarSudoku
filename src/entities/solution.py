
class Solution:
    """Class that stores information about users' solutions to different sudoku puzzles.

    Attributes:
        id: An integer that is a unique identifier for the solution.
        user: A user object that represents the user who made the solution.
        sudoku: A sudoku object that ties the solution to a specific sudoku puzzle.
        is_correct: A boolean value that shows whether the solution was correct.
        time: An integer that represents the time it took to get the solution in seconds.
    """

    def __init__(self, user, sudoku, is_correct, time, id=None):
        """The Constructor that initiates the solution object"""
        self.id = id
        self.user = user
        self.sudoku = sudoku
        self.is_correct = is_correct
        self.time = time
