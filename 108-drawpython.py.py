#e2.1DrawPython.py
import turtle
turtle.setup(650, 350, 200, 200,)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("red")
turtle.seth(-40)
for i in range(4):
    turtle.pencolor("purple")
    turtle.circle(40,80)
    turtle.pencolor("blue")
    turtle.circle(-40,80)
    turtle.pencolor("yellow")
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
