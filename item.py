
class Item:
    def __init__(self, image, name, attack=0, defence=0):
        self.image = image
        self.name = name
        self.attack = attack
        self. defence = defence

    def __repr__(self):
        return "%s" % self.name
