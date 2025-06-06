import pygame as pg
import settings as sts



class Enemy1(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.carEnemy = pg.image.load('img/randomcar2.png').convert_alpha()
        self.image = pg.transform.scale(self.carEnemy, (sts.CARWIDTH-30,sts.CARHEIGHT-30))
        self.rect = self.image.get_rect()
        self.rect.center = (sts.WIDTH/2, sts.HEIGHT/3)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def detectPlayer(self, player):
        self.posx = self.rect.x
        self.posy = self.rect.y
        if player.rect.x < self.posx:
            print("I want you")
        

    def move(self, screen):
        self.rect.y -=5
        if self.rect.y <0:
            self.kill()
        #self.detectPlayer(player)
        self.draw(screen)
    def update(self, screen):
        self.move(screen)

    
