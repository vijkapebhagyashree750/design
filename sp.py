import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtle.bgcolor("black")

for i in range(200):
    t.pencolor(colors[i % 6])
    t.forward(i)
    t.right(59)

turtle.done()