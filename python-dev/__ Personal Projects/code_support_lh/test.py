# a121_catch_a_turtle.py

#-----import statements-----
import turtle
import random

#-----game configuration----
turt_color = "red"
turt_size = 5
turt_shape = "turtle"
score = 0

#-----initialize turtle-----
turt = turtle.Turtle()
turt.shape(turt_shape)
turt.fillcolor(turt_color)
turt.shapesize(turt_size)

'''score_writer = turtle.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(250, 210)
font_setup = ("Arial" , 40, "bold")

counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-250, 210)

timer = 5
counter_interval = 1000
timer_up = False'''

#-----game functions--------
'''
def turt_clicked(x, y):
    global timer
    if(timer_up == False):
        update_score()
        change_position()
    else:
        turt.hideturtle()
'''
def turt_clicked(x, y):
      change_position()

def change_position():
    new_xpos = random.randint(-200, 200)
    new_ypos = random.randint(-200, 200)
    turt.penup()
    turt.hideturtle()
    turt.goto(new_xpos, new_ypos)
    turt.showturtle()

def update_score():
    global score
    score += 1
    #score_writer.clear()
    #score_writer.write(score, font=font_setup)

'''def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) '''

#-----events----------------
turt.onclick(turt_clicked)
wn = turtle.Screen()
#wn.ontimer(countdown, counter_interval)
wn.mainloop()