import math
import turtle
window = turtle.Screen()
window.setup(width=400, height=400)  # standardize the size of the screen
pen = turtle.Turtle()
pen.pensize(4)
pen.color('red')

a_len = float(input("enter value for side 'A': "))
b_len = float(input("enter value for side 'B': "))
c_len = float(input("enter value for side 'C': "))

#process the triangles angles
angA = (b_len**2 + c_len**2 - a_len**2) / (2*b_len*c_len)
angA = math.acos(angA)
angA = math.degrees(angA)

angB = (c_len**2 + a_len**2 - b_len**2) / (2*c_len*a_len)
angB = math.acos(angB)
angB = math.degrees(angB)
angC= 180 - angA - angB

if a_len + b_len > c_len and a_len + c_len > b_len and b_len + c_len > a_len:
    pen.penup()
    pen.goto(-100,0)
    pen.pendown()

    pen.forward(a_len)
    pen.left(180 - angA)

    pen.forward(b_len)
    pen.left(180 - angB)

    pen.forward(c_len)
    
    print("Angle A is ", angA)
    print("Angle B is ", angB)
    print("Angle C is", angC)
    
else:
    print("The sides provided do not form a triangle.")

turtle.exitonclick()