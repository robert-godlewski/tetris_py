import pygame
import sys
import random

from tetris.settings import Settings
from tetris.gamegrid import GameGrid
from tetris.tetromino.block import Block
from tetris.tetromino.tetromino_base import Tetromino
from tetris.stats import Stats
# from tetris.scoreboard import Scoreboard


class Tetris:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings(screen_width=320, screen_height=640)
        size = (self.settings.screen_width, self.settings.screen_height)
        self.screen = pygame.display.set_mode(size=size)
        pygame.display.set_caption(title=self.settings.title)

        # Setting up the grid for the blocks to fit within
        self.game_grid = GameGrid(self, "32x32BlackGridBlock", width=self.settings.screen_width, height=self.settings.screen_height)

        # Represents the groups of blocks at the bottom
        self.bottom_tetro = Tetromino(self)
        self.bottom_tetro.is_active = False

        # Set up a middle position for the blocks to generate at the top
        mid = round(self.game_grid.columns/2)-1 # This will return the left top position

        # The active tetromino group that's moving
        self.sprite_shape = random.choice(self.settings.tetromino_shapes)
        self.block_base = Block(self, row_pos=0, col_pos=mid, image_name="32x32RedBlockTest") # adjust the settings here
        self.active_tetro = Tetromino(self, self.sprite_shape, self.block_base) # Will need to fix this

        self.stats = Stats(self)
        # self.scoreboard = Scoreboard(self)

    def run_game(self) -> None:
        clock = pygame.time.Clock()
        while True:
            # Need to also check if self.bottom_tetro is moving or not
            # Also need to check if the self.active_tetro is active or not
            self._check_events()
            self.block_base.update() # replace this with active_tetro
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
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.block_base.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.block_base.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.block_base.moving_down = True

    def _check_keyup_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.block_base.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.block_base.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.block_base.moving_down = False

    def _update_screen(self) -> None:
        self.screen.fill(self.settings.bg_color)
        self._fill_grid()
        pygame.display.flip()

    def _fill_grid(self) -> None:
        for r in range(self.game_grid.rows):
            for c in range(self.game_grid.columns):
                self.screen.blit(self.game_grid.grid_map[r][c]['image'], self.game_grid.get_cell_coordinates(r, c))
