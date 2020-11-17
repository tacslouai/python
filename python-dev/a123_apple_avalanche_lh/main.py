#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()
apple.penup()
apple_ypos = 0
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def fruit_fall(active_apple):
  global apple_ypos
  apple_ypos = active_apple.ycor() - 0.25
  active_apple.goto(active_apple.xcor(), apple_ypos)
#-----function calls-----
draw_apple(apple)
while(True):
  fruit_fall(apple)
  if(apple_ypos < -200):
    apple.hideturtle()
    break
wn.mainloop()