#20181599 김진명
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.goto(0,100)
t.pencolor("red")
t.dot(250)
t.pencolor("blue")
t.dot(200)

t.pencolor("white")
t.penup()
t.goto(-15,115)
t.pendown()
t.pensize(7)
for i in range(1, 6):
    t.left(72)
    t.forward(50)
    t.right(144)
    t.forward(50)

t.penup()
t.goto(0,-40)
t.pencolor("red")
t.pendown()
t.pensize(16)
t.penup()
t.goto(0,-77)
t.pendown()
t.circle(180)
