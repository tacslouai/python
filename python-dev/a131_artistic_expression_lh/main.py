import turtle

line = turtle.Turtle()
wn = turtle.Screen()
wn.setup(700, 700)
circles = []
slots = []
temp_scores = []
pressed = False
num_circles = 5

def press_button():
    global pressed
    pressed = True

def calculate_score(circles, slots):
    for i in range(0, num_circles):
        temp_score = 100 - abs(circles[i].ycor()-slots[i].ycor())
        temp_scores.append(temp_score)
        i += 1

    total_score =  int(sum(temp_scores))
    print("Your score is: ", total_score)

    if(total_score == 500):
        print("Are you sure you aren't cheating?")

    elif(total_score <= 500 and total_score > 300):
        print("You achieved Gold rank! \nGood job!")

    elif(total_score <= 300):
        print("Due to budget cuts, the only medal available is gold and you didn't make the cut \nsorry :(")

line.pensize(5)
line.goto(-wn.window_width()/2, 0)
line.goto(wn.window_width()/2, 0)

for i in range(0, num_circles):
    temp_turt = turtle.Turtle()
    temp_turt.penup()
    temp_turt.turtlesize(5)
    temp_turt.shape("circle")
    temp_turt.fillcolor("red")
    temp_turt.setheading(270)
    temp_turt.goto(-250+(i*125), 200)
    circles.append(temp_turt)

    temp_slot = turtle.Turtle()
    temp_slot.penup()
    temp_slot.turtlesize(6)
    temp_slot.shape(temp_turt.shape())
    temp_slot.color("grey")
    temp_slot.goto(-250+(i*125), 0)
    slots.append(temp_slot)

i = 0
wn.listen()

for circle in circles:
    while(True):
        wn.onkey(press_button, ' ')
        if(pressed):
            pressed = False
            i += 1
            break

        else:
            if(circle.ycor() > -350):
                circle.forward(1+i*2)

            else:
                circle.goto((-250+i*125), 200)

calculate_score(circles, slots)






wn.mainloop()
