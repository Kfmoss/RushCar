import pygame as pg
import settings as sts

class Coin(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.coin = pg.image.load('img/Coin.png').convert_alpha()
        self.image = pg.transform.scale(self.coin, (sts.COINWIDTH, sts.COINHEIGTH))
        self.rect = self.image.get_rect()
        self.vel = 4


    def draw(self, screen):
        self.rect.y += self.vel
        screen.blit(self.image, self.rect)


    def update(self, screen):
        

        self.draw(screen)