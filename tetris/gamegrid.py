import pygame

from tetris import Tetris


class GameGrid:
    def __init__(self, game: Tetris, image_name: str, image_extension: str="png", width: int=32, height: int=32) -> None:
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        grid_path = f'{self.settings.image_root}/{image_name}.{image_extension}'
        self.grid = pygame.image.load(grid_path)
        self.grid_rect = self.grid.get_rect()

        # Building out the grid
        self.width = width
        self.height = height
        self.block_size = game.settings.block_size
        self.rows = round(self.height/self.block_size)
        self.columns = round(self.width/self.block_size)
        column_arr = [{'image': self.grid, 'rect': self.grid_rect} for _ in range(self.columns)]
        self.grid_map = [column_arr for _ in range(self.rows)]

    def fill_grid(self, image, image_rect, row_pos: int, col_pos: int) -> None:
        self.grid_map[row_pos][col_pos] = {
            'image': image, 
            'rect': image_rect
        }

    def clear_grid(self, row_pos: int, col_pos: int) -> None:
        self.grid_map[row_pos[col_pos]] = {
            'image': self.grid, 
            'rect': self.grid_rect
        }

    def blitme(self) -> None:
        for r in self.grid_map:
            for c in self.grid_map[r]:
                self.screen.blit(self.grid_map[r][c]['image'],self.grid_map[r][c]['rect']) # Could also be self.screen.fill() instead
