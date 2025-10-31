import random
import turtle

D = random.randrange(10, 30)
Orange = "orange"
x = random.randrange(-100, 101)
y = random.randrange(-100, 101)

turtle.pu()
turtle.pencolor(Orange)
turtle.goto(x, y)
turtle.dot(D)
