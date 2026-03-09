import math as m
import random as rd
 
radikanden =  [4, 25, 10, 99, 100, 42, 3600, 289, 2, 7]
x = rd.choice(radikanden)
y = m.sqrt(x)
z = y**2
print(f"Radikant: {x}")
print(f"Die Quadratwurzel von {x} ist {y}")
print(f"Kontrolle: Das QUadrat von {y} ist {z}.")
