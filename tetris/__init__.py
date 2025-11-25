import pygame
import sys


class Tetris:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings(screen_width=1280, screen_height=720)
        size = (self.settings.screen_width, self.settings.screen_height)
        self.screen = pygame.display.set_mode(size=size)
        pygame.display.set_caption(title='Py Tetris')

        self.test_block = TetrisBlock(self)

    def run_game(self) -> None:
        clock = pygame.time.Clock()
        while True:
            self._check_events()
            # self.screen.fill(self.settings.bg_color)
            # self.test_block.blitme()
            # pygame.display.flip()
            self.test_block.update_movement()
            self._update_screen()
            clock.tick(self.settings.fps)

    def _check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self) -> None:
        self.screen.fill(self.settings.bg_color)
        self.test_block.blitme()
        pygame.display.flip()


# Move to new files for classes below
class Settings:
    def __init__(self, screen_width=None, screen_height=None) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fps = 60
        self.drop_speed = 1

        # self.bg_color = (230,230,230)
        self.bg_color = 'purple'

class TetrisBlock:
    def __init__(self, game: Tetris) -> None:
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Will need to actually get the image for the blocks
        self.image = pygame.image.load('./tetris/assets/32x32BlackBlockTest.png')
        self.rect = self.image.get_rect()

        # To start roughly near the top and then move down
        self.rect.midtop = self.screen_rect.midtop

        # Movement variables
        self.y = float(self.rect.y)

    def update_movement(self) -> None:
        if self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.drop_speed
        # Might need to update some other things later on
        self.rect.y = self.y

    def blitme(self) -> None:
        self.screen.blit(self.image, self.rect)
