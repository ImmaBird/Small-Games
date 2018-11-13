import ctypes
import math
import sys

import pygame

import defaults as d


class Grid:
    def __init__(self):
        self.blocks = {}

    def add(self, x, y):
        if x not in self.blocks:
            self.blocks[x] = {y}
        else:
            self.blocks[x].add(y)

    def remove(self, x, y):
        if x in self.blocks:
            if y in self.blocks[x]:
                self.blocks[x].remove(y)
                if len(self.blocks[x]) is 0:
                    del self.blocks[x]

    def draw_blocks(self):
        for x in self.blocks:
            for y in self.blocks[x]:
                self.draw_block(x, y)

    def draw_block(self, x, y):
        x += d.offset[0] / d.size
        y += d.offset[1] / d.size
        block = pygame.Rect(x * d.size, y * d.size, d.size, d.size)
        block = block.clip(d.screen_clip)
        d.screen.fill(d.block_color, block)

    def draw_grid(self):
        # horizantal grid
        a = math.floor((d.offset[1] % d.size) - d.size)
        b = math.floor((d.res[1] / d.size) + d.size)
        for i in range(a, b):
            x = 0
            y = i * d.size + d.offset[1] % d.size
            w = d.res[0]
            h = 1
            line = pygame.Rect(x, y, w, h)
            line = line.clip(d.screen_clip)
            d.screen.fill(d.grid_color, line)

        # vertical grid
        a = math.floor((d.offset[0] % d.size) - d.size)
        b = math.floor((d.res[0] / d.size) + d.size)
        for i in range(a, b):
            x = i * d.size + d.offset[0] % d.size
            y = 0
            w = 1
            h = d.res[1]
            line = pygame.Rect(x, y, w, h)
            line = line.clip(d.screen_clip)
            d.screen.fill(d.grid_color, line)
