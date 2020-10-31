import turtle as turtle

def make_cloud():
    cloud = turtle.Turtle()
    cloud.turtlesize(2)
    cloud.shape('circle')
    cloud.color('lightgrey')
    cloud.penup()
    cloud.stamp()
    cloud.setheading(0)
    cloud.forward(30)
    cloud.stamp()
    cloud.setheading(135)
    cloud.forward(30)


make_cloud()

wn = turtle.Screen()

wn.mainloop()