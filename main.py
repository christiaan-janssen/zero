import pgzrun
import yaml


from pgzero.builtins import *
from map import GameMap
from player import Player
from state import GameState
from item import Item

WIDTH = 600
HEIGHT = 400

SPRITE_SIZE = 16
SCREEN_ROWS = WIDTH // SPRITE_SIZE
MAP_WIDTH = 35
MAP_HEIGHT = 18
OFFSET = 4

DEBUG = False

game_state = GameState()
player = Player('player', OFFSET+SPRITE_SIZE, OFFSET+SPRITE_SIZE)
game_map = GameMap(MAP_WIDTH, MAP_HEIGHT)
game_items = []


# Handle player movement
def on_key_up(key) -> None:
    if key == keys.RIGHT:
        player.x += 16
    if key == keys.LEFT:
        player.x -= 16
    if key == keys.UP:
        player.y -= 16
    if key == keys.DOWN:
        player.y += 16
    if key == keys.A:
        player.hp -= 1
    if key == keys.D:
        player.hp += 1
    if key == keys.I:
        game_state.toggle_inventory()


def draw() -> None:
    screen.fill((71, 45, 60))
    game_map.draw()
    player.draw()
    draw_ui()
    if game_state.show_inventory:
        draw_inventory()


# load items
def load_items() -> None:
    with open("items.yaml", 'r') as stream:
        item_data = yaml.safe_load(stream)

    for item in item_data:
        game_items.append(Item(
            item_data[item]['image'],
            item_data[item]['name'],
            item_data[item]['stats']['attack'],
            item_data[item]['stats']['defence']
        ))



# UI
def draw_ui() -> None:
    """Draw the game ui"""
    # Corners:
    screen.blit('menu/corner_top_left', (OFFSET, 18*SPRITE_SIZE))
    screen.blit('menu/corner_top_right', (36*SPRITE_SIZE+OFFSET, 18*SPRITE_SIZE))
    screen.blit('menu/corner_bottom_left', (OFFSET, 24*SPRITE_SIZE))
    screen.blit('menu/corner_bottom_right', (36*SPRITE_SIZE+OFFSET, 24*SPRITE_SIZE))

    # Horizontal lines
    for x in range(35):
        screen.blit('menu/menu_straight_h', (x*SPRITE_SIZE+OFFSET+SPRITE_SIZE, 18*SPRITE_SIZE))
        screen.blit('menu/menu_straight_h', (x*SPRITE_SIZE+OFFSET+SPRITE_SIZE, 24*SPRITE_SIZE))

    # Vertical lines
    for y in range(5):
        screen.blit('menu/menu_straight', (OFFSET, 18*SPRITE_SIZE+y*SPRITE_SIZE+SPRITE_SIZE))
        screen.blit('menu/menu_straight', (36*SPRITE_SIZE+OFFSET, 18*SPRITE_SIZE+y*SPRITE_SIZE+SPRITE_SIZE))

    for i in range(player.hp):
        screen.blit('menu/heart', (i*SPRITE_SIZE+OFFSET+30*SPRITE_SIZE, 19*16))

    # UI Text
    screen.blit('h', (SPRITE_SIZE+OFFSET+22*SPRITE_SIZE, 19*16))
    screen.blit('e', (SPRITE_SIZE+OFFSET+23*SPRITE_SIZE, 19*16))
    screen.blit('a', (SPRITE_SIZE+OFFSET+24*SPRITE_SIZE, 19*16))
    screen.blit('l', (SPRITE_SIZE+OFFSET+25*SPRITE_SIZE, 19*16))
    screen.blit('t', (SPRITE_SIZE+OFFSET+26*SPRITE_SIZE, 19*16))
    screen.blit('h', (SPRITE_SIZE+OFFSET+27*SPRITE_SIZE, 19*16))
    screen.blit('coln', (SPRITE_SIZE+OFFSET+28*SPRITE_SIZE, 19*16))


def draw_inventory() -> None:
    _START_X = 4*SPRITE_SIZE+OFFSET
    _START_Y = 2*SPRITE_SIZE+OFFSET
    _INV_WIDTH = 29*SPRITE_SIZE
    _INV_HEIGHT = 20*SPRITE_SIZE
    # Create a back ground for the inventory, Rect takes
    screen.draw.filled_rect(Rect(_START_X, _START_Y, _INV_WIDTH, _INV_HEIGHT), (71, 45, 60))

    screen.blit('menu/corner_top_left', (_START_X, _START_Y))
    screen.blit('menu/corner_top_right', (_START_X+_INV_WIDTH-SPRITE_SIZE, _START_Y))
    screen.blit('menu/corner_bottom_left', (_START_X, _START_Y+_INV_HEIGHT-SPRITE_SIZE))
    screen.blit('menu/corner_bottom_right', (_START_X+_INV_WIDTH-SPRITE_SIZE, _START_Y+_INV_HEIGHT-SPRITE_SIZE))


load_items()
print(game_items)
pgzrun.go()
