import pygame as pg
from sys import exit
import game_functions as gf
from time import sleep
from scoreboard import ScoreBoard

class GameStats:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.reset_stats()
        self.last_ships_left = self.ships_left
        self.score = 0
        self.highscore = 0
        self.level = 0
        self.highscore = self.load_highscore()

    def reset_stats(self): self.ships_left = self.settings.ship_limit
    def ship_hit(self):
        self.ships_left -= 1
        n = self.ships_left
        print(f'SHIP HIT!', end=' ')
        if self.last_ships_left != self.ships_left:
            print(f'{self.ships_left} ship{"s" if n != 1 else ""} left')
            self.last_ships_left = self.ships_left

    def __del__(self): self.save_highscore()

    def load_highscore(self):
        with open("highscore.txt", "r") as f:
            s = f.read()
            return int(s)


    def save_highscore(self):
        print("in save_high_score()")
        try:
            with open("highscore.txt", "w") as f:
                f.write(str(round(self.highscore, -1)))
        except:
            return 0

    def get_score(self): return(self.score)
    def get_highscore(self): return(self.highscore)
    def get_level(self): return(self.level)
    def get_ships_left(self): return(self.ships_left)
    def reset_stats(self): self.ships_left = self.settings.ship_limit
    def level_up(self):
        self.level += 1
        print("Level is now = ", self.level)
    def alien_hit(self, alien):
        self.score += alien.points
        self.highscore = max(self.score.highscore)
    #def ship_hit(self):
        #self.ship_left -= 1
        #n = self.ships_left



