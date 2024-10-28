class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0  # Tämänhetkinen nopeus asetetaan automaattisesti nollaksi
        self.kuljettu_matka = 0  # Kuljettu matka asetetaan automaattisesti nollaksi

    def kiihdytä(self, muutos):
        # Lasketaan uusi nopeus
        uusi_nopeus = self.nopeus + muutos
        # Varmistetaan, että nopeus ei ylitä huippunopeutta eikä alitu nollaa
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

# Pääohjelma
auto = Auto("ABC-123", 142)

# Nostetaan nopeutta +30 km/h, +70 km/h ja +50 km/h
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

# Tulostetaan auton nopeus
print(f"Tämänhetkinen nopeus: {auto.nopeus} km/h")

# Hätäjarrutus -200 km/h
auto.kiihdytä(-200)

# Tulostetaan uusi nopeus
print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")
