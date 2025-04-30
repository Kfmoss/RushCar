import pygame as pg
import settings as sts

class Fuel_Energy:
    def __init__(self):
        self.full_energy = 100
        self.energy_left = 100
        self.energy_increse = 10
        self.energy_decrease = 10
        self.color_bg = sts.Red
        self.color_surface = sts.Yellow
        self.rect1  = pg.Rect(10, 70, 100, 30)
        self.rect2 = pg.Rect(10, 70, self.full_energy, 30)

        self.font = pg.font.Font(None, 36)
        self.color_text = sts.White


    def increase(self):
        if self.energy_left <100:
            self.energy_left += self.energy_increse
        
    def decrease(self):
        if self.energy_left>0:
            self.energy_left-= self.energy_decrease

    def draw(self, screen):
        self.full_energy = int((self.full_energy / self.energy_left) *100)
        pg.draw.rect(screen, self.color_bg, self.rect1)
        pg.draw.rect(screen,self.color_surface, self.rect2)

    def update(self, screen):
        
        self.full_energy -= self.energy_left
        

        self.draw(screen)


        
