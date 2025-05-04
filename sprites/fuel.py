import pygame as pg
import settings as sts
import random as rd

class Energy(pg.sprite.Sprite):
    def __init__(self, posx, posy):
        pg.sprite.Sprite.__init__(self)
        self.fuel = pg.image.load('fuel.png').convert_alpha()
        self.image = pg.transform.scale(self.fuel, (38, 60) )
        self.rect = self.image.get_rect()
        self.rect.center= (posx, posy)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def move(self):
        self.rect.y +=sts.roadLineinicialSpeed
        keys=pg.key.get_pressed()
        if pg.time.get_ticks() <5000:
            self.rect.y +=1

    def update(self, screen):
        if self.rect.y > sts.WIDTH:
            self.kill()
    
        self.draw(screen)
        self.move()
