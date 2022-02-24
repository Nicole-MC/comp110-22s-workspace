"""The Ice King's Kingdom from Adventure Time."""

__author__ = 730388398

from turtle import Turtle, bgcolor, colormode, done
from random import randint
 

def main() -> None:
    """The entrypont of my scene."""
    paint_brush: Turtle = Turtle()
    paint_brush.speed(0)
    paint_brush.hideturtle

    # Calling Functions
    background(paint_brush)
    stars(paint_brush)
    moon(paint_brush, -200, 180, 50, 0)
    moon(paint_brush, -170, 180, 50, 1)
    mountains(paint_brush, -180, -190, 520)
    clouds(paint_brush, -650, -290)
    mountains(paint_brush, -160, -390, 400)
    mountains(paint_brush, 320, -300, 450)
    mountains(paint_brush, -770, -300, 450)
    mountains(paint_brush, 120, -300, 380)
    mountains(paint_brush, -400, -300, 380)
    foreground(paint_brush)
    clouds(paint_brush, -650, -390)
    mouth(paint_brush, 47, 72, 60)
    eyes(paint_brush, 54, 140, 6)
    eyes(paint_brush, 100, 140, 6)
    other_ice(paint_brush, -205, 38)
    other_ice(paint_brush, -540, 105)
    other_ice(paint_brush, 548, 105)
    other_ice(paint_brush, 312, 38)
    other_ice(paint_brush, 40, -30)
    ice_cap(paint_brush, 26, 176)
    
    done()


# Background
def background(paintbrush: Turtle) -> None:
    """Running this function will make the background of the screen blue."""
    colormode(255)
    bgcolor(15, 21, 61) 


# This is just a white rectangle that I used for better coverage for the clouds. 
def foreground(paint_brush: Turtle) -> None:
    """Running this function will create a white rectangle across the entire screen."""
    paint_brush.penup
    paint_brush.goto(-800, -300)
    paint_brush.pendown
    paint_brush.begin_fill()
    paint_brush.color("white")
    paint_brush.forward(1550)
    paint_brush.right(90)
    paint_brush.forward(500)
    paint_brush.right(90)
    paint_brush.forward(1550)
    paint_brush.right(90)
    paint_brush.forward(500)
    paint_brush.right(90)
    paint_brush.end_fill()


# clouds
# I couldnt figure out how to randomly rotate the circles to make clouds, so I went with a row of three different sizes.
def clouds(paint_brush: Turtle, x: float, y: float) -> None:
    """Draw a row of white circles of various sizes at the given location of x,y."""
    fluff: int = 0
    puff_order: int = 2
    alternate: int = 0

    paint_brush.penup()
    paint_brush.goto(x, y)
    paint_brush.pendown()
    paint_brush.color("white")
    paint_brush.begin_fill()
    while fluff < 10:
        if alternate == 1:
            paint_brush.circle(68)
            paint_brush.forward(150)
            alternate -= 1
        if puff_order % 2 == 0:
            paint_brush.circle(75)
            paint_brush.forward(145)
            alternate += 1
        else:
            paint_brush.circle(90)
            paint_brush.forward(150)
            alternate += 1
        fluff += 1
        puff_order += 1
    paint_brush.end_fill()
    paint_brush.penup()
    

# Mountains
def mountains(paint_brush: Turtle, x: float, y: float, width: float) -> None:
    """Draw a triangle of the given width at the location of x, y."""
    colormode(255)
    paint_brush.penup()
    paint_brush.goto(x, y)
    paint_brush.pendown()
    paint_brush.begin_fill()
    paint_brush.color((147, 235, 232), (1, 1, 145))
    i: int = 0
    while i < 3:
        paint_brush.forward(width)
        paint_brush.left(120)
        i += 1
    paint_brush.end_fill()
    paint_brush.penup()


# Moon <3 
# I wanted to make a cresent moon!
def moon(paint_brush: Turtle, x: float, y: float, radius: float, color: float) -> None:
    """Draw a circle of the given radius and color number at the location of x, y."""
    paint_brush.penup()
    paint_brush.goto(x, y)
    paint_brush.pendown()
    colormode(255)
    if color == 0:
        paint_brush.color(228, 228, 195)
    else:
        paint_brush.color(15, 21, 61)
    paint_brush.begin_fill()
    paint_brush.circle(radius)
    paint_brush.end_fill() 
    

# * stars *
def stars(paint_brush: Turtle) -> None:
    """Run function to randomly scatter 40 dots around the background of the scene."""
    colormode(255)
    paint_brush.color(15, 21, 61)
    scatter: int = 0
    while scatter < 40:
        paint_brush.penup
        x = randint(-700, 700)
        y = randint(-200, 500)
        paint_brush.goto(x, y)
        paint_brush.pendown
        paint_brush.color("white")
        paint_brush.begin_fill()
        paint_brush.circle(2)
        paint_brush.end_fill()
        paint_brush.penup()
        scatter += 1


# Face :)
# The main mountain has a face which acts at the enterance into the "kingdom."
def mouth(paint_brush: Turtle, x: float, y: float, width: float) -> None:
    """Draw a light blue triangle of the given width at the location of x, y."""
    paint_brush.penup()
    paint_brush.goto(x, y)
    paint_brush.pendown()
    colormode(255)
    paint_brush.color(147, 235, 232)
    paint_brush.begin_fill()
    i: int = 0
    while i < 3:
        paint_brush.forward(width)
        paint_brush.left(120)
        i += 1
    paint_brush.end_fill()


# Eyes 0 - 0
def eyes(paint_brush: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a light blue cricle with a given radius at the location of x, y."""
    paint_brush.penup()
    paint_brush.goto(x, y)
    paint_brush.pendown()
    colormode(255)
    paint_brush.color(151, 255, 252)
    paint_brush.begin_fill()
    paint_brush.circle(radius)
    paint_brush.end_fill()


# Ice cap on the center mountain ^
def ice_cap(paint_brush: Turtle, x: float, y: float) -> None:
    """Run to place ice cap on the center mountain at x,y location."""
    paint_brush.penup()
    paint_brush.goto(x, y)
    paint_brush.pendown()
    colormode(255)
    paint_brush.color(147, 235, 232)
    paint_brush.begin_fill()
    paint_brush.left(20)
    paint_brush.forward(45)
    paint_brush.right(75)
    paint_brush.forward(15)
    paint_brush.left(85)
    paint_brush.forward(30)
    paint_brush.right(70)
    paint_brush.forward(50)
    paint_brush.left(155)
    paint_brush.forward(145)
    paint_brush.end_fill() 


def other_ice(paint_brush: Turtle, x: float, y: float) -> None:
    """Run to place an ice cap on smaller mountains at the x, y location."""
    paint_brush.penup()
    paint_brush.goto(x, y)
    paint_brush.pendown()
    colormode(255)
    paint_brush.color(147, 235, 232)
    paint_brush.begin_fill()
    paint_brush.right(120)
    paint_brush.forward(120)
    paint_brush.left(150)
    paint_brush.forward(80)
    paint_brush.right(70)
    paint_brush.forward(50)
    paint_brush.left(160)
    paint_brush.forward(104)
    paint_brush.right(120)
    paint_brush.end_fill() 


if __name__ == "__main__":
    main()









    
# https://static.wikia.nocookie.net/adventuretimewithfinnandjake/images/4/42/5096598513_3214217d0f.jpg/revision/latest/scale-to-width-down/185?cb=20110302004337
# this is the image I used as a reference ^ I tried to simplify it with the clouds. I also couldnt figure out an easy way to draw and fill in the patterns on the mountains, so sorry for leaving that out. 