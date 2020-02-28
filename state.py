class GameState:
    """ GameState holds the state of the running game """
    def __init__(self):
        self.show_inventory = False
        self.debug = False

    def toggle_inventory(self):
        self.show_inventory = not self.show_inventory
