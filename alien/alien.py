import pgzrun
from random import randint

WIDTH=450
HEIGHT=450

TITLE="Good Shot"
message=""
alien=Actor('alien')

def draw():
    screen.clear()
    screen.fill(color=(0,0,255))
    alien.draw()
    screen.draw.text(message,center=(225,20),fontsize=30)
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        place_alien()
        message="good shot!"
    else:
        message="you missed!"

def place_alien():
    alien.x=randint(50,WIDTH-50)
    alien.y=randint(50,WIDTH-50)

place_alien()

pgzrun.go()