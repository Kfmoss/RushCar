import pygame as pg
import settings as sts



class Enemy1(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.carEnemy = pg.image.load('img/randomcar.png').convert_alpha
        self.rect = self.image.get_rect()
        self.rect.center = (sts.WIDTH/2, sts.HEIGHT/3)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, screen):
        pass
