import pygame as pg
import settings as sts
import sprites.road as sroad


class warning:
    def __init__(self):
        self.text = "GAME OVER"
        self.text_font = pg.font.SysFont("Serif", 85)
        self.t1 = self.text_font.render(self.text, True,"white",32)

    def update(self, screen):

        go_rect = self.t1.get_rect(center =(sts.ROADWIDTH+20, sts.ROADHEIGTH/2))
        screen.blit(self.t1, go_rect)

class LowEnergy:
    def __init__(self):
        self.text = "Warning: Low Energy"
        self.text_font = pg.font.SysFont("Serif", 25)
        self.t1 = self.text_font.render(self.text, True,"white",32)
        self.lowEnergy = False
    def update(self,screen):
        secs = pg.time.get_ticks()//1000
        if secs and self.lowEnergy:
            if secs%2==0:
                screen.blit(self.t1, (10,190))








