with open("cesta_souboru.txt", mode= "r+", encoding= "utf-8") as fd:
    fd.write("Ahoj jak se mas")
    text = fd.read()
    print(text)

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


# Docházka:
#   Všichni online
#   Chyběl Michal S.