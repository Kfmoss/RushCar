import pygame as pg
import settings as sts
import random as rn 



class Enemy1(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.carEnemy = pg.image.load('img/randomcar2.png').convert_alpha()
        self.image = pg.transform.scale(self.carEnemy, (sts.CARWIDTH-30,sts.CARHEIGHT-30))
        self.rect = self.image.get_rect()
        self.rect.center = (sts.WIDTH/2, sts.HEIGHT)
        self.direction = 2
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def move(self, screen):
        self.rect.y += -1
        self.rect.x+= self.direction 
        if self.rect.x >= 695:
            self.direction=-2
        if self.rect.x <= 290:
            self.direction=2
        self.draw(screen)

    
    def update(self, screen):
        self.move(screen)

    
