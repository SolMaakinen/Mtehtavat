nimet = set()

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
for nimi in nimet:
    print(nimi)


