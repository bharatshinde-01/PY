
import turtle
import math

screen = turtle.Screen()
screen.setup(850, 850)
screen.bgcolor("#050505")
screen.title("Golden Galaxy Animation")
screen.tracer(0)

flower = turtle.Turtle()
flower.hideturtle()
flower.speed(0)
flower.pensize(2)

particles = turtle.Turtle()
particles.hideturtle()
particles.speed(0)

frame = 0

def draw_petal(radius, angle, color):
    flower.penup()
    flower.goto(0, 0)
    flower.setheading(angle)
    flower.pendown()
    flower.pencolor(color)

    flower.circle(radius, 60)
    flower.left(120)
    flower.circle(radius, 60)

def animate():
    global frame

    flower.clear()
    particles.clear()

    # Rotating golden flower
    for i in range(18):
        angle = i * 20 + frame * 2
        colors = ["#FFD700", "#DAA520", "#FFF0A0"]
        draw_petal(150, angle, colors[i % 3])

    # Inner rotating flower
    for i in range(12):
        angle = i * 30 - frame * 3
        draw_petal(85, angle, "#FFE680")

    # Orbiting golden particles
    for i in range(24):
        angle = math.radians(i * 15 + frame * 4)
        radius = 205 + 12 * math.sin(
            math.radians(frame * 3 + i * 20)
        )

        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        particles.penup()
        particles.goto(x, y)
        particles.dot(5 if i % 2 == 0 else 3, "#FFD700")

    # Shining center
    particles.penup()
    particles.goto(0, -12)
    particles.dot(24, "#B8860B")

    particles.goto(0, -6)
    particles.dot(12, "#FFF0A0")

    screen.update()
    frame += 1

    screen.ontimer(animate, 40)

animate()
turtle.done()
