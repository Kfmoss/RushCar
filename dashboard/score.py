import pygame as pg
import settings as sts

class Score:
    def __init__(self):
        self.score = 0
        self.color = sts.Black
        self.rect = pg.Rect(10,10,150,50)
        self.font = pg.font.Font(None, 36)
        self.color_text = sts.White
    

        
    def draw(self, screen):
        time= pg.time.get_ticks()//1000
        keys = pg.key.get_pressed()
        #self.score += self.extra
        pg.draw.rect(screen, self.color, self.rect)
        score_txt = self.font.render(f"Score: {str(self.score)}", True, self.color_text)
        txt_rect = score_txt.get_rect(center=self.rect.center)
        screen.blit(score_txt, txt_rect)
       


        
    def update(self, screen):
        self.draw(screen)
    


