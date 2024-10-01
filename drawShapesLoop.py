# This program draws multiple triangles.

import turtle

import random

# Create a turtle object
pen = turtle.Turtle()

# Select random position for shape and ready pen
xPos      = -300
yPos      = 200

# Loop to draw 5 triangles.  Shift right and redraw
# using general coordinates for each.
for x in range(5):

    # Reset pen position for new shape
    pen.penup()
    pen.goto(xPos,yPos)

    # Draw triangle
    pen.pendown()
    pen.forward(80)
    pen.left(120)
    pen.forward(80)
    pen.left(120)
    pen.forward(80)
    pen.left(120)

    # Shift pen position to right
    xPos = xPos + 100

