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

    def kulje(self, tunnit):
        # Lasketaan kuljettu matka ja lisätään se kokonaismatkaan
        kuljettu = self.nopeus * tunnit
        self.kuljettu_matka += kuljettu

# Pääohjelma
auto = Auto("ABC-123", 142)

# Nostetaan nopeutta ja ajetaan
auto.kiihdytä(60)  # Nostetaan nopeutta 60 km/h
auto.kuljettu_matka = 2000  # Asetetaan kuljettu matka esimerkin mukaisesti

# Ajetaan 1.5 tuntia nykyisellä nopeudella
auto.kulje(1.5)

# Tulostetaan auton tiedot
print(f"Tämänhetkinen nopeus: {auto.nopeus} km/h")
print(f"Kuljettu matka: {auto.kuljettu_matka} km")
