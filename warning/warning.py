import pygame as pg
import settings as sts


class warning:
    def __init__(self):
        self.text = "GAME OVER"
        self.text_font = pg.font.SysFont("Serif", 85)
        self.t1 =self.text_font.render(self.text, True,"white",32)

    def update(self, screen):

        screen.blit(self.t1, (sts.WIDTH/2, sts.HEIGHT/2))


