import pygame as pg
import settings as sts


class warning:
    def __init__(self):
        self.text = "warning, low energy"
        self.text_font = pg.font.Font(None, 30)
        self.t1 =self.text_font.render(self.text, True,pg.SRCALPHA,32 )

    

    def update(self, screen):

        screen.blit(self.t1, (sts.WIDTH/2, sts.HEIGHT/2))


