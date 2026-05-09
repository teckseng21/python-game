import pgzrun
import random

WIDTH=1200
HEIGHT=600

ship=Actor('ship')
bug=Actor('bug')

ship.pos=(WIDTH//2,HEIGHT-60)
speed=5
enemies=[]
score=0
direction=1
bullets=[]

def display_score():
    screen.draw.text(str(score),(50,30))


for i in range(8):
    enemies.append(Actor('bug'))
    enemies[-1].x=100+90*i
    enemies[-1].y=80

def draw():
    screen.clear()
    screen.fill(color=(0,0,255))
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    display_score()
    ship.draw()

def update():
    move_down=False
    global score,direction
    
    if keyboard.a:
        ship.x=ship.x-speed
        if ship.x<0:
            ship.x=0
        
    if keyboard.d:
        ship.x=ship.x+speed
        if ship.x>1200:
            ship.x=1200

    if keyboard.s:
        ship.y=ship.y+speed
        if ship.y>600:
            ship.y=600
    
    if keyboard.w:
        ship.y=ship.y-speed
        if ship.y<0:
            ship.y=0
    
    if keyboard.space:
        print ("Pressing space")
        bullets.append(Actor('bullet'))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y

        
    if len(enemies)>0 and (enemies[-1].x>WIDTH-80 or enemies[0].x<80):
        move_down=True
        direction=direction*-1
    for enemy in enemies:
        enemy.x=enemy.x+5*direction
        if move_down==True:
            enemy.y=enemy.y+50
   



def place_ship():
    ship.x=(600)
    ship.y=(300)

place_ship()
pgzrun.go()