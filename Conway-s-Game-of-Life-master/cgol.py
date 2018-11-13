import math
import sys

import pygame


class Board:
    def __init__(self):
        self.cells = {}

    def add(self, x, y):
        if x not in self.cells:
            self.cells[x] = {y}
        else:
            self.cells[x].add(y)

    def remove(self, x, y):
        if x in self.cells:
            if y in self.cells[x]:
                self.cells[x].remove(y)
                if len(self.cells[x]) is 0:
                    del self.cells[x]

    def cell_count(self, x, y, dead):
        live = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i in self.cells and j in self.cells[i]:
                    live += 1
                else:
                    if (i, j) in dead:
                        dead[(i, j)] += 1
                    else:
                        dead[(i, j)] = 1
        return live - 1

    def simulate(self):
        trash = []
        dead = {}
        for x in self.cells:
            for y in self.cells[x]:
                live = self.cell_count(x, y, dead)
                if live > 3 or live < 2:
                    trash.append((x, y))
        for x, y in trash:
            self.remove(x, y)
        for x, y in dead:
            if dead[(x, y)] is 3:
                self.add(x, y)

    def draw_board(self):
        for x in self.cells:
            for y in self.cells[x]:
                draw_cell(x, y)


pygame.init()
length = 600
width = 800
screen = pygame.display.set_mode((width, length))
screen_clip = screen.get_clip()
pause = False
mouse_button3_down = False
mouse_button1_down = False
start_pos = [0, 0]
current_pos = [0, 0]
offset = [0, 0]
speed = 250
b = Board()
size = 10
white = (255, 255, 255)
grey = (150, 150, 150)
black = (0, 0, 0)
font = pygame.font.SysFont('arial', 16)
hide_speed_time = -1
clear_screen = True
time_till_simulation = 0
grid = False
clock = pygame.time.Clock()

b.add(1, 0)
b.add(2, 1)
b.add(0, 2)
b.add(1, 2)
b.add(2, 2)


def draw_cell(x, y):
    x += offset[0] / size
    y += offset[1] / size
    cell = pygame.Rect(x * size, y * size, size, size).clip(screen_clip)
    screen.fill(white, cell)


while 1:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit()

        elif event.type is pygame.KEYDOWN:
            if event.key is pygame.K_SPACE:
                pause = not pause

            elif event.key is pygame.K_w:
                if speed > 50:
                    speed -= 50
                elif speed > 10:
                    speed -= 10
                hide_speed_time = pygame.time.get_ticks() + 3000
            elif event.key is pygame.K_s:
                if speed < 50:
                    speed += 10
                else:
                    speed += 50
                hide_speed_time = pygame.time.get_ticks() + 3000
            elif event.key is pygame.K_c:
                clear_screen = not clear_screen
            elif event.key is pygame.K_g:
                grid = not grid

        elif event.type is pygame.MOUSEBUTTONDOWN:
            if event.button is 1:
                mouse_button1_down = True
                b.add(
                    math.floor((event.pos[0] - offset[0]) / size),
                    math.floor((event.pos[1] - offset[1]) / size))
            elif event.button is 3:
                mouse_button3_down = True
                start_pos[0] = event.pos[0]
                start_pos[1] = event.pos[1]
            elif event.button is 4:
                size += 1
                offset[0] += (offset[0] - (width / 2)) / (size - 1)
                offset[1] += (offset[1] - (length / 2)) / (size - 1)
            elif event.button is 5:
                if size > 2:
                    size -= 1
                    offset[0] -= (offset[0] - (width / 2)) / (size + 1)
                    offset[1] -= (offset[1] - (length / 2)) / (size + 1)
        elif event.type is pygame.MOUSEBUTTONUP:
            if event.button is 3:
                mouse_button3_down = False
            elif event.button is 1:
                mouse_button1_down = False

        elif event.type is pygame.MOUSEMOTION:
            if mouse_button3_down:
                current_pos[0] = event.pos[0]
                current_pos[1] = event.pos[1]
                offset[0] += current_pos[0] - start_pos[0]
                offset[1] += current_pos[1] - start_pos[1]
                start_pos[0] = current_pos[0]
                start_pos[1] = current_pos[1]
            if mouse_button1_down:
                b.add(
                    math.floor((event.pos[0] - offset[0]) / size),
                    math.floor((event.pos[1] - offset[1]) / size))

    if clear_screen:
        screen.fill(black)

    if hide_speed_time > pygame.time.get_ticks():
        screen.blit(
            font.render('Speed: ' + str(speed), 1, white), ((width / 2) - 40,
                                                            10))

    if pygame.time.get_ticks() > time_till_simulation and not pause:
        b.simulate()
        time_till_simulation = pygame.time.get_ticks() + speed
    b.draw_board()

    if grid:
        for i in range(
                math.floor((offset[0] % size) - size),
                math.floor(width / size) + size):
            screen.fill(grey,
                        pygame.Rect(i * size + offset[0] % size, 0, 1, length))
        for i in range(
                math.floor((offset[1] % size) - size),
                math.floor(length / size) + size):
            screen.fill(grey,
                        pygame.Rect(0, i * size + offset[1] % size, width, 1))

    pygame.display.update()
    clock.tick(144)
