import pgzrun
from random import randint
bee= Actor('bee')
flower= Actor('flower')
score=0

WIDTH=450
HEIGHT=450

def draw():
    screen.clear()
    screen.blit("grass",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score: "+str(score),color="black", topleft=(10,10))
def place_bee():
    bee.x=randint(50,WIDTH-50)
    bee.y=randint(50,WIDTH-50)

def place_flower():
    flower.x=randint(50,WIDTH-50)
    flower.y=randint(50,WIDTH-50)

def update():
    if keyboard.a:
        bee.x=bee.x-2
    if keyboard.d:
        bee.x=bee.x+2
    if keyboard.w:
        bee.y=bee.y-2
    if keyboard.s:
        bee.y=bee.y+2
    flower_collected=bee.colliderect(flower)
    if flower_collected:
        global score
        score+=9999999
        place_flower()



place_bee()
pgzrun.go()