import ctypes
import math
import sys

import pygame


def get_native_resolution():
    user32 = ctypes.windll.user32
    return (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))


# resolutions
native_res = get_native_resolution()
default_res = (800, 600)
res = [default_res[0], default_res[1]]  # current resolution

# screen
pygame.init()  # start pygame
screen = pygame.display.set_mode(res, pygame.RESIZABLE)
screen_clip = screen.get_clip()

# game timing
clock = pygame.time.Clock()
fps = 144

# viewing position
start_pos = [0, 0]
current_pos = [0, 0]
offset = [0, 0]

# default block size
size = 10

# booleans
mouse_button1_down = False
mouse_button3_down = False
clear_screen = True
fullscreen = False
show_grid = True

# colors
white = (255, 255, 255)
grey = (150, 150, 150)
black = (0, 0, 0)
block_color = white
grid_color = grey
background_color = black

# grid to store blocks
grid = None
