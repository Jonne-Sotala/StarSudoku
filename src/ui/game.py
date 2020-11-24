import pygame
from ui.menu import MainMenu, DifficultyMenu, CreditsMenu
from entities.sudoku import Sudoku
from sudoku_solver import SudokuSolver


class SudokuGame:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # State variables
        self.running = True
        self.solving = False
        self.insert_mode = False
        self.move_mode = True

        # KEYS
        self.START_KEY = False
        self.BACK_KEY = False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.NUM_1_KEY = False
        self.NUM_2_KEY = False
        self.NUM_3_KEY = False
        self.NUM_4_KEY = False
        self.NUM_5_KEY = False
        self.NUM_6_KEY = False
        self.NUM_7_KEY = False
        self.NUM_8_KEY = False
        self.NUM_9_KEY = False
        self.REMOVE_KEY = False
        self.SUBMIT_KEY = False

        # Define contant variables
        self.WIDTH = 800
        self.HEIGHT = 600
        self.BEIGE = (225, 198, 153)
        self.BLACK = (0, 0, 0)
        self.GREY = (96, 96, 96)
        self.GREY_BLUE = (102, 122, 128)
        self.GREEN = (0, 128, 0)

        # Surface
        self.display = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Caption
        caption = 'Sudoku'
        pygame.display.set_caption(caption)

        # Font
        self.menu_font = 'resources/fonts/8-BIT WONDER.TTF'
        self.sudoku_font = 'resources/fonts/comicsans.ttf'

        # Menus
        self.main_menu = MainMenu(self)
        self.difficulty_menu = DifficultyMenu(self)
        self.credits_menu = CreditsMenu(self)
        self.current_menu = self.main_menu

        # Current sudoku puzzle and solver
        self.sudoku = Sudoku('800930002009000040702100960200000090060000070070006005027008406030000500500062008',
                             '846937152319625847752184963285713694463859271971246385127598436638471529594362718',
                             'easy')
        self.solver = SudokuSolver(self.sudoku)

    def solving_sudoku(self):
        while self.solving:
            self.check_events()
            if self.move_mode:
                self.movement_mode()
            elif self.insert_mode:
                self.insertion_mode()
            self.display.fill(self.BEIGE)
            self.draw_sudoku_grid()
            self.draw_sudoku_boxes()
            self.draw_text("COMMANDS", 20, (self.HEIGHT+self.WIDTH)/2, 18)
            self.draw_text("MOVE", 15, (self.HEIGHT+self.WIDTH)/2, 70)
            self.draw_text("ARROW KEYS", 15, (self.HEIGHT+self.WIDTH)/2, 100)
            self.draw_text("INSERT MODE", 15, (self.HEIGHT+self.WIDTH)/2, 150)
            self.draw_text("ENTER", 15, (self.HEIGHT+self.WIDTH)/2, 180)
            self.draw_text("REMOVE NUM", 15, (self.HEIGHT+self.WIDTH)/2, 230)
            self.draw_text("DEL", 15, (self.HEIGHT+self.WIDTH)/2, 260)
            self.draw_text("SUBMIT", 15, (self.HEIGHT+self.WIDTH)/2, 310)
            self.draw_text("S", 15, (self.HEIGHT+self.WIDTH)/2, 340)
            self.draw_text("BACK TO MENU", 15, (self.HEIGHT+self.WIDTH)/2, 550)
            self.draw_text("BACKSPACE", 15, (self.HEIGHT+self.WIDTH)/2, 580)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def insertion_mode(self):
        if self.BACK_KEY or self.START_KEY:
            self.insert_mode = False
            self.move_mode = True
        elif self.NUM_1_KEY:
            self.solver.change_current_value('1')
            self.insert_mode = False
            self.move_mode = True
        elif self.NUM_2_KEY:
            self.solver.change_current_value('2')
            self.insert_mode = False
            self.move_mode = True
        elif self.NUM_3_KEY:
            self.solver.change_current_value('3')
            self.insert_mode = False
            self.move_mode = True
        elif self.NUM_4_KEY:
            self.solver.change_current_value('4')
            self.insert_mode = False
            self.move_mode = True
        elif self.NUM_5_KEY:
            self.solver.change_current_value('5')
            self.insert_mode = False
            self.move_mode = True
        elif self.NUM_6_KEY:
            self.solver.change_current_value('6')
            self.insert_mode = False
            self.move_mode = True
        elif self.NUM_7_KEY:
            self.solver.change_current_value('7')
            self.insert_mode = False
            self.move_mode = True
        elif self.NUM_8_KEY:
            self.solver.change_current_value('8')
            self.insert_mode = False
            self.move_mode = True
        elif self.NUM_9_KEY:
            self.solver.change_current_value('9')
            self.insert_mode = False
            self.move_mode = True

    def movement_mode(self):
        if self.BACK_KEY:
            self.solving = False
        elif self.START_KEY:
            self.insert_mode = True
            self.move_mode = False
        elif self.UP_KEY and self.solver.current_row > 0:
            self.solver.current_row -= 1
        elif self.DOWN_KEY and self.solver.current_row < 8:
            self.solver.current_row += 1
        elif self.LEFT_KEY and self.solver.current_col > 0:
            self.solver.current_col -= 1
        elif self.RIGHT_KEY and self.solver.current_col < 8:
            self.solver.current_col += 1
        elif self.REMOVE_KEY:
            self.solver.remove_current_value()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.solving = False, False
                self.current_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_UP or event.key == pygame.K_k:
                    self.UP_KEY = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_j:
                    self.DOWN_KEY = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_h:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_1:
                    self.NUM_1_KEY = True
                if event.key == pygame.K_2:
                    self.NUM_2_KEY = True
                if event.key == pygame.K_3:
                    self.NUM_3_KEY = True
                if event.key == pygame.K_4:
                    self.NUM_4_KEY = True
                if event.key == pygame.K_5:
                    self.NUM_5_KEY = True
                if event.key == pygame.K_6:
                    self.NUM_6_KEY = True
                if event.key == pygame.K_7:
                    self.NUM_7_KEY = True
                if event.key == pygame.K_8:
                    self.NUM_8_KEY = True
                if event.key == pygame.K_9:
                    self.NUM_9_KEY = True
                if event.key == pygame.K_DELETE:
                    self.REMOVE_KEY = True

    def reset_keys(self):
        self.START_KEY = False
        self.BACK_KEY = False
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.LEFT_KEY = False
        self.RIGHT_KEY = False
        self.NUM_1_KEY = False
        self.NUM_2_KEY = False
        self.NUM_3_KEY = False
        self.NUM_4_KEY = False
        self.NUM_5_KEY = False
        self.NUM_6_KEY = False
        self.NUM_7_KEY = False
        self.NUM_8_KEY = False
        self.NUM_9_KEY = False
        self.REMOVE_KEY = False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.menu_font, size)
        text_surface = font.render(text, True, self.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_sudoku_grid(self):
        gap = self.HEIGHT / 9
        for i in range(10):
            if i % 3 == 0 and i != 0:
                thickness = 3
            else:
                thickness = 1
            pygame.draw.line(self.display, self.BLACK, (0, i*gap),
                             (self.HEIGHT, i*gap), thickness)
            pygame.draw.line(self.display, self.BLACK, (i*gap, 0),
                             (i*gap, self.HEIGHT), thickness)

    def draw_sudoku_boxes(self):
        font = pygame.font.Font(self.sudoku_font, 35)
        gap = self.HEIGHT / 9
        for row in range(9):
            for col in range(9):
                x = col * gap
                y = row * gap
                value = self.solver.state[row][col]
                is_given = self.solver.is_given(row, col)
                if self.move_mode:
                    color = self.GREY_BLUE
                    thickness = 3
                else:
                    color = self.GREEN
                    thickness = 4
                if value != '0' and is_given:
                    text = font.render(value, 1, self.BLACK)
                    self.display.blit(text, (x + (gap/2 - text.get_width()/2),
                                             y + (gap/2 - text.get_height()/2)))
                elif value != '0':
                    text = font.render(value, 1, self.GREY)
                    self.display.blit(text, (x + (gap/2 - text.get_width()/2),
                                             y + (gap/2 - text.get_height()/2)))

                if self.solver.is_selected(row, col):
                    pygame.draw.rect(self.display, color,
                                     (x, y, gap+1, gap+1), thickness)
