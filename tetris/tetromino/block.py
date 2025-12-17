import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, game, row_pos: int, col_pos: int, image_name: str, image_extension: str="png") -> None:
        # game = class Tetris
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
        # Markers to check to move besides the basic drop
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        # Checking to see if it has reached the bottom to generate a new one
        self.reached_bottom = False

    def update(self) -> None:
        self.game_grid.clear_cell(self.row_pos, self.col_pos)
        if self.row_pos+1 < self.game_grid.rows:
            self.row_pos += 1
        else:
            self.reached_bottom = True
        if not self.reached_bottom:
            if self.moving_right and self.col_pos+1 < self.game_grid.columns:
                self.col_pos += 1
            if self.moving_left and self.col_pos-1 >= 0:
                self.col_pos -= 1
            if self.moving_down and self.row_pos+1 < self.game_grid.rows:
                self.row_pos += 1
        self.game_grid.fill_cell(self.cell, self.cell_rect, self.row_pos, self.col_pos)

    def blitme(self) -> None:
        self.screen.blit(self.cell, self.cell_rect)
