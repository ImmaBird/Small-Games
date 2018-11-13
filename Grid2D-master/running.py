import ctypes
import math
import sys

import pygame

import defaults as d
import events as e
import grid as g

# create the grid storage
d.grid = g.Grid()

while True:
    # handles event list
    for event in pygame.event.get():
        e.handle_event(event)

    # fills the background
    if d.clear_screen:
        d.screen.fill(d.background_color)

    # draws the grid
    if d.show_grid:
        d.grid.draw_grid()

    # draws the block in grid
    d.grid.draw_blocks()

    pygame.display.update()
    d.clock.tick(d.fps)
