import PIL.Image as img
import random as rd 

bild = img.new("RGB", (10, 20))
r = rd.randrange(0, 256)
g = rd.randrange(0, 256)
b = rd.randrange(0, 256)
farbe = (r, g, b)
for x in range(0, 10):
    bild.putpixel((x, 2), farbe)
for y in range(0, 20):
    bild.putpixel((2, y), farbe)
bild.save("04_kreuz_ergebnis.png")
