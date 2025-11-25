import pygame

from tetris import Tetris


class Block(pygame.sprite.Sprite):
    def __init__(self, game: Tetris) -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        '''Will need to either:
        * randomly generate actual specifically designed blocks or 
        * make separate classes and have the game randomly choose which block to use
        '''
        # Maybe update this entire class to alternate between the different test blocks
        self.image = pygame.image.load('./tetris/assets/32x32BlackBlockTest.png')
        self.rect = self.image.get_rect()

        # Positioning variables:
        # Starting point
        self.rect.midtop = self.screen_rect.midtop
        # Movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        # Checking to see if it has reached the bottom to generate a new one
        self.reached_bottom = False

    def update_movement(self) -> None:
        # Might need to doctor things up so that the movement is based on a grid
        if self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.drop_speed
        else:
            self.reached_bottom = True
        if not self.reached_bottom:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.lr_speed
            if self.moving_left and self.rect.left > 0:
                self.x -= self.settings.lr_speed
            if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
                self.y += self.settings.drop_speed * 2
        # Need to add in a rotation object feature
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self) -> None:
        self.screen.blit(self.image, self.rect)
