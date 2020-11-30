#   a123_apple_1.py

# Import necessary modules
import turtle as trtl
import random


#-----setup-----
# Declare/initialize global variables

apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

letters = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
current_apples = []
current_letters = []
temp_apples = []
num_apples = 5


#-----functions-----
# Draw letter text on apple
def draw_apple(active_apple, apple_letter):
  active_apple.penup()
  active_apple.shape(apple_image)
  wn.tracer(False)
  draw_text(active_apple, apple_letter)
  wn.tracer(True)
  wn.update()

# Make apple "fall" and reset it to a new location on the tree
def fruit_fall(apple_letter):
  global wn
  index = current_letters.index(apple_letter)
  current_letters.pop(index)
  active_apple = current_apples.pop(index)
  #apple_ypos = active_apple.ycor() - 200
  wn.tracer(False)
  active_apple.goto(active_apple.xcor(), active_apple.xcor()-200)
  wn.tracer(True)
  active_apple.clear()
  active_apple.hideturtle()
  reset_apple(active_apple)
  active_apple.showturtle()
  current_apples.append(active_apple)

# Draws text on turtle
def draw_text(active_apple, apple_letter):
  global wn
  pos = [active_apple.xcor(), active_apple.ycor()]
  active_apple.goto(active_apple.xcor()-10, active_apple.ycor()-30)
  active_apple.write(apple_letter, font = ("Arial", 30, "bold"))
  active_apple.goto(pos)

# If the list of letters isn't empty, then set the apple's position to a random position on the tree and remove that letter from the list
def reset_apple(active_apple):
  if(len(letters) > 0):
    active_apple.goto(random.randint(-100,100), random.randint(0, 50))
    index = random.randint(0, len(letters)-1)
    current_letter = letters.pop(index)
    current_letters.append(current_letter)
    draw_apple(active_apple, current_letter)

# Makes all of the apple turtles
for i in range(0, num_apples):
  active_apple = trtl.Turtle()
  active_apple.shape(apple_image)
  active_apple.color('white')
  active_apple.penup()

  reset_apple(active_apple)
  current_apples.append(active_apple)
  temp_apples.append(active_apple)


# Checks if the pressed key is in the current_letters list
def check_letter_a():
  if('A' in current_letters):
    fruit_fall('A')

def check_letter_b():
  if('B' in current_letters):
    fruit_fall('B')

def check_letter_c():
  if('C' in current_letters):
    fruit_fall('C')

def check_letter_d():
  if('D' in current_letters):
    fruit_fall('D')

def check_letter_e():
  if('E' in current_letters):
    fruit_fall('E')

def check_letter_f():
  if('F' in current_letters):
    fruit_fall('F')

def check_letter_g():
  if('G' in current_letters):
    fruit_fall('G')

def check_letter_h():
  if('H' in current_letters):
    fruit_fall('H')

def check_letter_i():
  if('I' in current_letters):
    fruit_fall('I')

def check_letter_j():
  if('J' in current_letters):
    fruit_fall('J')

def check_letter_k():
  if('K' in current_letters):
    fruit_fall('K')

def check_letter_l():
  if('L' in current_letters):
    fruit_fall('L')

def check_letter_m():
  if('M' in current_letters):
    fruit_fall('M')

def check_letter_n():
  if('N' in current_letters):
    fruit_fall('N')

def check_letter_o():
  if('O' in current_letters):
    fruit_fall('O')

def check_letter_p():
  if('P' in current_letters):
    fruit_fall('P')

def check_letter_q():
  if('Q' in current_letters):
    fruit_fall('Q')

def check_letter_r():
  if('R' in current_letters):
    fruit_fall('R')

def check_letter_s():
  if('S' in current_letters):
    fruit_fall('S')

def check_letter_t():
  if('T' in current_letters):
    fruit_fall('T')

def check_letter_u():
  if('U' in current_letters):
    fruit_fall('U')

def check_letter_v():
  if('V' in current_letters):
    fruit_fall('V')

def check_letter_w():
  if('W' in current_letters):
    fruit_fall('W')

def check_letter_x():
  if('X' in current_letters):
    fruit_fall('X')

def check_letter_y():
  if('Y' in current_letters):
    fruit_fall('Y')

def check_letter_z():
  if('Z' in current_letters):
    fruit_fall('Z')
  
#-----function calls-----#
def check_keypress():
  wn.onkeypress(check_letter_a, 'a')
  wn.onkeypress(check_letter_b, 'b')
  wn.onkeypress(check_letter_c, 'c')
  wn.onkeypress(check_letter_d, 'd')
  wn.onkeypress(check_letter_e, 'e')
  wn.onkeypress(check_letter_f, 'f')
  wn.onkeypress(check_letter_g, 'g')
  wn.onkeypress(check_letter_h, 'h')
  wn.onkeypress(check_letter_i, 'i')
  wn.onkeypress(check_letter_j, 'j')
  wn.onkeypress(check_letter_k, 'k')
  wn.onkeypress(check_letter_l, 'l')
  wn.onkeypress(check_letter_m, 'm')
  wn.onkeypress(check_letter_n, 'n')
  wn.onkeypress(check_letter_o, 'o')
  wn.onkeypress(check_letter_p, 'p')
  wn.onkeypress(check_letter_q, 'q')
  wn.onkeypress(check_letter_r, 'r')
  wn.onkeypress(check_letter_s, 's')
  wn.onkeypress(check_letter_t, 't')
  wn.onkeypress(check_letter_u, 'u')
  wn.onkeypress(check_letter_v, 'v')
  wn.onkeypress(check_letter_w, 'w')
  wn.onkeypress(check_letter_x, 'x')
  wn.onkeypress(check_letter_y, 'y')
  wn.onkeypress(check_letter_z, 'z')

check_keypress()

# Detects keypresses when user is focused on the turtle graphics window
wn.listen()
wn.mainloop()