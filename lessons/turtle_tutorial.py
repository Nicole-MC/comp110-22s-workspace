"""Turtle."""

from turtle import Turtle, colormode, done

leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle() 


leo.penup()
leo.goto(-120, 0) 
leo.pendown()

leo.begin_fill()
colormode(255)
leo.color(23, 43, 23)

i: int = 0 
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

leo.end_fill()

bob: Turtle = Turtle()

bob.speed(100)
bob.hideturtle()

bob.penup()
bob.goto(-110, 5)
bob.pendown()

bob.begin_fill()
colormode(255)
bob.pencolor(112, 161, 113)
# bob.color(23, 43, 23)

z: int = 0 
while (z < 3):
    bob.forward(280)
    bob.left(120)
    z += 1

side_length: int = 280

f: int = 0
while (f < 5):
    bob.forward(side_length)
    bob.left(120.5)
    side_length = side_length * 0.96
    if bob.pendown():
        bob.penup()
    else:
        bob.pendown()
    f += 1

bob.end_fill()
done()