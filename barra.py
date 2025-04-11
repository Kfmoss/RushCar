import pygame as pg
import settings as sts
class Barra(pg.sprite.Sprite):
    def __init__(self, rectspeedx, rectspeedy):
        pg.sprite.Sprite.__init__(self)
        self.rect = pg.Rect(120, 20, sts.WIDTH/3, sts.HEIGHT/3)
        self.rsx = rectspeedx
        self.rsy = rectspeedy
        self.car = pg.image.load('newCarPygame.jpg').convert_alpha()
        self.image = pg.transform.scale(self.car, (sts.CARWIDTH-30,sts.CARHEIGHT-30))
        self.rect = self.image.get_rect()

    def bounce_the_barra(self):
    
    
        pass
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
            if self.rect.x <0:
                self.rect.x =2

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
        self.bounce_the_barra()
        self.radar()
        self.create()
        self.carCrash()
        self.move(screen)
        
