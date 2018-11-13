import math
import sys

import pygame

import shapes

pygame.init()
screen_length = 600
screen_width = 800
screen_dimensions = (screen_width, screen_length)
screen = pygame.display.set_mode(screen_dimensions)

pygame.mouse.set_visible(False)
mouse_x = screen_width / 2
mouse_y = screen_length / 2
pause = True

black = (0, 0, 0)
white = (255, 255, 255)


class camera:
    def __init__(self):
        self.horizontal_angle = 0
        self.verticle_angle = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.fov = 256
        self.move_speed = .1
        self.look_speed = 1

    def get_position(self):
        return shapes.Point3D(self.x, self.y, self.z)


camera = camera()
cube = shapes.Cube(0, 0, 4)

while True:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit()
        elif event.type is pygame.KEYDOWN:
            if event.key is pygame.K_ESCAPE:
                pause = not pause
                pygame.mouse.set_visible(pause)
                pygame.mouse.set_pos(mouse_x, mouse_y)
            elif event.key is pygame.K_p:
                print('h_angle: ' + str(camera.horizontal_angle))
                print('v_angle: ' + str(camera.verticle_angle))
                print('camera_pos: ' + str(camera.get_position()))
            elif event.key is pygame.K_k:
                camera.horizontal_angle += 1
                print(camera.horizontal_angle)
            elif event.key is pygame.K_h:
                camera.horizontal_angle -= 1
                print(camera.horizontal_angle)
            elif event.key is pygame.K_u:
                camera.verticle_angle += 1
                print(camera.verticle_angle)
            elif event.key is pygame.K_j:
                camera.verticle_angle -= 1
                print(camera.verticle_angle)
        elif event.type is pygame.MOUSEBUTTONDOWN:
            pass

    if pygame.key.get_pressed()[pygame.K_w]:
        camera.x += math.cos(camera.horizontal_angle *
                             (math.pi / 180)) * camera.move_speed
        camera.z += math.sin(camera.horizontal_angle *
                             (math.pi / 180)) * camera.move_speed
    if pygame.key.get_pressed()[pygame.K_s]:
        camera.x -= math.cos(camera.horizontal_angle *
                             (math.pi / 180)) * camera.move_speed
        camera.z -= math.sin(camera.horizontal_angle *
                             (math.pi / 180)) * camera.move_speed

    if not pause:
        camera.horizontal_angle += pygame.mouse.get_pos()[0] - mouse_x
        camera.verticle_angle -= pygame.mouse.get_pos()[1] - mouse_y
        pygame.mouse.set_pos(mouse_x, mouse_y)
        if camera.verticle_angle > 90:
            camera.verticle_angle = 90
        elif camera.verticle_angle < -90:
            camera.verticle_angle = -90
        camera.horizontal_angle %= 360

    screen.fill(white)
    cube.draw(screen, camera)
    pygame.display.update()
