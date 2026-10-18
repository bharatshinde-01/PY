import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Reel")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
colors = ["cyan", "blue", "magenta","pink"]
for i in range(500):
    t.color(colors[i % 4])
    t.forward(i * 2)
    t.left(91)
    t.dot(5)
turtle.done