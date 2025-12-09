import calendar as cal
import random as rd 

jahr = rd.randrange(1900, 2026)
antwort = cal.isleap(jahr)
print("Zufälliges Jahr:")
print(jahr)
print("ist es ein Schaltjahr")
print(antwort)