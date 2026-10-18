
import turtle
import colorsys
import math

screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("#050510")
screen.title("Rainbow Flower Galaxy")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

# Rainbow flower petals
for i in range(240):
    hue = i / 240
    r, g, b = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
    t.pencolor(r, g, b)

    t.penup()
    t.goto(0, 0)
    t.pendown()

    t.setheading(i * 7)
    t.circle(180, 60)
    t.left(120)
    t.circle(180, 60)

    t.left(120)
    t.circle(180, 60)

# Inner galaxy rings
for i in range(12):
    hue = i / 12
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(r, g, b)
    t.penup()
    t.goto(0, -20 - i * 3)
    t.pendown()
    t.circle(20 + i * 3)

# Center star
t.penup()
t.goto(0, -8)
t.pendown()
t.color("white")
t.dot(18)

screen.update()
turtle.done()
