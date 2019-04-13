from Pong.Player.PlayerRacket import PlayerRacket


class Player:
    def __init__(self, color, posize, limit):
        self.racket = PlayerRacket(color, posize, limit)

    def update(self, surface):
        self.racket.draw(surface)

    def up(self):
        self.racket.moveUp()

    def down(self):
        self.racket.moveDown()
# A player Class and file to store all player related stuff. For starters
# I am going to take PlayerRacket to here and implement Goal. Then in Player Class
# I will make composition with them. After that I hope main will be much more clear for
# new tools such as menu screen, multiplayer and etc.
