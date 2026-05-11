import PIL.Image as img


bild = img.new("RGB", (10, 10))
for x in range(0, 10):
    farbe = (225, 26, 39)
    for y in range(0, 10):
        bild.putpixel((x, y), farbe)
for x in range(4, 6):
    farbe = (256, 256, 256)
    for y in range(1, 9):
        bild.putpixel((x, y), farbe)
for x in range(1, 9):
    farbe = (256, 256, 256)
    for y in range(4, 6):
        bild.putpixel((x, y), farbe)
bild.save("07_schweizer_kreuz_ergebnis.png")
