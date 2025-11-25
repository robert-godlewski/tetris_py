import pygame
import sys

from tetris.settings import Settings


class Tetris:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings(screen_width=1280, screen_height=720)
        size = (self.settings.screen_width, self.settings.screen_height)
        self.screen = pygame.display.set_mode(size=size)
        pygame.display.set_caption(title=self.settings.title)

        from tetris.block import Block
        self.test_block = Block(self)

    def run_game(self) -> None:
        clock = pygame.time.Clock()
        while True:
            self._check_events()
            # Need to fix the movement generation and mechanics here:
            # * Check to see if the current block has reached the bottom or not
            # * if it has then update the movement of the current block
            # * otherwise check to see if there's a full row of existing blocks at any level
            # ** if there's a full row clear those blocks and move everything that doesn't have a full row down quickly and decrease the level by the number of cleared rows.
            # ** ...as reached the bottom/ other block then check to see if there's a full row
            self.test_block.update_movement()
            self._update_screen()
            clock.tick(self.settings.fps)

    def _check_events(self) -> None:
        # Need to check if the level is high enough to automatically "GAMEOVER"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.test_block.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.test_block.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.test_block.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.test_block.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.test_block.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.test_block.moving_down = False

    def _update_screen(self) -> None:
        self.screen.fill(self.settings.bg_color)
        self.test_block.blitme()
        pygame.display.flip()
