# a121_catch_a_turtle.py
# Screen Size: 400x300
#-----import statements-----
import turtle, random

#-----game configuration----
turt_color = 'darkgreen'
turt_size = 5
turt_shape = 'circle'

score = 0
#-----initialize turtle-----
turt = turtle.Turtle(shape = turt_shape)
turt.turtlesize(turt_size)
turt.color(turt_color)
turt.speed(0)
turt.penup()

score_writer = turtle.Turtle()
#-----game functions--------
def turt_clicked(x, y):
    change_position()
    update_score()

def change_position():
    newx = random.randint(-400, 400)
    newy = random.randint(-300, 300)
    turt.goto(newx, newy)

def update_score():
    global score
    score += 1
    print(score)

#-----events----------------
turt.onclick(turt_clicked)





wn = turtle.Screen()
wn.mainloop()