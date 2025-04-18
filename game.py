import pygame as pg
import settings as sts
import barra as br
import sprites.road as rd
import dashboard.score as sc
import sprites.fuel as sf
import random as rnd 
import sys

pg.init()

screen = pg.display.set_mode((sts.WIDTH*1.25,sts.HEIGHT*1.25))
pg.display.set_caption("My game send info to my database")

clock = pg.time.Clock()
# pg.mixer.music.load('MyBackgroundGameSong.mp3')
# pg.mixer.music.set_volume(0.3)
# pg.mixer.music.play(-1)


## car
car = br.Barra(sts.rect_speed_x, sts.rect_speed_y)
## road
road = rd.Road()
roadLines1= rd.RoadLines(sts.WIDTH/1.575, 0)
roadLines2 = rd.RoadLines(sts.WIDTH/1.575, 150)
roadLines3 = rd.RoadLines(sts.WIDTH/1.575, 300)
roadLines4 = rd.RoadLines(sts.WIDTH/1.575, 450)
roadLines5 = rd.RoadLines(sts.WIDTH/1.575, 600)
roadLines6 = rd.RoadLines(sts.WIDTH/1.575, 750)

#dashboard
score = sc.Score()

# Fuel
fuel = sf.Energy(sts.WIDTH/1.25, 0)


#pg.sprite.Group.add(road)
#pg.sprite.Group.add(roadLines1)
#pg.sprite.Group.add(roadLines2)

all_Obj = pg.sprite.Group(car)
all_Obj.add(fuel)




while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if fuel not in all_Obj:
            posx = rnd.randint(sts.ROADWIDTH-200,sts.ROADWIDTH + 200)

            fuel = sf.Energy(posx, 0)

            all_Obj.add(fuel)
        get_collide = pg.sprite.spritecollide(fuel, all_Obj,True)
        if get_collide:
            print("hohoho")

        
    screen.fill(sts.Green)
    score.update(screen)
    car.update(screen)
    road.update(screen)
    fuel.update(screen)
    roadLines1.update(screen)
    roadLines2.update(screen)
    roadLines3.update(screen)
    roadLines4.update(screen)
    roadLines5.update(screen)
    roadLines6.update(screen)
    
    all_Obj.draw(screen)
    all_Obj.update(screen)


    pg.display.flip()
    clock.tick(60)
