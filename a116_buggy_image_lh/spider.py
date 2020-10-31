import turtle as trtl

painter = trtl.Turtle()

painter.pensize(5)
painter.turtlesize(5)
painter.speed(0)


# Thorax
painter.penup()
painter.goto(0, -30)
painter.begin_fill()
painter.circle(100, 360)
painter.end_fill()

# Head
painter.penup()
painter.goto(0,-100)
painter.pendown()
painter.fillcolor('black')
painter.begin_fill()
painter.circle(60, 360)
painter.end_fill()

painter.penup()

#eyes
painter.pencolor('yellow')
painter.goto(-20, -70)
painter.pendown()
painter.circle(5)
painter.penup()
painter.goto(20, -70)
painter.pendown()
painter.circle(5)


# Legs
painter.pencolor('black')
leg_space = 30

i = 0
while(i < 4):
    painter.penup()
    painter.setheading(135 + (10 * i))
    painter.goto(-80, 100 - i * leg_space)
    painter.pendown()
    painter.circle(60, 135)
    i += 1

i = 0
while(i < 4):
    painter.penup()
    painter.setheading(-135 - (10 * i))
    painter.goto(80, 100 - i * leg_space)
    painter.pendown()
    painter.circle(60, -135)
    i += 1

painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()