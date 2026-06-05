import random as rd
import calendar as cal

überprüfungen = rd.randrange(10, 21)
for _ in range(überprüfungen):
  jahr = rd.randrange(1900, 2025)
  antwort = cal.isleap(jahr)
  print(f"Ist {jahr} ein Schaltjahr? {antwort}")
  