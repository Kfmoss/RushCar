import pygame as pg
import settings as sts
import random as rd

class Energy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        posx = rd.randint(sts.ROADWIDTH, sts.ROADHEIGTH) 
        self.rect = pg.Rect(posx, 0, 40,90)
        self.fuel = pg.image.load('fuel.png').convert_alpha()
        self.image = pg.transform.scale(self.fuel, (30, 90) )
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, screen):
        self.draw(screen)
