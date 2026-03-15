import pgzrun
import random

WIDTH=800
HEIGHT=600
centrex=WIDTH/2
centrey=HEIGHT/2
centre=(centrex,centrey)

final_level=6
start_speed=10
ITEMS=["bottle","battery","chips","plasticbag"]
game_over=False
game_complete=False
current_level=1

items=[]
animations=[]

def draw():
    global items,current_level,game_over,game_complete
    screen.clear()
    screen.blit("background",(0,0))
    if game_over:
        display_message("GAME OVER","TRY AGAIN")
    elif game_complete:
        display_message("YOU WON","WELL DONE")
    else:
        for item in items:
            item.draw()
def update():
    global items
    if len(items)==0:
        items=make_items(current_level)

def display_message(heading_text,sub_heading_text):
    screen.draw.text(heading_text,fontsize=60,centre=CENTRE,color="white")
    screen.draw.text(sub_heading_text,fontsize=30,centre=(centrex,centrey+30),color="white")


def create_items(items_to_create):
    new_items=[]
    for options in items_to_create:
        item=Actor(options) 
        new_items.append(item)
    return new_items

def make_items(number_of_extra_items):
    items_to_create=get_option_to_create(number_of_extra_items)
    new_items=create_items(items_to_create)
    return new_items
def get_option_to_create(number_of_extra_items):
    items_to_create=["paperbag"]
    for i in range(0,number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create
pgzrun.go()