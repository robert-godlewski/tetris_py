import pygame


class Tetris:
    def __init__(self):
        pygame.init()
        self.settings = Settings(screen_width=1280, screen_height=720)
        size = (self.settings.screen_width, self.settings.screen_height)
        self.screen = pygame.display.set_mode(size=size)
        pygame.display.set_caption(title='Py Tetris')

    def run_game(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill('purple')
            pygame.display.flip()
            clock.tick(self.settings.fps)
        pygame.quit()


class Settings:
    def __init__(self, screen_width=None, screen_height=None):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fps = 60
