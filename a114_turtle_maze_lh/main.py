#   a114_robot_maze.py
import turtle as trtl

#------ robot algorithms
def move():
  robot.dot(10)
  robot.forward(50)

def turn_left():
  robot.speed(0)
  robot.left(90)
  robot.speed(2)

def turn_right():
  robot.speed(0)
  robot.right(90)
  robot.speed(2)
  
#----- roboto starting location
startx = -100
starty = -100

#----- init screen
wn = trtl.Screen()
wn.setup(width=400, height=420)

#----- init robot
robot_image = "robot.gif"
wn.addshape(robot_image)
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.penup()
robot.pencolor("darkorchid") # used for dot color
robot.setheading(90)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO 1: change maze here
wn.bgpic("maze3.png") # other file names should be maze2.png, maze3.png

#---- TODO 2: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:

# Original code
'''
i = 0
while (i < 3):
  i += 1
  move()
'''

'''
# Maze 1
i = 0
while (i < 4): # forward 4
  i += 1
  move()

turn_right()

i = 0
while (i < 4): # forward 4
  i += 1
  move()
'''
'''
# Maze 2
i = 0
while (i < 3): # forward 3
  i += 1
  move()

turn_right()

i = 0
while (i < 2): # forward 2
  i += 1
  move()
'''


# Maze 3

i = 0
while (i < 4):
  i += 1
  move()
  turn_right()
  move()
  turn_left()




#---- end robot movement 

wn.mainloop()
