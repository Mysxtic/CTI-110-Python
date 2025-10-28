# Dayvion Peoples
# 10/28/2025
# Draw a sqaure and triangle using turtle library
# Only need 1 turtle

import turtle
win = turtle.Screen()
t = turtle.Turtle()
win.bgcolor("black")

t.pensize(10)                   # increase pensize(takes integer)
t.pencolor("red")            # set pencolor(takes string)
t.shape("arrow")



# While loop to draw a square
num = 0
while num  < 4:
    t.forward(150)
    t.right(90)
    num += 1
print("while loop ends")

# For loop to draw a triangle
for tr in range(0,3):
    t.forward(150)
    t.left(120)
print("For loop has ended")


