import pygame
from menu import MainMenu, DifficultyMenu, CreditsMenu


class SudokuGame:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # State variables
        self.running = True
        self.solving = False

        # KEYS
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False

        # Define contant variables
        self.WIDTH = 800
        self.HEIGHT = 600
        self.BEIGE = (225, 198, 153)
        self.BLACK = (0, 0, 0)

        # Surface
        self.display = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Caption
        caption = 'Sudoku'
        pygame.display.set_caption(caption)

        # Font
        self.font_name = 'resources/8-BIT WONDER.TTF'

        # Menus
        self.main_menu = MainMenu(self)
        self.difficulty_menu = DifficultyMenu(self)
        self.credits_menu = CreditsMenu(self)
        self.current_menu = self.main_menu

    def solving_sudoku(self):
        while self.solving:
            self.check_events()
            if self.START_KEY:
                self.solving = False
            self.display.fill(self.BEIGE)
            self.draw_text("Solving Sudoku puzzle", 30,
                           self.WIDTH/2, self.HEIGHT/2)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.solving = False, False
                self.current_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.START_KEY = False
        self.BACK_KEY = False
        self.DOWN_KEY = False
        self.UP_KEY = False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
