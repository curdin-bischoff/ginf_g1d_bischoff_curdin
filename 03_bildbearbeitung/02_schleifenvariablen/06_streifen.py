import PIL.Image as img
import random as rd 

bild = img.new("RGB", (20, 3))
for x in range(0, 20):
    r = rd.randrange(0, 256)
    g = rd.randrange(0, 256)
    b = rd.randrange(0, 256)
    farbe = (r, g, b)
    for y in range(0, 3):
        bild.putpixel((x, y), farbe)
bild.save("06_streifen_ergebnis.png")
