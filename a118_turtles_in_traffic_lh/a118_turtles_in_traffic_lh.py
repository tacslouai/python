#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across the screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
horiz_colors = ['red', 'blue', 'green', 'orange', 'purple', 'gold']
vert_colors = ['darkred', 'darkblue', 'lime', 'salmon', 'indigo', 'brown']

# turtle location
tloc = 30
# for every shape in the list, create two sets of turtles
for s in turtle_shapes:
  # horizontal turtles
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-200, tloc)
  ht.setheading(0)

  # vertical turtles
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 200)
  vt.setheading(270)
  
  # turtle spacing
  tloc += 30

# TODO: move turtles across and down screen, stopping for collisions

# variable initializations and assignments for contents of while loop
steps = 0
distance = 5
hitbox = 15

# generic loop
while (steps < 7):

  # loop increment
  steps = steps + 1

  # loops through each turtle
  for vt in vert_turtles:

    for ht in horiz_turtles:
      
      distance += 0.5

      if(distance > 10):
        distance = 5

      # move turtles
      ht.forward(distance)
      vt.forward(distance)

      # check for collision
      if ((abs(ht.xcor() - vt.xcor()) < hitbox) and (abs(ht.ycor() - vt.ycor()) < hitbox)):
        
        ht_color = ht.fillcolor()
        vt_color = vt.fillcolor()
        ht_shape = ht.shape()
        vt_shape = vt.shape()

        # change collided turtles to grey and collision shape
        ht.fillcolor('grey')
        vt.fillcolor('grey')
        ht.shape('classic')
        vt.shape('classic')

        # move collided turtles backward
        ht.forward(-10 * distance)
        vt.forward(-10 * distance)

        # restore original shape and color
        ht.fillcolor(ht_color)
        vt.fillcolor(vt_color)
        ht.shape(ht_shape)
        vt.shape(vt_shape)



for vt in vert_turtles:
  for ht in horiz_turtles:
    vt.color('grey')
    ht.color('grey')
        

# displays "That's all folks!" to indicate end of program
txt_trtl = trtl.Turtle(shape = 'classic')
txt_trtl.color('deep pink')
style = ('Courier', 35, 'bold italic')
txt_trtl.write("That's all folks!", font=style, align='center')
txt_trtl.hideturtle()

wn = trtl.Screen()
wn.mainloop()

