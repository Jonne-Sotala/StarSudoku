import pygame
import string
from entities.user import User


class Popup:
    def __init__(self, game, prev_menu, message, options='', allow_start_key=False):
        self.game = game
        self.prev_menu = prev_menu
        self.run_display = True
        self.message = message
        self.options = options
        self.allow_start_key = allow_start_key
        self.MID_W = self.game.WIDTH / 2
        self.MID_H = self.game.HEIGHT / 2
        self.LIGHTBEIGE = (239, 231, 219)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.draw_popup()
            self.draw_popup_text()
            self.game.window.blit(self.game.display, (0, 0))
            pygame.display.update()
            self.game.reset_keys()

    def check_input(self):
        if self.allow_start_key:
            if self.game.START_KEY or self.game.BACK_KEY:
                self.run_display = False
                self.game.current_menu = self.prev_menu
        elif self.game.YES_KEY:
            self.game.confirm = True
            self.run_display = False
            self.game.current_menu = self.prev_menu
        elif self.game.NO_KEY:
            self.game.confirm = False
            self.run_display = False
            self.game.current_menu = self.prev_menu

    def draw_popup(self):
        pygame.draw.rect(self.game.display, self.LIGHTBEIGE,
                         (200, 200, 400, 200), border_radius=30)
        pygame.draw.rect(self.game.display, self.game.BLACK,
                         (200, 200, 400, 200), 4, border_radius=30)

    def draw_popup_text(self, message=None, options=None):
        if message is None:
            message = self.message
        if options is None:
            options = self.options
        self.game.draw_text(message, 23,
                            self.MID_W, self.MID_H - 35)
        self.game.draw_text(options, 20,
                            self.MID_W, self.MID_H + 35)


class CreateUserPopUp(Popup):
    def __init__(self, game, message):
        super().__init__(game, game.login_menu, message)
        self.username = ''

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.check_events()
            self.draw_popup()
            self.draw_popup_text(options=self.username)
            self.game.window.blit(self.game.display, (0, 0))
            pygame.display.update()
            self.game.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(self.username) > 0:
                        self.game.users.create_user(self.username)
                        self.game.login_menu.users = self.game.users.get_all()
                        self.username = ''
                    self.run_display = False
                    self.game.current_menu = self.prev_menu
                elif event.key == pygame.K_BACKSPACE:
                    if len(self.username) == 0:
                        self.run_display = False
                        self.game.current_menu = self.prev_menu
                    else:
                        self.username = self.username[:-1]
                else:
                    char = event.unicode
                    if char in string.ascii_letters or char in string.digits:
                        if len(self.username) < 10:
                            self.username += char
