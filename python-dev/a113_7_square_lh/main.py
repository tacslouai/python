#   a113_square.py
#   Write code to draw a square.
import turtle as trtl

painter = trtl.Turtle()
painter.pensize(5)
# Your code here
i = 0
while (i < 4):
  painter.forward(50)
  painter.right(90)
  i += 1

wn = trtl.Screen()
wn.mainloop()
