from pgzero.builtins import Actor


class Player(Actor):
    def __init__(self, image, x, y, hp=5):
        super().__init__(image, (x,y),anchor=('left', 'top'))
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.image = image
        self.hp = hp
