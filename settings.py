from vector import Vector
import pygame as pg
import sys

class Settings:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (30, 30, 30)



        self.ship_speed_factor = 1
        self.ship_limit = 3

        self.alien_speed_factor = 1

        self.fleet_drop_speed = 5

        self.fleet_direction = Vector(1, 0)

        self.laser_speed_factor = 1

        self.laser_height = 15

        self.laser_width = 10

        self.laser_color = 0, 0, 255

