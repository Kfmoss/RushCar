import pygame as pg
import settings as sts
import barra as br
import sprites.road as rd
import dashboard.score as sc
import dashboard.energy as en
import sprites.fuel as sf
import sprites.coins as spc
import random as rnd 
import sys

pg.init()


screen = pg.display.set_mode((sts.WIDTH*1.25,sts.HEIGHT*1.25))
pg.display.set_caption("My game send info to my database")

clock = pg.time.Clock()
# pg.mixer.music.load('MyBackgroundGameSong.mp3')
# pg.mixer.music.set_volume(0.3)
# pg.mixer.music.play(-1)

car = br.Barra()
## road
road = rd.Road()
roadLines1= rd.RoadLines(sts.WIDTH/1.575, 0)
roadLines2 = rd.RoadLines(sts.WIDTH/1.575, 150)
roadLines3 = rd.RoadLines(sts.WIDTH/1.575, 300)
roadLines4 = rd.RoadLines(sts.WIDTH/1.575, 450)
roadLines5 = rd.RoadLines(sts.WIDTH/1.575, 600)
roadLines6 = rd.RoadLines(sts.WIDTH/1.575, 750)

#dashboard
full_energy = 100
score = sc.Score()
health =en.Fuel_Energy(full_energy)

# coins

coin1 = spc.Coin()

# Fuel
fuel = sf.Energy(sts.WIDTH/1.25, 0)

all_coins = pg.sprite.Group(coin1)
all_Obj = pg.sprite.Group(car)
energy = pg.sprite.Group(fuel)

# Energy




while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if fuel not in energy:
            posx = rnd.randint(sts.ROADWIDTH-200,sts.ROADWIDTH + 200)
            fuel = sf.Energy(posx, 0)
            energy.add(fuel)

        get_collide = pg.sprite.spritecollide(car,energy, True)
        if get_collide:
            fuel.kill()
            score.score+=1
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            health.full_energy = max(0, health.full_energy -1)

        health.full_energy = max(0, health.full_energy -0.2)

 
    screen.fill(sts.Green)
    score.update(screen)
    health.update(screen)
    road.update(screen)

    roadLines1.update(screen)
    roadLines2.update(screen)
    roadLines3.update(screen)
    roadLines4.update(screen)
    roadLines5.update(screen)
    roadLines6.update(screen)
    
    all_Obj.update(screen)
    all_Obj.draw(screen)
    energy.update(screen)
    energy.draw(screen)
    coin1.update(screen)



    pg.display.flip()
    clock.tick(60)
