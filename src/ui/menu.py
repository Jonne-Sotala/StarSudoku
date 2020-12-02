import pygame
from ui.popup import Popup


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

    def draw_logged_in_user(self):
        self.game.draw_text(
            f"logged in as {self.game.users.current_user}", 10, 10, 10, align='topleft')

    def draw_logo(self):
        image = pygame.image.load("resources/images/logo.png")
        self.game.display.blit(image, (self.logo_x, self.logo_y))

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class LoginMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = 0
        self.users = self.game.users.get_all()
        self.new_user_x, self.new_user_y = self.MID_W, self.MID_H+100
        self.cursor_rect.midtop = (
            self.new_user_x + self.offset, self.new_user_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BEIGE)
            self.game.draw_text('Welcome', 35,
                                self.MID_W, self.MID_H - 200)
            self.draw_logo()
            self.game.draw_text('Create new user', 25,
                                self.MID_W, self.MID_H+100)
            pygame.draw.line(self.game.display, self.game.BLACK,
                             (self.MID_W-190, self.MID_H+125),
                             (self.MID_W+190, self.MID_H+125), 3)
            self.draw_users()
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            self.state += 1
            if self.state > len(self.users):
                self.state = 0
        if self.game.UP_KEY:
            self.state -= 1
            if self.state < 0:
                self.state = len(self.users)

        if self.state == 0:
            self.cursor_rect.midtop = (
                self.MID_W + self.offset, self.new_user_y)
        else:
            self.cursor_rect.midtop = (
                self.MID_W + self.offset, self.MID_H + 110 + 35*self.state)

    def draw_users(self):
        for i, user in enumerate(self.users, start=1):
            self.game.draw_text(user.username, 25,
                                self.MID_W, self.MID_H + 110 + 35*i)

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 0 and len(self.users) < 4:
                self.run_display = False
                self.game.current_menu = self.game.create_user_menu
            elif self.state == 0 and len(self.users) >= 4:
                self.run_display = False
                self.game.current_menu = Popup(
                    self.game, self, "Max 4 users", "press del to delete", True)
            else:
                self.game.users.login(self.users[self.state-1].id)
                self.run_display = False
                self.game.current_menu = self.game.main_menu
        if self.game.REMOVE_KEY and self.state > 0:
            self.game.users.remove_user(self.users[self.state-1].id)
            self.users = self.game.users.get_all()
            if self.state > len(self.users):
                self.state = len(self.users)


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
            self.game.draw_text(f'Main Menu', 35,
                                self.game.WIDTH / 2,
                                self.game.HEIGHT / 2 - 200)
            self.game.draw_text("Choose Puzzle", 30,
                                self.choose_x, self.choose_y)
            self.game.draw_text("History", 30, self.history_x, self.history_y)
            self.game.draw_text("Credits", 30, self.credits_x, self.credits_y)
            self.draw_logged_in_user()
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
        if self.game.BACK_KEY:
            self.game.users.logout()
            self.game.current_menu = self.game.login_menu
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
            self.draw_logged_in_user()
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
            self.draw_logged_in_user()
            self.blit_screen()
