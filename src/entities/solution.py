
class Solution:
    """Class that stores information about users' solutions to different sudoku puzzles.

    Attributes:
        user: A user object that is the user who made the solution.
        sudoku: A sudoku object that ties the solution to a specific sudoku puzzle.
        is_correct: A boolean value that shows whether the solution was correct.
        time: An integer that represents the time it took to get the solution in seconds.
    """

    def __init__(self, sudoku, user, is_correct, time):
        """The Constructor that initiates the solution object"""
        self.user = user
        self.sudoko = sudoku
        self.is_correct = is_correct
        self.time = time
