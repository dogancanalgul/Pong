class Player:
    pass
# A player Class and file to store all player related stuff. For starters
# I am going to take PlayerRacket to here and implement Goal. Then in Player Class
# I will make composition with them. After that I hope main will be much more clear for
# new tools such as menu screen, multiplayer and etc.


class Goal:
    def __init__(self, posize):
        self.posize = posize