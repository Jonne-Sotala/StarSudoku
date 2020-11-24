import pygame


class Menu:
    def __init__(self, game):
        self.game = game
        self.MID_W = self.game.WIDTH / 2
        self.MID_H = self.game.HEIGHT / 2
        self.logo_x, self.logo_y = self.MID_W - 64, self.MID_H - 100
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -200

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def draw_logo(self):
        image = pygame.image.load("resources/images/logo.png")
        self.game.display.blit(image, (self.logo_x, self.logo_y))

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "Choose"
        self.choose_x, self.choose_y = self.MID_W, self.MID_H + 100
        self.history_x, self.history_y = self.MID_W, self.MID_H + 150
        self.credits_x, self.credits_y = self.MID_W, self.MID_H + 200
        self.cursor_rect.midtop = (self.choose_x + self.offset, self.choose_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BEIGE)
            self.draw_logo()
            self.game.draw_text('Main Menu', 35,
                                self.game.WIDTH / 2,
                                self.game.HEIGHT / 2 - 200)
            self.game.draw_text("Choose Puzzle", 30,
                                self.choose_x, self.choose_y)
            self.game.draw_text("History", 30, self.history_x, self.history_y)
            self.game.draw_text("Credits", 30, self.credits_x, self.credits_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Choose':
                self.cursor_rect.midtop = (
                    self.history_x + self.offset, self.history_y)
                self.state = 'History'
            elif self.state == 'History':
                self.cursor_rect.midtop = (
                    self.credits_x + self.offset, self.credits_y)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (
                    self.choose_x + self.offset, self.choose_y)
                self.state = 'Choose'

        if self.game.UP_KEY:
            if self.state == 'Choose':
                self.cursor_rect.midtop = (
                    self.credits_x + self.offset, self.credits_y)
                self.state = 'Credits'
            elif self.state == 'History':
                self.cursor_rect.midtop = (
                    self.choose_x + self.offset, self.choose_y)
                self.state = 'Choose'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (
                    self.history_x + self.offset, self.history_y)
                self.state = 'History'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Choose':
                self.game.current_menu = self.game.difficulty_menu
            elif self.state == 'History':
                pass
            elif self.state == 'Credits':
                self.game.current_menu = self.game.credits_menu
            self.run_display = False


class DifficultyMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = 'Easy'
        self.easy_x, self.easy_y = self.MID_W, self.MID_H + 100
        self.medium_x, self.medium_y = self.MID_W, self.MID_H + 150
        self.hard_x, self.hard_y = self.MID_W, self.MID_H + 200
        self.cursor_rect.midtop = (self.easy_x + self.offset, self.easy_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BEIGE)
            self.draw_logo()
            self.game.draw_text('Choose Difficulty', 35,
                                self.game.WIDTH / 2,
                                self.game.HEIGHT / 2 - 200)
            self.game.draw_text('Easy', 30, self.easy_x, self.easy_y)
            self.game.draw_text('Medium', 30, self.medium_x, self.medium_y)
            self.game.draw_text('Hard', 30, self.hard_x, self.hard_y)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.current_menu = self.game.main_menu
            self.run_display = False
        elif self.game.DOWN_KEY:
            if self.state == 'Easy':
                self.cursor_rect.midtop = (
                    self.medium_x + self.offset, self.medium_y)
                self.state = 'Medium'
            elif self.state == 'Medium':
                self.cursor_rect.midtop = (
                    self.hard_x + self.offset, self.hard_y)
                self.state = 'Hard'
            elif self.state == 'Hard':
                self.cursor_rect.midtop = (
                    self.easy_x + self.offset, self.easy_y)
                self.state = 'Easy'
        elif self.game.UP_KEY:
            if self.state == 'Easy':
                self.cursor_rect.midtop = (
                    self.hard_x + self.offset, self.hard_y)
                self.state = 'Hard'
            elif self.state == 'Medium':
                self.cursor_rect.midtop = (
                    self.easy_x + self.offset, self.easy_y)
                self.state = 'Easy'
            elif self.state == 'Hard':
                self.cursor_rect.midtop = (
                    self.medium_x + self.offset, self.medium_y)
                self.state = 'Medium'
        elif self.game.START_KEY:
            # TO-DO: Go to the sudoku puzzle list
            # Currently just opens a predetermined sudoku puzzle
            self.run_display = False
            self.game.solving = True


class CreditsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.current_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BEIGE)
            self.game.draw_text('Credits', 40, self.game.WIDTH / 2,
                                self.game.HEIGHT / 2)
            self.blit_screen()
