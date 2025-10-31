import random
import turtle

length_diameter = random.randrange(10, 30)
orange_color = "orange"
x_coordinate = random.randrange(-100, 101)
y_coordinate = random.randrange(-100, 101)
turtle.pu()
turtle.pencolor(orange_color)
turtle.goto(x_coordinate, y_coordinate)
turtle.dot(length_diameter)
