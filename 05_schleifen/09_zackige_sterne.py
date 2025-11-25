import turtle as t
import random as rd

farbe = "blue"
a = rd.randrange(50, 201)

t.pencolor(farbe)
t.speed(10)

for _ in range(5):
    for _ in range(5):
        t.fd(a)
        t.lt(144)
    t.lt(144)
    a = rd.randrange(50, 201)
