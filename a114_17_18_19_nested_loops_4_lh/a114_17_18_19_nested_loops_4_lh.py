#   a114_nested_loops_4.py 
import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()
painter.pensize(2)
painter.speed(0)
x = -200
y = 0
move_x = 1
move_y = 1
while (x < 100):

  while (y < 100):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = -1
  
  while (y > 0):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = 1

painter.penup()
painter.goto(-200, 0)
painter.pendown()
x = -200
y = 0
move_y = -1
move_x = 1
while (x < 100):

  while (y > -100):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = 1
 
  while (y < 0):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = -1


wn = trtl.Screen()
wn.mainloop()