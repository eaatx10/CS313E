#  File: USFlag.py
#  Description: This program draws the US flag using turtle graphics.
#  Student's Name:Elias Ansari
#  Student's UT EID:eaa957
#  Course Name: CS 313E 
#  Unique Number: 50950


def drawRectangle(ttl, startx, starty, flagWidth, flagHeight):
    ttl.penup()
    ttl.goto(0,flagHeight/2)
    ttl.pendown()
    ttl.forward(flagWidth/2)
    ttl.right(90)
    ttl.forward(flagHeight)
    ttl.right(90)
    ttl.forward(flagWidth)
    ttl.right(90)
    ttl.forward(flagHeight)
    ttl.right(90)
    ttl.forward(flagWidth/2)

def drawStripes(ttl, startx, starty, flagWidth, flagHeight, stripe):
    for i in range (0,7):
        ttl.penup()
        ttl.goto(startx, starty)
        ttl.pendown()
        ttl.color("red")
        ttl.begin_fill()
        ttl.forward(flagWidth)
        ttl.right(90)
        ttl.forward(stripe)
        ttl.right(90)
        ttl.forward(flagWidth)
        ttl.right(90)
        ttl.forward(stripe)
        ttl.right(90)
        ttl.end_fill()

        starty -= stripe * 2

def drawCanton (ttl, startx, starty, cantonWidth, cantonHeight):
    ttl.penup()
    ttl.goto(startx, starty)
    ttl.pendown()
    ttl.color("blue")
    ttl.begin_fill()
    ttl.forward(cantonWidth)
    ttl.right(90)
    ttl.forward(cantonHeight)
    ttl.right(90)
    ttl.forward(cantonWidth)
    ttl.right(90)
    ttl.forward(cantonHeight)
    ttl.end_fill()

def drawStars (ttl, startx, starty, flagWidth, cantonWidth, cantonHeight, starRadius, starDiameter, starOutline):
    ttl.speed(.5)
    for i in range (0,6):
        startx = (-flagWidth/2 + cantonWidth/12)
        for i in range (0,6):
            ttl.penup()
            ttl.goto(startx, starty)
            ttl.setheading(0)
            ttl.left(18)
            ttl.forward(starRadius)
            ttl.left(162)
            ttl.pendown()
            ttl.color("white")
            ttl.begin_fill()
            ttl.forward(starOutline)
            ttl.right(72)

            for i in range (0,4):
                ttl.forward(starOutline)
                ttl.left(144)
                ttl.forward(starOutline)
                ttl.right(72)

            ttl.forward(starOutline)
            ttl.setheading(0)
            ttl.end_fill()
            startx += cantonWidth/6
        starty -= cantonHeight/6

def drawStars2 (ttl, startx, starty, flagWidth, cantonWidth, cantonHeight, starRadius, starDiameter, starOutline):
    ttl.speed(.5)
    for i in range (0,5):
        startx = (-flagWidth/2 + (2 * cantonWidth/12))
        for i in range (0,5):
            ttl.penup()
            ttl.goto(startx, starty)
            ttl.setheading(0)
            ttl.left(18)
            ttl.forward(starRadius)
            ttl.left(162)
            ttl.pendown()
            ttl.color("white")
            ttl.begin_fill()
            ttl.forward(starOutline)
            ttl.right(72)

            for i in range (0,4):
                ttl.forward(starOutline)
                ttl.left(144)
                ttl.forward(starOutline)
                ttl.right(72)

            ttl.forward(starOutline)
            ttl.setheading(0)
            ttl.end_fill()
            startx += cantonWidth/6
        starty -= cantonHeight/6

def main():

    import turtle, math

    
    ttl = turtle.Turtle()
    ttl.speed(0)

    tall = int(input("Enter the vertical height (the hoist) of the flag in pixels: "))

    flagWidth = 1.9 * tall

    flagHeight = tall

    turtle.setup(flagWidth + 100, flagHeight + 100)

    stripe = flagHeight / 13

    cantonHeight = 7 * stripe
               
    cantonWidth = .4 * flagWidth

    starDiameter = (flagHeight/13) * .8

    starRadius = (4 * flagHeight)/130

    starOutline = (math.sin(math.radians(36)) * starRadius)/(math.sin(math.radians(126)))

    # call rectangle function to draw rectangle
    drawRectangle(ttl, 0, flagHeight/2, flagWidth, flagHeight)

    # call stripe function to draw stripes
    drawStripes(ttl, -flagWidth/2, flagHeight/2, flagWidth, flagHeight, stripe)

    # call canton function to draw canton
    drawCanton(ttl, -flagWidth/2, flagHeight/2, cantonWidth, cantonHeight)

    # call star function to draw stars
    drawStars(ttl, (-flagWidth/2 + cantonWidth/12), (flagHeight/2 - cantonHeight/12), flagWidth, cantonWidth, cantonHeight, ((4 * flagHeight)/130), ((flagHeight/13) * .8), (math.sin(math.radians(36))* starRadius)/math.sin(math.radians(126)))

    # call star2 function to draw the rest of the stars
    drawStars2(ttl, (-flagWidth/2 + cantonWidth/12), (flagHeight/2 - (2 * cantonHeight/12)), flagWidth, cantonWidth, cantonHeight, ((4 * flagHeight)/130), ((flagHeight/13) * .8), (math.sin(math.radians(36))* starRadius)/math.sin(math.radians(126)))

    
main()
