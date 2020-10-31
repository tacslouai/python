import turtle as trtl
#import pygame

wn = trtl.Screen()
xpos = -600
message = "NeoNut was The Imposter"
wn.screensize(1200, 900)
trtl.bgpic("background.png")
wn.addshape("crewmate.gif")
crewmate = trtl.Turtle(shape = 'crewmate.gif')
text = trtl.Turtle(shape = 'classic')
text.hideturtle()

crewmate.speed(0)
crewmate.penup()
crewmate.hideturtle()
crewmate.goto(-600, 0)
crewmate.showturtle()


while(True):
    crewmate.goto(xpos, 0)
    xpos += 1

    if(crewmate.xcor() == -10):
        text.color('white')
        style = ('Arial', 25)
        text.write(message, font = style, align = 'center')
        text.hideturtle()

    if(crewmate.xcor() >= 540):
        crewmate.hideturtle()
        break


    



wn.mainloop()