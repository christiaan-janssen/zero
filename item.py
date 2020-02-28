
class Item:
    def __init__(self, image: str, name: str, attack: int, defence: int):
        self.image = image
        self.name = name
        self.attack = attack
        self. defence = defence

    def __repr__(self):
        return "%s" % self.name
