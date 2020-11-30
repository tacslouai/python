#   a123_apple_1.py
import turtle as trtl
import random

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

'''
apple = trtl.Turtle()
apple.penup()
apple_ypos = 0
apple.color("white")

apple_letter = "A"
'''


letters = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
current_apples = []
current_letters = []
num_apples = 2
#check_funtions = [check_letter_a, check_letter_b, check_letter_c, check_letter_d, check_letter_e, check_letter_f, check_letter_g, check_letter_h, check_letter_i, check_letter_j, check_letter_k, check_letter_l, check_letter_m, check_letter_n, check_letter_o, check_letter_p, check_letter_q, check_letter_r, check_letter_s, check_letter_t, check_letter_u, check_letter_v, check_letter_w, check_letter_x, check_letter_y, check_letter_z]
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, apple_letter):
  active_apple.penup()
  active_apple.shape(apple_image)
  wn.tracer(False)
  draw_text(active_apple, apple_letter)
  wn.tracer(True)
  wn.update()


def fruit_fall(apple_letter):
  global wn
  index = current_letters.index(apple_letter)
  current_letters.pop(index)
  active_apple = current_apples.pop(index)
  apple_ypos = active_apple.ycor() - 200
  wn.tracer(False)
  active_apple.goto(active_apple.xcor(), apple_ypos)
  wn.tracer(True)
  active_apple.clear()
  active_apple.hideturtle()
  reset_apple(active_apple)
  

def draw_text(active_apple, apple_letter):
  global wn
  pos = [active_apple.xcor(), active_apple.ycor()]
  active_apple.goto(active_apple.xcor()-10, active_apple.ycor()-30)
  active_apple.write(apple_letter, font = ("Arial", 30, "bold"))
  active_apple.goto(pos)


def reset_apple(active_apple):
  if(len(letters) > 0):
    active_apple.goto(random.randint(-100,100), random.randint(0, 50))
    index = random.randint(0, len(letters)-1)
    current_letter = letters.pop(index)
    current_letters.append(current_letter)
    draw_apple(active_apple, current_letter)


for i in range(0, num_apples):
  active_apple = trtl.Turtle()
  active_apple.shape(apple_image)
  active_apple.color('white')
  active_apple.penup()
  reset_apple(active_apple)
  current_apples.append(active_apple)

#def check_functions_old():

  '''
  def check_letter_a():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'A' or apple_letter_lower == 'a'):
      fruit_fall('A')

  def check_letter_b():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'B' or apple_letter_lower == 'B'):
      fruit_fall()

  def check_letter_c():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'C' or apple_letter_lower == 'c'):
      fruit_fall()

  def check_letter_d():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'D' or apple_letter_lower == 'd'):
      fruit_fall()

  def check_letter_e():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'E' or apple_letter_lower == 'e'):
      fruit_fall()

  def check_letter_f():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'F' or apple_letter_lower == 'f'):
      fruit_fall()

  def check_letter_g():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'G' or apple_letter_lower == 'g'):
      fruit_fall()

  def check_letter_h():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'H' or apple_letter_lower == 'h'):
      fruit_fall()

  def check_letter_i():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'I' or apple_letter_lower == 'i'):
      fruit_fall()

  def check_letter_j():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'J' or apple_letter_lower == 'j'):
      fruit_fall()

  def check_letter_k():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'K' or apple_letter_lower == 'k'):
      fruit_fall()

  def check_letter_l():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'L' or apple_letter_lower == 'l'):
      fruit_fall()

  def check_letter_m():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'M' or apple_letter_lower == 'm'):
      fruit_fall()

  def check_letter_n():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'N' or apple_letter_lower == 'n'):
      fruit_fall()

  def check_letter_o():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'O' or apple_letter_lower == 'o'):
      fruit_fall()

  def check_letter_p():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'P' or apple_letter_lower == 'p'):
      fruit_fall()

  def check_letter_q():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'Q' or apple_letter_lower == 'q'):
      fruit_fall()

  def check_letter_r():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'R' or apple_letter_lower == 'r'):
      fruit_fall()

  def check_letter_s():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'S' or apple_letter_lower == 's'):
      fruit_fall()

  def check_letter_t():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'T' or apple_letter_lower == 't'):
      fruit_fall()

  def check_letter_u():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'U' or apple_letter_lower == 'u'):
      fruit_fall()

  def check_letter_v():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'V' or apple_letter_lower == 'v'):
      fruit_fall()

  def check_letter_w():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'W' or apple_letter_lower == 'w'):
      fruit_fall()

  def check_letter_x():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'X' or apple_letter_lower == 'x'):
      fruit_fall()

  def check_letter_y():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'Y' or apple_letter_lower == 'y'):
      fruit_fall()

  def check_letter_z():
    global apple_letter
    global apple_letter_lower
    if(apple_letter == 'Z' or apple_letter_lower == 'z'):
      fruit_fall()

  '''

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


wn.listen()
wn.mainloop()