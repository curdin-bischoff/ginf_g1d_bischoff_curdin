import turtle
import random as rd

a = rd.randrange(75, 176)
for _ in range (4):
    turtle.fd(a)
    turtle.rt(45)
    turtle.fd(a)
    turtle.bk(a)
    turtle.lt(135)
    