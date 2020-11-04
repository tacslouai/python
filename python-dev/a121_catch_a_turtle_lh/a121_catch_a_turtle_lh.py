# a121_catch_a_turtle.py
#-----import statements-----
import turtle

#-----game configuration----
turt_color = 'darkgreen'
turt_size = 5
turt_shape = 'classic'

#-----initialize turtle-----
turt = turtle.Turtle(shape = turt_shape)
turt.turtlesize(turt_size)
turt.color(turt_color)

#-----game functions--------
def on_click():
    print('nut')

#-----events----------------

wn = turtle.Screen()
wn.mainloop()