import turtle

trtl = turtle.Turtle()
trtl.speed(1)

#Function contains the procedure that draws clouds.
def make_cloud(xPos, yPos):
    trtl.goto(xPos, yPos)
    trtl.turtlesize(4)
    trtl.shape('circle')
    trtl.color('lightgrey')
    trtl.penup()
    # Stamp attaches a copy of the large turtle on canvas as it follows the trtl trianlge route
    trtl.stamp()
    trtl.setheading(0)
    trtl.forward(54)
    trtl.stamp()
    trtl.setheading(126)
    trtl.forward(50)


make_cloud(0, 0)


wn = turtle.Screen()
wn.mainloop()