import pygame as pg
import settings as sts
import random as rd

class Energy(pg.sprite.Sprite):
    def __init__(self, posx, posy):
        pg.sprite.Sprite.__init__(self)
        #posx = rd.randint(sts.ROADWIDTH, sts.ROADHEIGTH) 
        self.rect = pg.Rect(posx, posy, 35,60)
        self.fuel = pg.image.load('fuel.png').convert()
        self.image = pg.transform.scale(self.fuel, (38, 60) )
        self.rect = self.image.get_rect()
        self.rect.center= (posx, posy)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        #pg.draw.rect(screen, self.rect)
    
    def move(self):
        keys=pg.key.get_pressed()
        self.rect.y +=sts.roadLineinicialSpeed
        if self.rect.y > sts.HEIGHT:
            self.kill()
            #self.rect.y =0
        if keys[pg.K_SPACE] and pg.time.get_ticks() <5000:
            self.rect.y +=3
        elif keys[pg.K_SPACE] and pg.time.get_ticks() >=5000:
            self.rect.y +=5


    def update(self, screen):
    
        self.draw(screen)
        self.move()
