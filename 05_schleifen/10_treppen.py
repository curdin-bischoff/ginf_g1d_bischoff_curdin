import turtle as t
import random as rd

a = rd.randrange(10, 26)
t.speed(10)

for _ in range(4):
    for _ in range(10):
        t.fd(a)
        t.rt(90)
        t.fd(a)
        t.lt(90)
    t.rt(90)
    t.bk(a)
