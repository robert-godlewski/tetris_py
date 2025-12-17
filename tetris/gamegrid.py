import pygame


class GameGrid:
    def __init__(self, game, image_name: str, image_extension: str="png", width: int=32, height: int=32) -> None:
        # game = class Tetris
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
        self.grid_map = [[
            {
                'image': self.grid, 
                'rect': self.grid_rect
            } for _ in range(self.columns)
        ] for _ in range(self.rows)] # Might need to fix this because I'm not sure if we really need 'rect' at all

    def get_cell_coordinates(self, row_pos: int, col_pos: int) -> tuple:
        x = col_pos * self.block_size
        y = row_pos * self.block_size
        return (x, y)

    def check_cell_collision(self, row_pos: int, col_pos: int) -> bool:
        if self.grid_map[row_pos][col_pos]['image'] == self.grid:
            return True # There's a collision
        else:
            return False # No collision

    def fill_cell(self, image, image_rect, row_pos: int, col_pos: int) -> None:
        self.grid_map[row_pos][col_pos] = {
            'image': image, 
            'rect': image_rect
        }

    def clear_cell(self, row_pos: int, col_pos: int) -> None:
        self.grid_map[row_pos][col_pos] = {
            'image': self.grid, 
            'rect': self.grid_rect
        }

    def check_row(self, row_pos: int) -> bool:
        for col in range(self.rows):
            if self.grid_map[row_pos][col]['image'] is self.grid:
                return False
        return True
