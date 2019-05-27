

class GameStats:

    # Game Surface 640x640
    height: int = 640
    width: int = 640
    mod: str = "start_game"
    FONT: int

    def __init__(self):
        raise TypeError("This class only for static use")