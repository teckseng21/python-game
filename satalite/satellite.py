import pgzrun
from random import randint



WIDTH=700
HEIGHT=400

satellites=[]
lines=[]
next_satellite=0
number_of_satellite=8
def draw():
    screen.clear()
    screen.blit("space",(0,0))
    for satellite in satellites: 
        satellite.draw()
def place_satellite():
    for i in range(0,number_of_satellite):
        satellite= Actor('satellite')
        satellite.x=randint(50,WIDTH-50)
        satellite.y=randint(50,HEIGHT-50)
        satellites.append(satellite)
place_satellite()
pgzrun.go()