class Settings:
    def __init__(self, screen_width: int=0, screen_height: int=0) -> None:
        self.title = 'Py Tetris'
        self.dev_name = 'PAC Studios'
        self.assets_root = './tetris/assets'
        self.image_root = f'{self.assets_root}/images'
        self.audio_root = f'{self.assets_root}/audio'
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Block and Tetromino settings
        self.block_size = 32
        self.tetromino_shapes = ["I","O","T","S","Z","J","L",""]

        # Game Speed
        self.fps = 2
        self.fps_max = 60

        self.bg_color = (230,230,230) # White
        # self.bg_color = 'purple'
