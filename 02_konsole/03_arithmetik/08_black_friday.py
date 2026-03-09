import random as rd
 
rabatt = rd.randrange(0, 101)
preis = rd.randrange(99, 1000)
r_zahl = preis * rabatt * 0.01
n_preis = preis - r_zahl
 
print("Black Friday Aktion")
print(f"Preis: {preis}")
print(f"Rabatt: {rabatt}%")
print(f"{rabatt}% von CHF {preis} sind CHF {r_zahl}")
print(f"Neuer Preis: CHF {n_preis}")
print("Was für ein Schnäppchen!")
