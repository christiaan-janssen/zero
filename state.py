class GameState:
    """ GameState holds the state of the running game """
    def __init__(self):
        self.show_inventory = False
        self.draw_popup = False
        self.debug = False
        self.popup_msg = "Test Msg"

    def toggle_inventory(self) -> None:
        self.show_inventory = not self.show_inventory

    def toggle_popup(self) -> None:
        self.draw_popup = not self.draw_popup