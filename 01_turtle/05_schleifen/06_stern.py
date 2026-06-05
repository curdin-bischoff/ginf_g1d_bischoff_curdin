import turtle as t
import random as rd

a = rd.randrange(100, 201)
for _ in range(8):
    t.fd(a)
    t.bk(a)
    t.lt(45)
