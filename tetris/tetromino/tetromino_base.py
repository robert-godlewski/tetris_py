import pygame

from tetris import Tetris
from tetris.tetromino.block import Block


class Tetromino(pygame.sprite.Group):
    def __init__(self, game: Tetris, shape: str="", *sprites):
        super().__init__(*sprites)
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.game_grid = game.game_grid

        self.shape = shape # Might need to do more things here later on
        self.blocks = sprites # len(sprites) = 4

        # Add in more details here
        # This class will also represent both the different shapes and the base where everything clumps up

    def fill(self):
        pass

    def rotate(self):
        pass

    def update(self) -> None:
        for block in self.blocks: self._update_movement(block)

    def _update_movement(self, block: Block):
        # 1. Drop down by one grid point or stay
        # 2. Move left/right/down based on user input
        pass


# Shapes:
'''
I pos 1 = [.,.,.,.,.,.]
          [.,.,.,.,.,.]
          [.,I,I,I,I,.]
          [.,.,.,.,.,.]

I pos 2 = [.,.,.,.,.,.]
          [.,.,I,.,.,.]
          [.,.,I,.,.,.]
          [.,.,I,.,.,.]
          [.,.,I,.,.,.]
          [.,.,.,.,.,.]
'''
class Iblock(Tetromino):
    def __init__(self, game, block, *sprites): # need to fix the block variable
        super().__init__(game, block, "I", *sprites)

'''
O = [.,O,O,.]
    [.,O,O,.]
'''
class Oblock(Tetromino):
    # No need for the rotate function
    def __init__(self, game, *sprites): # need to fix the block variable
        super().__init__(game, "O", *sprites)
        # Initial position of the sprites
        mid = round(self.game_grid.columns/2)
        self.game_grid.fill_cell(self.blocks[0].cell, self.blocks[0].cell_rect, 0, mid-1)
        self.game_grid.fill_cell(self.blocks[1].cell, self.blocks[1].cell_rect, 0, mid)
        self.game_grid.fill_cell(self.blocks[2].cell, self.blocks[2].cell_rect, self.game_grid.block_size, mid-1)
        self.game_grid.fill_cell(self.blocks[3].cell, self.blocks[3].cell_rect, self.game_grid.block_size, mid)

'''
T pos 1 = [.,.,.,.,.]
          [.,T,T,T,.]
          [.,.,T,.,.]
          [.,.,.,.,.]

T pos 2 = [.,.,.,.,.]
          [.,.,T,.,.]
          [.,.,T,T,.]
          [.,.,T,.,.]
          [.,.,.,.,.]

T pos 3 = [.,.,.,.,.]
          [.,.,T,.,.]
          [.,T,T,T,.]
          [.,.,.,.,.]

T pos 4 = [.,.,.,.,.]
          [.,.,T,.,.]
          [.,T,T,.,.]
          [.,.,T,.,.]
          [.,.,.,.,.]
'''
class Tblock(Tetromino):
    def __init__(self, game, block, *sprites): # need to fix the block variable
        super().__init__(game, block, "T", *sprites)

'''
S pos 1 = [.,.,.,.,.]
          [.,.,S,S,.]
          [.,S,S,.,.]
          [.,.,.,.,.]

S pos 2 = [.,.,.,.,.]
          [.,S,.,.,.]
          [.,S,S,.,.]
          [.,.,S,.,.]
          [.,.,.,.,.]
'''
class Sblock(Tetromino):
    def __init__(self, game, block, *sprites): # need to fix the block variable
        super().__init__(game, block, "S", *sprites)

'''
Z pos 1 = [.,.,.,.,.]
          [.,Z,Z,.,.]
          [.,.,Z,Z,.]
          [.,.,.,.,.]

Z pos 2 = [.,.,.,.,.]
          [.,.,.,Z,.]
          [.,.,Z,Z,.]
          [.,.,Z,.,.]
          [.,.,.,.,.]
'''
class Zblock(Tetromino):
    def __init__(self, game, block, *sprites): # need to fix the block variable
        super().__init__(game, block, "Z", *sprites)

'''
J pos 1 = [.,.,.,.,.]
          [.,J,J,J,.]
          [.,.,.,J,.]
          [.,.,.,.,.]

J pos 2 = [.,.,.,.,.]
          [.,.,.,J,.]
          [.,.,.,J,.]
          [.,.,J,J,.]
          [.,.,.,.,.]

J pos 3 = [.,.,.,.,.]
          [.,J,.,.,.]
          [.,J,J,J,.]
          [.,.,.,.,.]

J pos 4 = [.,.,.,.,.]
          [.,J,J,.,.]
          [.,J,.,.,.]
          [.,J,.,.,.]
          [.,.,.,.,.]
'''
class Jblock(Tetromino):
    def __init__(self, game, block, *sprites): # need to fix the block variable
        super().__init__(game, block, "J", *sprites)

'''
L pos 1 = [.,.,.,.,.]
          [.,L,L,L,.]
          [.,L,.,.,.]
          [.,.,.,.,.]

L pos 2 = [.,.,.,.,.]
          [.,L,.,.,.]
          [.,L,.,.,.]
          [.,L,L,.,.]
          [.,.,.,.,.]

L pos 3 = [.,.,.,.,.]
          [.,.,.,L,.]
          [.,L,L,L,.]
          [.,.,.,.,.]

L pos 4 = [.,.,.,.,.]
          [.,.,L,L,.]
          [.,.,.,L,.]
          [.,.,.,L,.]
          [.,.,.,.,.]
'''
class Lblock(Tetromino):
    def __init__(self, game, block, *sprites): # need to fix the block variable
        super().__init__(game, block, "L", *sprites)
