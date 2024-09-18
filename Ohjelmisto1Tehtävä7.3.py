lentoasemat = {"EFHK": "Helsinki-Vantaa"}

while True:
    print("Valitse toiminto: ")
    print("1. Syötä uusi lentoasema: ")
    print("2. Hae syötetyn lentoaseman tiedot: ")
    print("3. Lopeta ohjelma. ")

    syote = input("Syötä valintasi: ")

    if syote == "1":
        icao = input("Syötä lentoaseman ICAO-koodi: ").upper()
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} lisätty, ICAO-koodilla {icao}. ")

    elif syote == "2":
        icao = input("Syötä ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoasema koodilla {icao} löytyi nimellä: {lentoasemat[icao]}")
        else:
            print(f"Lentoasemaa koodilla {icao} ei löytynyt")

    elif syote == "3":
        print("Ohjelma lopetetaan")
        break

    else:
        print("Virheellinen valinta, valitse uudelleen")


