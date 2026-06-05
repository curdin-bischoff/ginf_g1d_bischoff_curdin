import random as rd
import calendar as cal

jahr = rd.randrange(1900, 2026)
antwort = cal.isleap(jahr)
print("Zufälliges Jahr:")
print(jahr)
print("Ist es ein Schaltjahr?")
print(antwort)
  