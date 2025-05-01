import pygame as pg
import settings as sts


class Fuel_Energy:
    def __init__(self, energy):
        self.full_energy = energy
        self.energy_increse = 10
        self.energy_decrease = 15
        self.color_bg = sts.Red
        self.color_surface = sts.Yellow
        #self.rect1  = pg.Rect(10, 70, 100, 30)
        self.rect2 = pg.Rect(10, 70, self.full_energy, 30)

        self.font = pg.font.Font(None, 36)
        self.color_text = sts.White

    def draw(self, screen):
        self.full_energy = max(0, min(100, self.full_energy))
        self.rect2 = pg.Rect(10, 70, self.full_energy, 30)
        pg.draw.rect(screen, self.color_surface, self.rect2)
        

    def update(self, screen):
        self.draw(screen)


        
