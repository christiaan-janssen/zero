from pgzero.builtins import *

"""
This module contains all ui elements for the game
"""
def draw_ui():
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