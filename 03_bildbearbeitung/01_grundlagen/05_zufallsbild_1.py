import PIL.Image as img
import random as rd

bild = img.new("RGB", (100, 100))
for _ in range(7500):
    x = rd.randrange(0, 100)
    y = rd.randrange(0, 100)
    r = rd.randrange(0, 256)
    g = rd.randrange(0, 256)
    b = rd.randrange(0, 256)
    bild.putpixel((x, y), (r, g, b))
bild.save("05_zufallsbild_1_ergebnis.png")
