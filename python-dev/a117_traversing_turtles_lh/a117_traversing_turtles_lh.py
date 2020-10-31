#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "classic", "classic"]
turtle_colors = ["steelblue4", "springgreen4", "steelblue3", "springgreen3", "steelblue2", "springgreen2", "steelblue1", "springgreen1"]


for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  new_color = turtle_colors.pop()
  t.fillcolor(new_color)
  t.pencolor(new_color)
  
  t.penup()

t.speed(0)



#   assign starting position to center of the screen
startx = 0
starty = 0

#   loop through each turtle and go forward at a 45 degree angle


direction = 90
for t in my_turtles:
  t.goto(startx, starty)
  t.setheading(direction)
  t.pendown()

  i = 0
  while(i < 45):
    t.pensize(i)
    t.right(1)
    t.forward(2)
    i += 1
  #t.right(45)
  #t.forward(75)
  direction = t.heading()
  startx = t.xcor()
  starty = t.ycor()



#   increment startx and starty by 50 to move up and to the right 50 pixels
  #startx = startx + 50
  #starty = starty + 50

wn = trtl.Screen()
wn.mainloop()