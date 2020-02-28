from pgzero.builtins import Actor
import random


class Player(Actor):
    def __init__(self, image: str, x: int, y: int, hp: int = 5):
        super().__init__(image, (x, y), anchor=('left', 'top'))
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.image = image
        self.hp = hp
        self.power = 1
        self.defence = 1
        self.helm = None
        self.sword = None
        self.inventory = []

    def take_damage(self, amount: int) -> None:
        raise NotImplementedError

    def attack(self) -> int:
        raise NotImplementedError


