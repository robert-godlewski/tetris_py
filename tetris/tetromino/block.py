import pygame

from tetris import Tetris


class Block(pygame.sprite.Sprite):
    def __init__(self, game: Tetris, row_pos: int, col_pos: int, image_name: str, image_extension: str="png") -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.game_grid = game.game_grid

        image_path = f'{self.settings.image_root}/{image_name}.{image_extension}'
        self.cell = pygame.image.load(image_path)
        self.cell_rect = self.cell.get_rect()
        # Will need to generate the different shapes off of 4 cells clumped together in a specific shape

        # Positioning variables
        self.row_pos = row_pos # Grid row position
        self.col_pos = col_pos # Grid column position
        # Starting point
        self.game_grid.fill_cell(self.cell, self.cell_rect, self.row_pos, self.col_pos)
        # mid = round(self.game_grid.columns/2)
        # self.game_grid.fill_cell(self.cell, self.cell_rect, 0, mid-1)
        # self.cell_rect.midtop = self.screen_rect.midtop
        # Movement
        # self.x = float(self.cell_rect.x)
        # self.x = int(self.cell_rect.x)
        # self.y = float(self.cell_rect.y)
        # self.y = int(self.cell_rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        # Checking to see if it has reached the bottom to generate a new one
        self.reached_bottom = False

    def update_movement(self) -> None:
        # Actual Movements
        if self.cell_rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.drop_speed
            # self.y += self.game_grid.block_size # not sure if this is right
        else:
            self.reached_bottom = True
        if not self.reached_bottom:
            if self.moving_right and self.cell_rect.right < self.screen_rect.right:
                self.x += self.settings.lr_speed
            if self.moving_left and self.cell_rect.left > 0:
                self.x -= self.settings.lr_speed
            if self.moving_down and self.cell_rect.bottom <= self.screen_rect.bottom:
                self.y += self.settings.drop_speed * 2
        # Need to add in a rotation object feature
        self.cell_rect.x = self.x
        self.cell_rect.y = self.y

    def blitme(self) -> None:
        self.screen.blit(self.cell, self.cell_rect)
