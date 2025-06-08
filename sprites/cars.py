import pygame as pg
import settings as sts
import random as rn 



class Enemy1(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.carEnemy = pg.image.load('img/randomcar2.png').convert_alpha()
        self.image = pg.transform.scale(self.carEnemy, (sts.CARWIDTH-20,sts.CARHEIGHT-20))
        self.rect = self.image.get_rect()
        self.rect.center = (sts.WIDTH/2, sts.HEIGHT)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def move(self, screen):
        #self.vel = rn.randint(1,5)*-1
        self.rect.y += -1

        self.draw(screen)
    def update(self, screen):
        self.move(screen)

    
