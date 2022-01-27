'''
Project 1 - Turtle Art - Spring 2022
Author: 
    name: Sefunmi Ashiru 
    PID: Sefunmi

This program uses turtle graphics to generate a drawing of describe your drawing here.

I have neither given or received unauthorized assistance on this assignment.
Signed:  Sefunmi Ashiru
'''

import turtle
pen_width = 18
x = 700
y = 650
turtle.setup(x, y)
turtle.title('Project 1 - Turtle Art - Sefunmi Ashiru')

#border
def corner(x_or_y):
    return (x_or_y/2-pen_width)

turtle.penup()
turtle.goto(corner(x),corner(y))
turtle.pendown()

turtle.pensize(18)
turtle.pencolor('maroon')

turtle.goto(-corner(x),corner(y))
turtle.goto(-corner(x),-corner(y))
turtle.goto(corner(x),-corner(y))
turtle.goto(corner(x),corner(y))


#VT SIGN
turtle.penup()
turtle.goto(-corner(x*(0.8)),corner(y*(0.7)))
turtle.pendown()

turtle.pensize(5)
turtle.pencolor('black')
turtle.fillcolor('darkorange')
turtle.begin_fill()
#-
turtle.goto(-corner(x*(0.65)),corner(y*(0.7)))
#\
turtle.goto(-corner(x*(0.35)),corner(y*(0.25)))
#/
turtle.goto(-corner(x*(0.08)),corner(y*(0.7)))
#-->
turtle.goto(corner(x*(0.8)),corner(y*(0.7)))
# |
turtle.goto(corner(x*(0.8)),corner(y*(0.55)))
#<-
turtle.goto(corner(x*(0.55)),corner(y*(0.55)))
#|
turtle.goto(corner(x*(0.55)),-corner(y*(0.1)))
#-
turtle.goto(corner(x*(0.4)),-corner(y*(0.1)))
# |
turtle.goto(corner(x*(0.4)),corner(y*(0.55)))
#-
turtle.goto(corner(x*(0.1)),corner(y*(0.55)))
#/
turtle.goto(-corner(x*(0.35)),-corner(y*(0.1)))
#\
turtle.goto(-corner(x*(0.8)),corner(y*(0.7)))
turtle.end_fill()


#text field
turtle.penup()
turtle.goto(-corner(x*(0.8)),-corner(y*(0.3)))
turtle.pendown()

turtle.pensize(10)
turtle.pencolor('mediumaquamarine')
turtle.fillcolor('slategray')

turtle.begin_fill()
turtle.goto(corner(x*(0.8)),-corner(y*(0.3)))
turtle.goto(corner(x*(0.8)),-corner(y*(0.8)))
turtle.goto(-corner(x*(0.8)),-corner(y*(0.8)))
turtle.goto(-corner(x*(0.8)),-corner(y*(0.3)))
turtle.end_fill()

# text
turtle.penup()
turtle.goto(-corner(x*(0.0)),-corner(y*(0.6)))
turtle.pendown()
turtle.pencolor('white')
string = "HELLO HOKIES!"
turtle.write(string, move=False, align='center', font=('Arial', 40, 'normal'))
# circle & shape decoration


turtle.pensize(2)
turtle.pencolor('yellow')
turtle.fillcolor('orange')

turtle.penup()
turtle.goto(-corner(x*(0.5)),-corner(y*(0.3)))
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(corner(x*(0.6)),corner(y*(0.3)))
turtle.pendown()
turtle.begin_fill()
turtle.circle(20, steps=5)
turtle.end_fill()

turtle.penup()
turtle.goto(-corner(x*(0.8)),corner(y*(0.3)))
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
            
turtle.pensize(2)
turtle.pencolor('orange')
turtle.fillcolor('yellow')
            

turtle.penup()
turtle.goto(corner(x*(0.2)),corner(y*(0.6)))
turtle.pendown()
turtle.begin_fill()
turtle.circle(20, steps=6)
turtle.end_fill()

turtle.penup()
turtle.goto(-corner(x*(0.6)),corner(y*(0.6)))
turtle.pendown()
turtle.begin_fill()
turtle.circle(20, steps=6)
turtle.end_fill()

turtle.penup()
turtle.goto(corner(x*(0.3)),-corner(y*(0.67)))
turtle.pendown()
turtle.begin_fill()
turtle.circle(30, steps=3)
turtle.end_fill()
turtle.done()