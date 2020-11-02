import turtle
import random
trtl = turtle.Turtle()

trtl.speed(0)

wn = turtle.Screen()
wn.addshape("opbird4.gif")

# Grass
wn.bgcolor("green")


# Sky
trtl.penup()
trtl.goto(-400, -100)
trtl.pendown()
trtl.color("deepskyblue")
trtl.begin_fill()
for i in range(2):
    trtl.forward(800)
    trtl.left(90)
    trtl.forward(500)
    trtl.left(90)
trtl.end_fill()

# Sun
trtl.penup()
trtl.goto(-320, 125)
trtl.pendown()
trtl.color("yellow")
trtl.begin_fill()
trtl.circle(305)
trtl.end_fill()

# Cloud
trtl.penup()
trtl.goto(200, 200)
trtl.pendown()
trtl.color("white")
trtl.begin_fill()
trtl.circle(25)
trtl.end_fill()

trtl.penup()
trtl.goto(220, 240)
trtl.pendown()
trtl.begin_fill()
trtl.circle(25)
trtl.end_fill()

trtl.penup()
trtl.goto(230, 215)
trtl.pendown()
trtl.begin_fill()
trtl.circle(25)
trtl.end_fill()

trtl.penup()
trtl.goto(180, 225)
trtl.pendown()
trtl.begin_fill()
trtl.circle(25)
trtl.end_fill()

trtl.penup()
trtl.goto(2500, 235)
trtl.pendown()
trtl.begin_fill()
trtl.circle(30)
trtl.end_fill()

# House
trtl.penup()
trtl.goto(-100, -100)
trtl.pendown()
trtl.pensize(3)
trtl.color("chocolate", "orange") # (stroke, fill)
trtl.begin_fill()
for i in range(4):
    trtl.forward(170)
    trtl.left(90)
trtl.end_fill()


# Roof
trtl.penup()
trtl.goto(-127, 70)
trtl.pendown()
trtl.begin_fill()
for i in range(3):
    trtl.forward(225)
    trtl.left(120)
trtl.end_fill()

# Window 1
trtl.penup()
trtl.goto(0, 0)
trtl.pendown()
trtl.color("black", "white")
trtl.begin_fill()
for i in range(4):
    trtl.forward(50)
    trtl.left(90)
trtl.end_fill()

# Window 1 Cross - Horizontal Line 
trtl.penup()
trtl.goto(0, 25)
trtl.pendown()
trtl.color("black")
trtl.forward(50)

# Window 1 Cross - Vertical Line 
trtl.penup()
trtl.goto(25, 0)
trtl.pendown()
trtl.left(90)
trtl.forward(50)

# Window 2
trtl.penup()
trtl.goto(-80, 0)
trtl.pendown()
trtl.right(90)
trtl.color("black", "white")
trtl.begin_fill()
for i in range(4):
    trtl.forward(50)
    trtl.left(90)
trtl.end_fill()

# Window 2 Cross - Horizontal Line 
trtl.penup()
trtl.goto(-80, 25)
trtl.pendown()
trtl.color("black")
trtl.forward(50)

# Window 2 Cross - Vertical Line 
trtl.penup()
trtl.goto(-55, 0)
trtl.pendown()
trtl.left(90)
trtl.forward(50)

# Door
trtl.penup()
trtl.goto(-40, -97)
trtl.pendown()
trtl.right(90)
trtl.color("red")
trtl.begin_fill()
for i in range(2):
    trtl.forward(50)
    trtl.left(90)
    trtl.forward(80)
    trtl.left(90)
trtl.end_fill()

# Door Handle
trtl.penup()
trtl.goto(-30, -60)
trtl.pendown()
trtl.color("black")
trtl.begin_fill()
trtl.circle(5)
trtl.end_fill()
trtl.penup()
trtl.hideturtle()

# Bird
wn.addshape("opbird4.gif")
bird = turtle.Turtle(shape = "opbird4.gif")
bird_xpos = -400
bird_ypos = 100
bird.speed(0)
bird.setheading(0)
bird.hideturtle()
bird.penup()
bird.goto(bird_xpos, bird_ypos)
bird.showturtle()

# Bird Movement


while(True):

    bird_xpos = bird_xpos + random.randint(1, 5)
    bird_ypos = bird_ypos + random.randint(1, 5)
    bird_ypos = bird_ypos - random.randint(1, 5)
    bird.goto(bird_xpos, bird_ypos)

    
    if(bird_xpos >= 400 or bird_ypos >= 500):
        bird.goto(-400, 100)
        bird_xpos = bird.xcor()
        bird_ypos = bird.ycor()
        #break
    









trtl.hideturtle()
wn.mainloop()
