# defining drawing of horizontal row
import turtle
from turtle import *
a = turtle.Screen()
turtle.speed(100)
def create_horizontal_row():
    for i in range(4):
        pendown()
        left(90)
        forward(50)

# defining drawing of vertical row
def create_vertical_row():
    for k in range(4):
        pendown()
        left(90)
        forward(50)

# creating vertical spacing
def create_space_vertical():
    left(90)
    forward(50)
    right(90)

penup()
setposition(-150, -200)
for i in range(8):  # creating 8 horizontal top squares
    create_horizontal_row()
    forward(50)
penup()
setposition(-150, 150)
for i in range(8):  # creating 8 horizontal top squares
    create_horizontal_row()
    forward(50)
penup()
setposition(-150, -150)
for k in range(6):  # creating left vertical row
    create_vertical_row()
    create_space_vertical()
penup()
setposition(200, -150)
for k in range(6):  # creating right vertical row
    create_vertical_row()
    create_space_vertical()

a.exitonclick()