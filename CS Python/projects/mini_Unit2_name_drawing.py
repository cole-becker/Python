# Mini Programming Project - Turtle Graphics Resource File
# https://docs.python.org/2/library/turtle.html#
#
# Purpose to draw your name to the screen using turtle commands.
# Note: people with long names need only print the first six characters
# Note: How would you perfectly centre your name on the screen? 
#
# Author: Cole Becker
#
# Date: September 19, 2023

# setup the environment
# recall the x,y coordinate system is 0,0 in the centre of the drawing window
import turtle
window = turtle.Screen()
window.setup(width=600, height=600)  # standardize the size of the screen
pen = turtle.Turtle()
pen.pensize(3)
pen.color('cyan')
padding = 20                          # padding between letters

# relocate the turtle near the left side of the screen 
pen.penup()
pen.goto(-205,0)
pen.pendown()

# Draw the first letter of your name here C
pen.penup()
pen.goto(-115, 50)
pen.pendown()
pen.goto(-205,50)
pen.goto(-205 ,-50)
pen.goto(-115, -50)

# relocate the pen for the next letter
pen.penup()
x,y = pen.position()      # get the x and y position of the turtle
pen.goto(x+padding,0)     # set the pen to draw the next letter
pen.pendown()
# Draw the next letter of your name here . . O
pen.goto(-115+padding, -50)
pen.goto(-115+padding, 50)
pen.goto(-15+padding, 50)
pen.goto(-15+padding, -50)
pen.goto(-115+padding, -50)
pen.penup()
pen.goto(-15+padding, -50)

# relocate the pen for the next letter
pen.penup()
x,y = pen.position()      # get the x and y position of the turtle
pen.goto(x+padding, 0)     # set the pen to draw the next letter
pen.pendown()

# Draw the next letter of your name here . . . L
pen.goto(5+padding, 50)
pen.goto(5+padding, -50)
pen.goto(85+padding, -50)

# relocate the pen for the next letter
pen.penup()
x,y = pen.position()      # get the x and y position of the turtle
pen.goto(x+padding,0)     # set the pen to draw the next letter
pen.pendown()
# Draw the last letter of your name here . . E 
pen.goto(105+padding, 50)
pen.goto(185+padding, 50)
pen.goto(105+padding, 50)
pen.goto(105+padding, 0)
pen.goto(185+padding, 0)
pen.goto(105+padding, 0)
pen.goto(105+padding, -50)
pen.goto(185+padding, -50)

pen.penup()
x,y = pen.position()      # get the x and y position of the turtle
pen.goto(600,0)     # set the pen to draw the next letter
pen.pendown()

# end of program
window.mainloop() # needed in most programming environments 