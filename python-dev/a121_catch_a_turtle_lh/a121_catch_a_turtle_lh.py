# a121_catch_a_turtle.py
# Screen Size: 400x300
#-----import statements-----
import turtle
import random
import leaderboard as lb

#-----game configuration----
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("What is your name?")

turt_color = 'darkgreen'
turt_size = 5
turt_shape = 'circle'

score = 0
#-----initialize turtle-----
turt = turtle.Turtle(shape=turt_shape)
turt.turtlesize(turt_size)
turt.color(turt_color)
turt.speed(0)
turt.penup()

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(250, 220)
font_setup = ("Arial", 20, 'normal')
score_writer.write(score, font=font_setup)

counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-250, 220)

timer = 5
counter_interval = 1000
timer_up = False

#------game functions------


def turt_clicked(x, y):
    global timer, score

    if (timer+1 >= 0):
        update_score()
        change_position()

    else:
        turt.hideturtle()


def change_position():
    newx = random.randint(-400, 400)
    newy = random.randint(-300, 300)
    turt.goto(newx, newy)


def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    # print(score)


def countdown():
    global timer, timer_up
    counter.clear()
    if (timer < 0):
        counter.write("Time's up!", font=font_setup)
        timer -= 1
        timer_up = True
        manage_leaderboard()
        counter.getscreen().ontimer(countdown, counter_interval)

    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        timer_up = False
        counter.getscreen().ontimer(countdown, counter_interval)

# manages the leaderboard for top 5 scorers

def manage_leaderboard():

    global leader_scores_list
    global leader_names_list
    global score
    global turt

    # load all the leaderboard records into the lists
    lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

    # TODO
    if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(leader_names_list, leader_scores_list, True, turt, score)

    else:
        lb.draw_leaderboard(leader_names_list, leader_scores_list, False, turt, score)


#-------events-------

turt.onclick(turt_clicked)
wn = turtle.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()
