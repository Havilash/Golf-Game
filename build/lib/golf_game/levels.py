import pygame

from constants import *
import game_objects


class Level(game_objects.GameObject):
    size = WIN_SIZE
    startpos = None
    endpos = None

    def __init__(self):
        self.draw_start()
        self.draw_end()
        super().__init__((0, 0))

    def draw_start(self):
        pass

    def draw_end(self):
        pass


class Level1(Level):

    def __init__(self):
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
        test_obstacles = [
            game_objects.Obstacle((10, 550), (780, 30)),
            game_objects.Obstacle((100, 100), (30, 400))
        ]

        for test_obstacle in test_obstacles:
            test_obstacle.draw(self.surface)

        super().__init__()


class Level2(Level):
    def __init__(self):
        self.surface = pygame.Surface(WIN_SIZE, pygame.SRCALPHA)
        super().__init__()


class Level3(Level):
    def __init__(self):
        self.surface = pygame.Surface(WIN_SIZE, pygame.SRCALPHA)
        super().__init__()