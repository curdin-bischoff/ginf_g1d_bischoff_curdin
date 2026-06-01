import random as rd

wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
tag = rd.choice(wochentage)
print(f"Heute ist: {tag}")
if tag != "Sonntag":
  print("Heute ist ein Werktag")
print("Ich wünsche Ihnen einen schönen Tag")
