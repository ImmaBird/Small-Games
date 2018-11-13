import math

import pygame

pygame.init()
black = (0, 0, 0)


class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'

    def rotateX(self, angle, point):
        x, y, z = self.x, self.y, self.z
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y -= point.y
        z -= point.z
        y = y * cosa - z * sina
        z = y * sina + z * cosa
        y += point.y
        z += point.z
        return Point3D(x, y, z)

    def rotateY(self, angle, point):
        x, y, z = self.x, self.y, self.z
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z -= point.z
        x -= point.x
        z = z * cosa - x * sina
        x = z * sina + x * cosa
        z += point.z
        x += point.x
        return Point3D(x, y, z)

    def rotateZ(self, angle, point):
        x, y, z = self.x, self.y, self.z
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x -= point.x
        y -= point.y
        x = x * cosa - y * sina
        y = x * sina + y * cosa
        x += point.x
        y += point.y
        return Point3D(x, y, z)

    def distance(self, b):
        radicand = (self.x - b.x)**2 + (self.y - b.y)**2 + (self.z - b.z)**2
        return math.sqrt(radicand)

    def project(self, win_width, win_height, fov, camera):
        factor = fov / (self.distance(camera) + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return (x, y)


class Cube:
    def __init__(self, x, y, z):
        self.positon = (x, y, z)
        s = 40
        self.vertices = [
            Point3D(x - s, y - s, z - s),
            Point3D(x, y - s, z - s),
            Point3D(x - s, y, z - s),
            Point3D(x, y, z - s),
            Point3D(x - s, y - s, z),
            Point3D(x, y - s, z),
            Point3D(x - s, y, z),
            Point3D(x, y, z)
        ]

        self.faces = [
            (1, 0, 4, 5),
            (6, 7, 5, 4),
            (2, 0, 1, 3),
            (2, 3, 7, 6),
            (2, 6, 4, 0),
            (3, 7, 5, 1)
        ]

    def draw(self, screen, camera):
        camera_pos = camera.get_position()
        width = screen.get_width()
        height = screen.get_height()
        projections = []

        for vertex in self.vertices:
            vertex = vertex.rotateX(camera.verticle_angle, camera_pos)
            vertex = vertex.rotateY(camera.horizontal_angle, camera_pos)

            point2D = vertex.project(width, height, camera.fov, camera_pos)
            projections.append(point2D)

        for face in self.faces:
            edges = []
            for index in face:
                edges.append(projections[index])
            pygame.draw.aalines(screen, black, True, edges)
