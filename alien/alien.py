import pgzrun

WIDTH=450
HEIGHT=400

TITLE="Good Shot"

alien=Actor('alien')

def draw():
    screen.clear()
    screen.fill(color=(0,0,255))
    alien.draw()

pgzrun.go()