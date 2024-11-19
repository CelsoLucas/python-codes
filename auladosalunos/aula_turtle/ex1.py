import turtle

turtle.setup(500, 500)
turtle.fillcolor("blue")
turtle.pencolor("blue")

turtle.begin_fill()
for q in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.done()