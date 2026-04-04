import pgzrun

TITLE="Quiz master"

WIDTH=870
HEIGHT=650

marquee_box=Rect(0,0,880,80)

question_box=Rect(0,0,650,150)
timer_box=Rect(0,0,150,150)
answer_box1=Rect(0,0,300,150)
answer_box2=Rect(0,0,300,150)
answer_box3=Rect(0,0,300,150)
answer_box4=Rect(0,0,300,150)
timer_box=Rect(0,0,150,150)
skip_box=Rect(0,0,150,330)

score=0
time_left=10

question_file_name="question.txt"

answer_boxes=[answer_box1,answer_box2,answer_box3,answer_box4]
questions=[]
question_count=0
question_index=0


marquee_message=""
marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
timer_box.move_ip(700,100)
skip_box.move_ip(700,270)


def draw():
    screen.clear()
    global marquee_message
    screen.fill(color="black")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"navyblue")
    screen.draw.filled_rect(skip_box,"darkgreen")
    screen.draw.filled_rect(timer_box,"navyblue")
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"darkorange")
    marquee_message="Welcome To Quiz Master!"
    screen.draw.textbox(marquee_message,marquee_box,color="white")



def update():
    move_marquee()

def read_question_file():
    global question_count,questions
    q_file=open(question_file_name,"r")
    for question in q_file:
        questions.append(question)
        question_count=question_count+1
    q_file.close()

def read_next_question():
    global question_index
    question_index=question_index+1
    return questions.pop(0).split(",")

def move_marquee():
    marquee_box.x=marquee_box.x-2
    if marquee_box.right<0:
        marquee_box.left=WIDTH    


read_question_file()
print (questions)
print (question_count)
move_marquee()
pgzrun.go()