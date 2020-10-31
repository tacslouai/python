#   a116_ladybug.py
import turtle as trtl

ladybug = trtl.Turtle()

# Draw Legs
ladybug.pensize(3)
ladybug.penup()
leg_length = 60
num_legs = 6
rotation = 360/num_legs
leg_x_pos = 0
leg_y_pos = -45
i = 0
while (i < num_legs/2):
    ladybug.goto(-leg_x_pos, leg_y_pos)
    ladybug.pendown()
    ladybug.setheading(rotation*i/2 + 150)
    ladybug.forward(leg_length)
    i += 1

ladybug.penup()

i = 0
while (i < num_legs/2):
    ladybug.goto(leg_x_pos, leg_y_pos)
    ladybug.pendown()
    ladybug.setheading(rotation*i/2 - 25)
    ladybug.forward(leg_length)
    i += 1

ladybug.penup()
ladybug.setheading(0)


# create ladybug head
ladybug.goto(0,0)
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(5)
ladybug.speed(0)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1




ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()