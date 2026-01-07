import random as rd
import math as m

radien = [10, 15, 20, 25, 30, 35, 40, 45, 50]
radius = rd.choice(radien)
umfang = 2 * m.pi * radius
flaeche = m.pi * radius**2
umfang_gerundet = round(umfang, 1)
flaeche_gerundet = round(flaeche, 1)
print("Kreisberechnungen")
print(f"r: {radius}")
print(f"u: {umfang} und gerundet: {umfang_gerundet}")
print(f"u: {flaeche} und gerundet: {flaeche_gerundet}")