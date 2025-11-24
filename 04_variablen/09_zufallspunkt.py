import random
import turtle

diameter = random.randrange(10, 30)
color = "orange"
x_coordinate = random.randrange(-100, 101)
y_coordinate = random.randrange(-100, 101)
turtle.pu()
turtle.pencolor(color)
turtle.goto(x_coordinate, y_coordinate)
turtle.dot(diameter)
