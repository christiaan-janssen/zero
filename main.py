import pgzrun
import yaml


from pgzero.builtins import *
from map import GameMap
from player import Player
from npc import Npc
from state import GameState
from item import Item, GameItem

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
orc = Npc('orc_01', (OFFSET+15*SPRITE_SIZE, OFFSET+12*SPRITE_SIZE))
npcs = [orc]

game_map = GameMap(MAP_WIDTH, MAP_HEIGHT)
game_items = []


# Handle player movement
def on_key_up(key) -> None:
    if key == keys.RIGHT:
        move_player('right')
    if key == keys.LEFT:
        move_player('left')
    if key == keys.UP:
        move_player('up')
    if key == keys.DOWN:
        move_player('down')
    if key == keys.A:
        player.hp -= 1
    if key == keys.D:
        player.hp += 1
    if key == keys.P:
        game_state.toggle_popup()
    if key == keys.I:
        game_state.toggle_inventory()
    if key == keys.E:
        pickup_item()


def update():
    for item in ingame_items:
        if player.pos == item.pos:
            game_state.popup_msg = item.item.name
            game_state.draw_popup = True


def draw() -> None:
    screen.fill((71, 45, 60))
    game_map.draw()
    for item in ingame_items:
        item.draw()
    player.draw()
    for npc in npcs:
        npc.draw()
    draw_ui()
    if game_state.draw_popup:
        draw_popup_message()
    if game_state.show_inventory:
        draw_inventory()


def move_player(move):
    if game_state.draw_popup:
        game_state.toggle_popup()
    if move == 'left':
        check_collision(player, 'left')
        player.x -= 16
    if move == 'right':
        check_collision(player, 'right')
        player.x += 16
    if move == 'up':
        check_collision(player, 'up')
        player.y -= 16
    if move == 'down':
        check_collision(player, 'down')
        player.y += 16

    for npc in npcs:
        move_npc(npc)


def check_collision(actor, direction):
    if direction == 'left':
        x = actor.x - 16
        y = actor.y
    if direction == 'right':
        x = actor.x + 16
        y = actor.y
    if direction == 'up':
        x = actor.x
        y = actor.y + 16
    if direction == 'down':
        x = actor.x
        y = actor.y - 16
    


def move_npc(npc):
    if npc.distance_to(player) <= 100:
        if player.x < npc.x:
            npc.x -= 16
        elif player.x > npc.x:
            npc.x += 16
        elif player.y > npc.y:
            npc.y += 16
        elif player.y < npc.y:
            npc.y -= 16


def pickup_item() -> None:
    for item in ingame_items:
        if player.pos == item.pos:
            player.inventory.append(item.item)
            ingame_items.remove(item)
            game_state.toggle_popup()
            game_state.popup_msg = ""


# load items
def load_items() -> None:
    with open("items.yaml", 'r') as stream:
        item_data = yaml.safe_load(stream)

    for item in item_data:
        game_items.append(Item(
            item_data[item]['image'],
            item_data[item]['name'],
            item_data[item]['type'],
            item_data[item]['stats']['attack'],
            item_data[item]['stats']['defence']
        ))


def draw_inventory_item(item, x, y):
    screen.blit(item.image, (x, y))
    screen.draw.text(item.name, (x + SPRITE_SIZE + OFFSET, y), color=(200, 200, 200))


def draw_popup_message() -> None:
    screen.draw.filled_rect(Rect(WIDTH//2-WIDTH//4+4, 40+4, WIDTH//2, 50), (0, 0, 0))
    screen.draw.filled_rect(Rect(WIDTH//2-WIDTH//4, 40, WIDTH//2, 50), (71, 45, 60))
    screen.draw.text(game_state.popup_msg, (WIDTH//2-WIDTH//4+10, 55,), color=(200, 200, 200))


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
    _ITEM_START_X = _START_X + 2 * SPRITE_SIZE
    _ITEM_START_Y = _START_Y + 2 * SPRITE_SIZE

    # Create a back ground for the inventory, Rect takes
    screen.draw.filled_rect(Rect(_START_X+4, _START_Y+4, _INV_WIDTH, _INV_HEIGHT), (0, 0, 0))
    screen.draw.filled_rect(Rect(_START_X, _START_Y, _INV_WIDTH, _INV_HEIGHT), (71, 45, 60))

    screen.blit('menu/corner_top_left', (_START_X, _START_Y))
    screen.blit('menu/corner_top_right', (_START_X+_INV_WIDTH-SPRITE_SIZE, _START_Y))
    screen.blit('menu/corner_bottom_left', (_START_X, _START_Y+_INV_HEIGHT-SPRITE_SIZE))
    screen.blit('menu/corner_bottom_right', (_START_X+_INV_WIDTH-SPRITE_SIZE, _START_Y+_INV_HEIGHT-SPRITE_SIZE))

    for i in range(len(player.inventory)):
        draw_inventory_item(player.inventory[i], _ITEM_START_X, _ITEM_START_Y+i*SPRITE_SIZE)

    # Horizontal lines
    for x in range(_INV_WIDTH//SPRITE_SIZE-2):
        screen.blit('menu/menu_straight_h', (_START_X+SPRITE_SIZE+x*SPRITE_SIZE, _START_Y))
        screen.blit('menu/menu_straight_h', (_START_X+SPRITE_SIZE+x*SPRITE_SIZE, _START_Y+_INV_HEIGHT-SPRITE_SIZE))

    # Vertical lines
    for y in range(_INV_HEIGHT//16-2):
        screen.blit('menu/menu_straight', (_START_X, _START_Y+y*SPRITE_SIZE+SPRITE_SIZE))
        screen.blit('menu/menu_straight', (_START_X+_INV_WIDTH-SPRITE_SIZE, _START_Y+y*SPRITE_SIZE+SPRITE_SIZE))


load_items()
ingame_items = [GameItem(game_items[0], (10*SPRITE_SIZE+OFFSET, 10*SPRITE_SIZE+OFFSET)),
                GameItem(game_items[1], (5*SPRITE_SIZE+OFFSET, 3*SPRITE_SIZE+OFFSET))]

pgzrun.go()
