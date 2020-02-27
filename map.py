from pgzero.builtins import *
from tile import Tile


class GameMap:
    """ GameMap holds the current game map """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.generate_map()
        
    def generate_map(self):
        game_map = [[Tile('floor_02', (x*16+16+4, y*16+4)) for y in range(self.height)]
                    for x in range(self.width)]
        
        return game_map

    def draw(self):
        for x in range(self.width):
            for y in range(self.height-1):
                self.tiles[x][y].draw()
