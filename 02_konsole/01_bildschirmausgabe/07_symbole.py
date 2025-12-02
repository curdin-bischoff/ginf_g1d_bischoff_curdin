import random as rd

symbol = "a", "b", "c"
symbolprint = rd.choice(symbol)
for _ in range(4):
  print(symbolprint, symbolprint, symbolprint, symbolprint)
  