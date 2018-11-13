import ctypes
import math
import sys

import pygame

import defaults as d
import grid as g


def handle_event(event):
    if event.type is pygame.QUIT:
        sys.exit()

    # resizing window
    elif event.type is pygame.VIDEORESIZE:
        if not d.fullscreen:
            d.res[0], d.res[1] = event.size
            d.screen = pygame.display.set_mode(d.res, pygame.RESIZABLE)
            d.screen_clip = d.screen.get_clip()

    elif event.type is pygame.KEYDOWN:
        chr(event.key)
        if event.key is pygame.K_c:
            d.clear_screen = not d.clear_screen
        elif event.key is pygame.K_g:
            d.show_grid = not d.show_grid

        # toggle fullscreen
        elif event.key is pygame.K_f:
            if d.fullscreen:
                d.res[0] = d.default_res[0]
                d.res[1] = d.default_res[1]
                flag = pygame.RESIZABLE
                d.screen = pygame.display.set_mode(d.default_res, flag)
                d.screen_clip = d.screen.get_clip()
            else:
                d.res[0] = d.native_res[0]
                d.res[1] = d.native_res[1]
                flag = pygame.HWSURFACE | pygame.DOUBLEBUF
                flag = flag | pygame.FULLSCREEN
                d.screen = pygame.display.set_mode(d.native_res, flag)
                d.screen_clip = d.screen.get_clip()
            d.fullscreen = not d.fullscreen

    elif event.type is pygame.MOUSEBUTTONDOWN:
        if event.button is 1:
            d.mouse_button1_down = True
            x = math.floor((event.pos[0] - d.offset[0]) / d.size)
            y = math.floor((event.pos[1] - d.offset[1]) / d.size)
            d.grid.add(x, y)
        elif event.button is 3:
            d.mouse_button3_down = True
            d.start_pos[0] = event.pos[0]
            d.start_pos[1] = event.pos[1]

        # zoom in
        elif event.button is 4:
            d.size += 1
            d.offset[0] += (d.offset[0] - d.res[0] / 2) / (d.size - 1)
            d.offset[1] += (d.offset[1] - d.res[1] / 2) / (d.size - 1)

        # zoom out
        elif event.button is 5:
            if d.size > 1:
                d.size -= 1
                d.offset[0] -= (d.offset[0] - d.res[0] / 2) / (d.size + 1)
                d.offset[1] -= (d.offset[1] - d.res[1] / 2) / (d.size + 1)

    elif event.type is pygame.MOUSEBUTTONUP:
        if event.button is 3:
            d.mouse_button3_down = False
        elif event.button is 1:
            d.mouse_button1_down = False

    elif event.type is pygame.MOUSEMOTION:
        # window movement
        if d.mouse_button3_down:
            d.current_pos[0] = event.pos[0]
            d.current_pos[1] = event.pos[1]
            d.offset[0] += d.current_pos[0] - d.start_pos[0]
            d.offset[1] += d.current_pos[1] - d.start_pos[1]
            d.start_pos[0] = d.current_pos[0]
            d.start_pos[1] = d.current_pos[1]

        if d.mouse_button1_down:
            x = math.floor((event.pos[0] - d.offset[0]) / d.size)
            y = math.floor((event.pos[1] - d.offset[1]) / d.size)
            d.grid.add(x, y)
