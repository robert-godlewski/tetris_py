import pygame

from tetris import Tetris


class Block(pygame.sprite.Sprite):
    def __init__(self, game: Tetris, shape: str, image_name: str, image_extension: str="png") -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.game_grid = game.game_grid

        self.shape = shape
        image_path = f'{self.settings.image_root}/{image_name}.{image_extension}'
        self.cell = pygame.image.load(image_path)
        self.cell_rect = self.cell.get_rect()
        # Will need to generate the different shapes off of 4 cells clumped together in a specific shape

        # Positioning variables
        # Starting point - Fix this based on all shapes instead
        mid = round(self.game_grid.columns/2)
        self.game_grid.fill_cell(self.cell, self.cell_rect, 0, mid-1)
        # self.cell_rect.midtop = self.screen_rect.midtop
        # Movement
        self.x = float(self.cell_rect.x)
        self.y = float(self.cell_rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        # Checking to see if it has reached the bottom to generate a new one
        self.reached_bottom = False

    def update_movement(self) -> None:
        # Might need to doctor things up so that the movement is based on a grid
        if self.cell_rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.drop_speed
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
'''
O = [.,O,O,.]
    [.,O,O,.]
'''
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
# class Lblock(Block):
#     def __init__(self, game: Tetris) -> None:
#         super().__init__(game, "32x32BlackBlockTest")
