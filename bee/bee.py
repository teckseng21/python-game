import pgzrun
from random import randint
bee= Actor('bee')
flower= Actor('flower')

WIDTH=450
HEIGHT=450

def draw():
    screen.clear()
    bee.draw()
    flower.draw()

def place_bee():
    bee.x=randint(50,WIDTH-50)
    bee.y=randint(50,WIDTH-50)

def place_flower():
    flower.x=randint(50,WIDTH-50)
    flower.y-randint(50,WIDTH-50)

place_bee()
pgzrun.go()