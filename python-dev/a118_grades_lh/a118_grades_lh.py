#   a118_grades.py
#   This code is incomplete. 
my_courses = ["English", "Math", "CS"]

for course in my_courses:
    redo = "y"
    while (redo == "y"):
        print() # blank line
        print("Enter your points for " + course)

        points = int(input("Points -> "))
        if(points > 105 or points < 0):
            print("Either your input is invalid, or you have a crazy score!")
        elif (points >= 90):
            print("A")
        elif (points >= 80):
            print("B")
        elif (points >= 70):
            print("C")
        elif (points >= 60):
            print("D")
        else:
            print("F")

        redo = input("Do you need to re-do these grades? (y/n)")




