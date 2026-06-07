import random as rd

konto = rd.randrange(100, 1001)
zinsen_arten = [0.01, 0.025, 0.03, 0.035, 0.04, 0.05]
zins = rd.choice(zinsen_arten)
zinssatz = zins*100
zinsen = zins*konto
neues_konto = konto + zinsen
print("Jahresende - Kontoauszug")
print(f"Kontostand: CHF {konto}")
print(f"Zinssatz: {zinssatz} %")
print(f"Zinsen: CHF {zinsen}")
print(f"Neuer Kontostand: CHF {neues_konto}")
print("Danke für Ihr vertrauen in die Random-Bank")
