import unittest
import pygame
from ui.game import SudokuGame


class TestSudokuGame(unittest.TestCase):
    def setUp(self):
        self.game = SudokuGame()

    def test_has_running_state_set_as_true(self):
        self.assertTrue(self.game.running)

    def test_windows_caption_has_been_set_correctly(self):
        self.assertEqual('Sudoku', pygame.display.get_caption()[0])
