import pygame

from tetris.tetromino.block import Block


class Tetromino(pygame.sprite.Group):
    def __init__(self, game, shape: str="", *sprites):
        # game = class Tetris
        super().__init__(*sprites)
        self._game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.game_grid = game.game_grid

        self.shape = shape # Might need to do more things here later on
        self.blocks = []
        self.bottom_row = 0

        # Checks to see if the tetromino is moving or not
        self.is_active = True

        # Add in more details here
        # This class will also represent both the different shapes and the base where everything clumps up

    def add_new_block(self, row_pos: int, col_pos: int, image_name: str, image_extension: str="png"):
        block = Block(self._game, row_pos, col_pos, image_name, image_extension)
        self.blocks.append(block)

    def add_block(self, block: Block):
        self.blocks.append(block)

    def remove_block(self):
        if len(self.blocks) > 0:
            return self.blocks.pop() # Returns Block object at the end of the list
        else:
            return None

    def moving_left(self):
        for block in self.blocks:
            block.moving_left = True

    def moving_right(self):
        for block in self.blocks:
            block.moving_right = True

    def moving_down(self):
        for block in self.blocks:
            block.moving_down = True

    def stop_moving_left(self):
        for block in self.blocks:
            block.moving_left = False

    def stop_moving_right(self):
        for block in self.blocks:
            block.moving_right = False

    def stop_moving_down(self):
        for block in self.blocks:
            block.moving_down = False

    def fill(self) -> None:
        # Repeats self.game_grid.fill_cell(...) for the whole group
        mid = round(self.game_grid.columns/2)
        # fix this whole thing

    def rotate(self):
        # Doesn't rotate if it's the base or if it's O shaped
        if self.shape == "O" or self.shape == "": pass
        # Need to do something special for other shapes

    def update(self) -> None: # Fix this to stop all blocks from moving instead of just some that reach the bottom
        for block in self.blocks: block.update()


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
        self.image = '32x32RedBlockTest' # Fix this later
        self.setup()

    def setup(self):
        mid = round(self.game_grid.columns/2)
        self.add_new_block(1, mid-1, self.image) # we are adding in the lowest row first so that it can determine where the Tetromino collides
        self.add_new_block(1, mid, self.image)
        self.add_new_block(0, mid-1, self.image)
        self.add_new_block(0, mid, self.image)
        for block in self.blocks:
            self.game_grid.fill_cell(block.cell, block.cell_rect, block.row_pos, block.col_pos)

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
