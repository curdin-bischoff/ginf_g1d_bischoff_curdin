import PIL.Image as img
import random as rd

bild = img.new("RGB", (2,2))
grau_1 = rd.randrange(0, 256)
grau_2 = rd.randrange(0, 256)
grau_3 = rd.randrange(0, 256)
grau_4 = rd.randrange(0, 256)
bild.putpixel((0, 0), (grau_1, grau_1, grau_1))
bild.putpixel((1, 0), (grau_2, grau_2, grau_2))
bild.putpixel((0, 1), (grau_3, grau_3, grau_3))
bild.putpixel((1, 1), (grau_4, grau_4, grau_4))
bild.save("04_graustufen_ergebnis.png")
