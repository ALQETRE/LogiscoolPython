with open("text4.txt", mode= "r+", encoding= "utf-8") as fd:
    print(fd.read())
    fd.write("Hello")






# Cesta souboru:
#   Relativní (od main.py) MUCH BETTER (sometimes)
#   Absolutní (od C:\ neboli root)

# Modes:
#   r - Čtení (rEAD)
#   w - Psaní (wRITE)
#   a - Psaní nakonec (aPPEND)
#   x - Jen vytváření
#   r+ - čtení a psaní

# Encodings:
#   Ascii - 8bit (4bit) menší a malo pouzivana nepodporuje hacky carky
#   Unicode (utf-8) - vetsi nejcasteji pouzivane podporuje VSE