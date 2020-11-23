from ui.game import SudokuGame

game = SudokuGame()

while game.running:
    game.current_menu.display_menu()
    game.solving_sudoku()
