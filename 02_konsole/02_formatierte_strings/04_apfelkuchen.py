import random as rd

Anzahl_kuchenstücke = rd.randrange(1, 13)
print(f"Sie erhalten {Anzahl_kuchenstücke} Stücke von diesem leckeren Apfelkuchen.")
for _ in range(Anzahl_kuchenstücke):
  print("Kuchenstück")
