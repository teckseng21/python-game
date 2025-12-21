import turtle
import time

screen=turtle.Screen()
screen.setup(600,400)
screen.bgcolor("black")
screen.tracer(0)

score=0
score_display=turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0,170)
score_display.write("Score: {}".format(score),align="center",font=("Courier",16,"normal"))

paddle=turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.penup()
paddle.speed(0)
paddle.goto(0,-180)
paddle_width=120

ball=turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)
ball.goto(0,0)
ball.dx=2
ball.dy=-2

bricks=[]
colors=["red","orange","yellow","green","blue"]
for row in range(5):
  for col in range(-250,300,80):
    brick=turtle.Turtle()
    brick.shape("square")
    brick.color(colors[row])
    brick.penup()
    brick.speed(0)
    brick.goto(col,150-(row*30))
    bricks.append(brick)


  
def move_left():
  x=paddle.xcor()
  if x-paddle_width//2>-450:
    paddle.setx(x-20)
    
def move_right():
  x=paddle.xcor()
  if x+paddle_width//2<450:
    paddle.setx(x+20)
  
screen.listen()
screen.onkey(move_left,"Left")
screen.onkey(move_right,"Right")

game_started=False
def start_game(x,y):
  global game_started
  game_started=True
  
screen.onclick(start_game)

while True:
  screen.update()
  time.sleep(0.01)
  
  if not game_started:
    continue
  
  ball.setx(ball.xcor()+ball.dx)
  ball.sety(ball.ycor()+ball.dy)
  
  if ball.xcor()>290 or ball.xcor()<-290:
    ball.dx=ball.dx*(-1)
  if ball.ycor()>190:
    ball.dy=ball.dy*(-1)
  if ball.ycor()<-190:
    ball.goto(0,0)
    ball.dy*=-1
    game_started=False
    score=0
    score_display.clear()
    score_display.write("Score: {}".format(score),align="center",font=("Courier",16,"normal"))
  
  if (ball.ycor()>-180 and ball.ycor()<-170) and (paddle.xcor()-paddle_width//2<ball.xcor()<paddle.xcor()+paddle_width//2):
    ball.dy*=-1
    
  for brick in bricks:
    if abs(ball.xcor()-brick.xcor())<40 and abs(ball.ycor()-brick.ycor())<15:
      ball.dy*=-1
      brick.hideturtle()
      bricks.remove(brick)
      score=score+10
      score_display.clear
      score_display.write("Score: {}".format(score),align="center",font=("Courier",16,"normal"))
      
  if not bricks:
    print("You win!!!")
    break