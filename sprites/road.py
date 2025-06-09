import pygame as pg
import settings as sts


class Road:
    def __init__(self):
        self.roadWidth = sts.ROADWIDTH
        self.roadHeigth = sts.ROADHEIGTH
        self.color = sts.slate_gray
        #self.rect = pg.Rect(sts.WIDTH/3,0 ,490, 800)
        self.rect = pg.Rect(sts.WIDTH/3,0 ,self.roadWidth,self.roadHeigth)
        self.speed = sts.roadLineinicialSpeed
        

    def draw(self, screen):

        pg.draw.rect(screen, self.color, self.rect)
        
            
        # screen.blit(screen, self.rect)
    def update(self, screen):
        self.draw(screen)


class RoadLines:
    def __init__(self, pos_X, pos_y):
        self.color = sts.WHITE
        self.rect = pg.Rect(pos_X,pos_y ,sts.ROADLINEWIDTH,sts.ROADLINEHEIGTH)
        self.stopSignal = True
        #self.rect = pg.Rect(sts.WIDTH/1.15,0 ,sts.ROADLINEWIDTH,sts.ROADLINEHEIGTH)
        


    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)

    def move(self):
        keys=pg.key.get_pressed()
        self.rect.y +=sts.roadLineinicialSpeed
        if self.stopSignal == True:
            if self.rect.y > sts.HEIGHT:
                self.rect.y =0
            if keys[pg.K_SPACE] and pg.time.get_ticks() <5000:
                self.rect.y +=3
            elif keys[pg.K_SPACE] and pg.time.get_ticks() >=5000:
                self.rect.y +=10
        else: 
            sts.roadLineinicialSpeed =0
        

                
       

        
    def update(self, screen):
        self.draw(screen)
        self.move()

