#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic('background.gif')

letter_x_offset = -10
letter_y_offset = -30


apple = trtl.Turtle() 

letter_list = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']

apple_list =  []
#for i in apple_list

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file & display it
def draw_apple(active_apple, current_letter):
  active_apple.showturtle()
  active_apple.shape(apple_image)
  active_apple.color("blue")
  draw_letter(current_letter, active_apple)
  wn.update()


#This function draws and attaches the letters to apples
def draw_letter(current_letter, active_apple):
  global wn
  wn.tracer(False)

  active_apple.penup()
  active_apple.color("white")
  pos = active_apple.position()
  letter_x = active_apple.xcor() + letter_x_offset
  letter_y = active_apple.ycor() + letter_y_offset
  active_apple.setpos(letter_x, letter_y)
  active_apple.write(current_letter, font=("Arial", 32, "bold"))
  active_apple.setpos(pos)

  wn.tracer(True)



#Drops and hides the apples
def drop_apple():
  global apple
  apple.penup()
  x_drop_pos = apple.xcor()
  y_drop_pos = apple.ycor() - 150
  apple.goto(x_drop_pos, y_drop_pos)
  apple.clear()
  apple.hideturtle()

#Resets the position of the apple to a random location on the tree
def reset_apple(apple):
  global letter_list
  global current_letter
  letter_list_length = len(letter_list)
  if(letter_list_length > 0):
    apple.setpos(rand.randint(-100, 100), rand.randint(0, 100))
    index = rand.randint(0, 8)
    current_letter = letter_list.pop(index)


#-----function calls-----
draw_apple(apple, current_letter)
wn.onkeypress(drop_apple, "a")
wn.onkeypress(drop_apple, "A")


wn.listen()
wn.mainloop()
