import random as rd

a = rd.randrange(50, 501)
h = rd.randrange(100, 251)
c = 2*a
A = (a + c)*h/2
print("Berechnungen am Trapez")
print(f"Seitenlängen: a:{a} c:{c} h:{h} A:{A}")
