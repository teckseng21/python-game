import pgzrun
from random import randint
import time
from time import time


WIDTH=700
HEIGHT=400
start_time=0
total_time=0
end_time=0
satellites=[]
lines=[]
next_satellite=0
number_of_satellite=8
def draw():
    number=1
    screen.clear()
    screen.blit("space",(0,0))
    for satellite in satellites: 
        satellite.draw()
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20))
        number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    if next_satellite<number_of_satellite:
        total_time=time()-start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)


def place_satellite():
    global start_time
    for i in range(0,number_of_satellite):
        satellite= Actor('satellite')
        satellite.x=randint(50,WIDTH-50)
        satellite.y=randint(50,HEIGHT-50)
        satellites.append(satellite)
    start_time=time()

def update():
    pass

def on_mouse_down(pos):
    global next_satellite,lines
    if next_satellite<number_of_satellite:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                print("adding lines")
                lines.append((satellites[next_satellite-1].pos,satellites[next_satellite].pos))
                print(f"new data{lines}")
            next_satellite=next_satellite+1
        else:
            lines=[]
            next_satellite=0

place_satellite()
pgzrun.go()