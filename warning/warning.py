import pygame as pg
import settings as sts


class warning:
    def __init__(self):
        self.text = "GAME OVER"
        self.text_font = pg.font.SysFont("Serif", 85)
        self.t1 = self.text_font.render(self.text, True,"white",32)

    def update(self, screen):

        screen.blit(self.t1, (sts.WIDTH/2, sts.HEIGHT/2))

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
        # if secs > secs+10:
        #     self.lowEnergy=False







