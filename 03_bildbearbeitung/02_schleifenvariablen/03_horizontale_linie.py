import PIL.Image as img
import random as rd 

bild = img.new("RGB", (10, 5))
r = rd.randrange(0, 256)
g = rd.randrange(0, 256)
b = rd.randrange(0, 256)
farbe = (r, g, b)
for x in range(0, 10):
    bild.putpixel((x, 2), farbe)
bild.save("03_horizontale_linie_ergebnis.png")
