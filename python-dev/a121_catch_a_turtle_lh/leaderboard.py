# The leaderboard module to be used in a122 solution.
#   leaderboard.py

# set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25

# load leaderboard from file


def load_leaderboard(file_name, leader_names, leader_scores):

  # need to create the file ahead of time in same folder
  leaderboard_file = open(file_name, "r")  

  # use a for loop to iterate through the content of the file, one line at a time
  # note that each line in the file has the format "leader_name,leader_score" for example "Pat,50"
  for line in leaderboard_file:
    leader_name = ""
    leader_score = ""    
    index = 0

    # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")

    # This while loop gets the name from the leaderboard file
    while (line[index] != ","):
      leader_name = leader_name + line[index]
      index += 1

    print("leader name is:" + leader_name)


      

    # TODO 2: add the leader name to the list
    leader_names.append(leader_name)

    index += 1
    # TODO 3: read the player score using a similar loop
    while (line[index] != "\n"):
      leader_score = leader_score + line[index]
      index += 1

    print("leader score is: ", leader_score)

    
    # TODO 4: add the player score to the list
    leader_scores.append(int(leader_score))


  leaderboard_file.close()


# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):

  leader_index = 0
  
  
  while (leader_index < len(leader_scores)):
    # TODO 6: check if this is the position to insert new score at
    if (player_score >= leader_scores[leader_index]):
      leader_scores.insert(leader_index, player_score)
      leader_names.insert(leader_index, player_name)
      break
    else:
      leader_index += 1
  
  


  # TODO 8: keep both lists at 5 elements only (top 5 players)
  while(len(leader_names) > 5):
    leader_scores.pop()
    leader_names.pop()
    

  
  # store the latest leaderboard back in the file
  leaderboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
  leader_index = 0
  # TODO 9: loop through all the leaderboard elements and write them to the file

  while(leader_index < len(leader_names)):
    leaderboard_file.write(leader_names[leader_index] + "," + str(leader_scores[leader_index]) + "\n")
    leader_index = leader_index + 1
  
  leaderboard_file.close()
  

# draw leaderboard and display a message to player
def draw_leaderboard(leader_names, leader_scores, high_scorer, turtle_object, player_score):
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-200,100)
  turtle_object.hideturtle()
  turtle_object.down()
  leader_index = 0

  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  while leader_index < len(leader_names):
    turtle_object.write(str(leader_index + 1) + "\t" + leader_names[leader_index] + "\t" + str(leader_scores[leader_index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-200,int(turtle_object.ycor())-50)
    turtle_object.down()
    leader_index = leader_index + 1

  # Display message about player making/not making leaderboard based on high_scorer
  if (high_scorer):
    turtle_object.write("Congratulations! You made the leaderboard!", font=font_setup)
  else:
    turtle_object.write("Sorry, you didn't make the leaderboard. Maybe next time!", font=font_setup)

  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-200,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  # TODO 10: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
  
  bronze_score = 15
  silver_score = 20
  gold_score = 25

  if(player_score >= bronze_score and player_score < silver_score):
    turtle_object.write("You earned a bronze medal!", font=font_setup)
  elif(player_score >= silver_score and player_score < gold_score):
    turtle_object.write("You earned a silver medal!", font=font_setup)
  elif(player_score >= gold_score):
    turtle_object.write("You earned a gold medal!", font=font_setup)
  
  