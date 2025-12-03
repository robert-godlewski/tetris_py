class Settings:
    def __init__(self, screen_width: int=0, screen_height: int=0) -> None:
        self.title = 'Py Tetris'
        self.dev_name = 'PAC Studios'
        self.assets_root = './tetris/assets'
        self.image_root = f'{self.assets_root}/images'
        self.audio_root = f'{self.assets_root}/audio'
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fps = 60
        self.block_size = 32
        self.lr_speed = 6 # Left/ Right movement for blocks
        # Fix the formula for the speed
        # * Increase speed if there are a stack of blocks
        # * Decrease speed based on the number of block rows removed
        self.drop_speed = 1

        self.bg_color = (230,230,230) # White
        # self.bg_color = 'purple'
