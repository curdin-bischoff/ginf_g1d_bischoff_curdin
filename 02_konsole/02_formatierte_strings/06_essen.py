import random as rd

speisen = ["Pommes", "Linsen-Dal", "Spaghetti", "Coq au Vin"]
speise = rd.choice(speisen)

wochentage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
wochentag = rd.choice(wochentage)
print(f"Am {wochentag} gibt es {speise} in der Mensa.")
print("Wie finden wir das?")
zahlen = [5, 42, 16, 8, 99]
anzahl = rd.choice(zahlen)
for _ in range(anzahl):
    print("Juhu")
