import turtle

turtle.setup(500, 500)
turtle.fillcolor("red")
turtle.pencolor("red")
turtle.begin_fill()
for q in range(3):
    turtle.forward(100)
    turtle.left(120)
turtle.end_fill()
turtle.done()