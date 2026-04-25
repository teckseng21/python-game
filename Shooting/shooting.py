import pgzrun
import random

WIDTH=1200
HEIGHT=600

ship=Actor('ship')
bug=Actor('bug')

def draw():
    screen.clear()
    screen.fill(color=(0,0,255))
    bug.draw()
    ship.draw()

def place_ship():
    ship.x=(600)
    ship.y=(300)

pgzrun.go()
place_ship()