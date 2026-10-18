import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("BHARAT SHINDE")
t = turtle.Turtle()
t.speed(2)
t.hideturtle()
colors = ["pink","red", "Yellow", "yello"]
for i in range(50):
    t.color(colors[ i % 3 ])
    t.forward(i * 2)
    t.left(50)
    t.bk (10)
    t.right(100)
    t.speed(20)
    t.circle(25)
turtle.done