import turtle as t
import random as rd 

farbe = "orange"
durchmesser = rd.randrange(10,31)
x = rd.randrange(-100, 101)
y = rd.randrange(-100, 101)
t.pu()
t.goto(x, y)
t.pd()
t.pencolor(farbe)
t.dot(durchmesser)