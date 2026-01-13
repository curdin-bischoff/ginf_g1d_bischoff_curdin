import random as rd

a = rd.randrange(1, 101)
b = rd.randrange(1, 101)
erste_formel = (a + b)**2
zweite_formel = (a - b)**2
dritte_formel = (a + b) * (a - b)
print(f"1. Binomische Formel: ({a} + {b})({a} + {b}) = {erste_formel}")
print(f"2. Binomische Formel: ({a} - {b})({a} - {b}) = {zweite_formel}")
print(f"3. Binomische Formel: ({a} + {b})({a} - {b}) = {dritte_formel}")
