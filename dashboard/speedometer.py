import pygame as pg
import settings as sts

class Speedometer:
    def __init__(self):
        self.max_speed = 200
        self.min_speed = 20
        self.speed_now = self.min_speed
        self.rect = pg.Rect (20, 120, 120,50)
        self.color_text = sts.Green
        self.color_surface = sts.Black
        self.font = pg.font.Font(None, 40)

    def draw(self, screen):

        pg.draw.rect(screen, self.color_surface, self.rect)
        speed_text = self.font.render(f"{ str(self.speed_now) } KM", True, self.color_text)
        speed_rect = speed_text.get_rect(center=self.rect.center)
        screen.blit(speed_text, speed_rect)
    def update(self, screen):
        self.draw(screen)


        