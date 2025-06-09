import pygame as pg
import settings as sts
import barra as br
import sprites.road as rd
import dashboard.score as sc
import dashboard.energy as en
import dashboard.speedometer as sp
import sprites.fuel as sf
import sprites.coins as spc
import random as rnd 
import sprites.cars as enc
import warning.warning as wr
import random 
import sys

pg.init()


screen = pg.display.set_mode((sts.WIDTH*1.25,sts.HEIGHT*1.25))
bg_pic = pg.image.load('img/streets.png')
pg.display.set_caption("My game send info to my database")

clock = pg.time.Clock()
pg.mixer.init()
pg.mixer.music.load('sounds/dova_DETROIT_BEAT_1.mp3')
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play(-1)

car = br.Barra()
enemyCar = enc.Enemy1()
## road
road = rd.Road()

Rlines= []
distance = 0
for i in range(6):
    rline = rd.RoadLines(sts.WIDTH/1.575, distance)
    Rlines.append(rline)
    distance +=150

    

# roadLines1= rd.RoadLines(sts.WIDTH/1.575, 0)
# roadLines2 = rd.RoadLines(sts.WIDTH/1.575, 150)
# roadLines3 = rd.RoadLines(sts.WIDTH/1.575, 300)
# roadLines4 = rd.RoadLines(sts.WIDTH/1.575, 450)
# roadLines5 = rd.RoadLines(sts.WIDTH/1.575, 600)
# roadLines6 = rd.RoadLines(sts.WIDTH/1.575, 750)

#dashboard
full_energy = 100
score = sc.Score()
health =en.Fuel_Energy(full_energy)
speed = sp.Speedometer()

# coins

coin1 = spc.Coin(sts.WIDTH/2,0)

# Fuel
fuel = sf.Energy(sts.WIDTH/1.25, 0)





#########  Groups 



all_enemies = pg.sprite.Group(enemyCar)
all_coins = pg.sprite.Group(coin1)
all_Obj = pg.sprite.Group(car)

energy = pg.sprite.Group(fuel)

#print(hex(id(ener
# gy)))



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if fuel not in energy:
            posx = rnd.randint(sts.ROADWIDTH-200,sts.ROADWIDTH + 200)
            fuel = sf.Energy(posx, 0)
            energy.add(fuel)
        hit = pg.sprite.groupcollide(energy, all_Obj, True, False )
        if hit:
            health.full_energy = max(0, health.full_energy +0.7)
        keys = pg.key.get_pressed()
        press = False
        if keys[pg.K_SPACE]:
            press = True
            
            health.full_energy = max(0, health.full_energy -0.5)
            if speed.speed_now <speed.max_speed:
                extra_speed = pg.time.get_ticks()//1000
                speed.speed_now +=extra_speed
                if speed.speed_now >=speed.max_speed:
                    speed.speed_now+=0
        if not keys[pg.K_SPACE] and speed.speed_now>speed.min_speed:
            less_speed = pg.time.get_ticks()//1000
            speed.speed_now-=less_speed
            if speed.speed_now <= speed.min_speed:
                speed.speed_now =speed.min_speed    


        health.full_energy = max(0, health.full_energy -0.2)
        if health.full_energy ==0:
            speed.speed_now =0
            coin1.stopSignal = False
            for i in Rlines:
                i.stopSignal= False
            # roadLines1.stopSignal = False
            # roadLines2.stopSignal = False
            # roadLines3.stopSignal = False
            # roadLines4.stopSignal = False
            # roadLines5.stopSignal = False
            # roadLines6.stopSignal = False
            


    


        #Collide_coins
        get_collide = pg.sprite.groupcollide(all_coins,all_Obj, True, False)
        if get_collide:
            score.score+=1
           
            posx = rnd.randint(sts.ROADWIDTH-200,sts.ROADWIDTH + 200)
            coin1 = spc.Coin(posx, 0)
            all_coins.add(coin1)
        
        if coin1 not in all_coins:
            pass
        #Collide_fuel
        hit = pg.sprite.groupcollide(energy, all_Obj, True, False )
        if hit:
            if health.full_energy<100:
                health.full_energy = max(0, health.full_energy +3)
        
        ##Collide enemy car
        get_collide_enemy =pg.sprite.groupcollide(all_enemies, all_Obj, True, False)
        if get_collide_enemy:
            pass
    
   
    screen.blit(bg_pic, [0,0])
    score.update(screen)
    health.update(screen)
    speed.update(screen)
    road.update(screen)

    for i in Rlines:
        i.update(screen)
    # roadLines1.update(screen)
    # roadLines2.update(screen)
    # roadLines3.update(screen)
    # roadLines4.update(screen)
    # roadLines5.update(screen)
    # roadLines6.update(screen)
    
    all_enemies.update(screen)
    all_Obj.update(screen)  
    energy.update(screen)
    coin1.update(screen)



    pg.display.flip()
    clock.tick(60)
