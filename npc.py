from pgzero.builtins import Actor


class Npc(Actor):
    def __init__(self, image, pos, hp=1):
        super().__init__(image, pos, anchor=('left', 'top'))
        self.hp = hp
