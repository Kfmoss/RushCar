import pygame as pg
import settings as sts
import random as rd

class Coin(pg.sprite.Sprite):
    def __init__(self, posx, posy):
        pg.sprite.Sprite.__init__(self)
        self.fuel = pg.image.load('fuel.png').convert()
        self.image = pg.transform.scale(self.fuel, (38, 60) )
        self.rect = self.image.get_rect()
        self.rect.center= (posx, posy)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    
    def move(self):
        self.rect.y +=sts.roadLineinicialSpeed
        keys=pg.key.get_pressed()
        if pg.time.get_ticks() <5000:
            self.rect.y +=5
        if self.rect.y > sts.WIDTH:
            self.kill()
            


    def update(self, screen):
    
        self.draw(screen)
        self.move()



# import pygame as pg
# import settings as sts
# import random as rn

# class Coin(pg.sprite.Sprite):
#     def __init__(self, posx, posy):
#         pg.sprite.Sprite.__init__(self)
#         self.coin = pg.image.load('img/Coin.png').convert_alpha()
#         self.image = pg.transform.scale(self.coin, (sts.COINWIDTH, sts.COINHEIGTH))
#         self.rect = self.image.get_rect()
#         self.rect.center=(posx,posy)
#         self.vel = 4

    
#     def move(self):
#         self.rect.y += self.vel
#         if self.rect.y >sts.HEIGHT:
#             self.kill()

#     def draw(self, screen):
#         self.move()
#         screen.blit(self.image, self.rect)


#     def update(self, screen):
#         self.draw(screen)