import pygame as pg
import settings as sts
class Barra(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.car = pg.image.load('img/playercar.png').convert_alpha()
        self.image = pg.transform.scale(self.car, (sts.CARWIDTH-20,sts.CARHEIGHT-20))
        self.rect = self.image.get_rect()
        self.rect.center=(sts.WIDTH/2, sts.HEIGHT/2)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
        
    def radar(self):
        pass
    def start_pos(self):
        pass
    def create(self):
        pass
    def carCrash(self):
        pass
    def move(self, screen):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.rect.x +=5
            if self.rect.x >sts.WIDTH:
                self.rect.x = sts.WIDTH

        if keys[pg.K_LEFT]:
            self.rect.x -=5
            # if self.rect.x <0:
            #     self.rect.x =2
            if self.rect.x <sts.WIDTH/3:
                self.rect.x = sts.WIDTH/3

        if keys[pg.K_UP]:
            self.rect.y -=5
     
            if self.rect.top <0:
                self.rect.y = 5
        if keys[pg.K_DOWN]:
            self.rect.y +=5

            if self.rect.y >sts.HEIGHT:
                self.rect.y=sts.HEIGHT-5
        self.draw(screen)
     
    def update(self,screen):
        #self.bounce_the_barra()
        self.radar()
        self.create()
        self.carCrash()
        self.move(screen)
        
