from pgzero.builtins import Actor

class Tile(Actor):
    def __init__(self, image, pos, blocks_move=True):
        super().__init__(image, pos, anchor=('left', 'top'))
        self.blocks_move = blocks_move
        
