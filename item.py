from pgzero.builtins import Actor


class Item:
    def __init__(self, image: str, name: str, type: str, attack: int, defence: int):
        self.image = image
        self.name = name
        self.type = type
        self.attack = attack
        self.defence = defence

    def __repr__(self):
        return "%s" % self.name


class GameItem(Actor):
    def __init__(self, item: Item, pos: tuple):
        super().__init__(item.image, pos, anchor=('left', 'top'))
        self.item = item