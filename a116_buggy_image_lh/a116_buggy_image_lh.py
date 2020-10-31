#   a116_buggy_image.py
import turtle as trtl

painter = trtl.Turtle()
painter.pensize(40)

# Spider Body/Head
painter.circle(20)
painter.speed(0)
numLegs = 8
legLength = 70
rotation = 360 / numLegs 
painter.pensize(5)

# Spider Legs
i = 0
while (i < numLegs/2):
  painter.goto(0,20)
  painter.setheading(rotation*i/1.5 + 135)
  painter.forward(legLength)
  i = i + 1

i = 0
while (i < numLegs/2):
  painter.goto(0,20)
  painter.setheading(rotation*i/1.5 - 45)
  painter.forward(legLength)
  i = i + 1

# Spider Eyes
eye_spacing = 8
painter.penup()
painter.goto(-eye_spacing, 0)
painter.pendown()
painter.pencolor('yellow')
painter.circle(2)
painter.penup()
painter.goto(eye_spacing, 0)
painter.pendown()
painter.circle(2)

painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()