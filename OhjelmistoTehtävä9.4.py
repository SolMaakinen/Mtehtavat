import random

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
# Luodaan lista kymmenestä autosta
autot = []
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)  # Arvotaan huippunopeus 100-200 km/h
    rekisteritunnus = f"ABC-{i}"  # Luodaan rekisteritunnus muotoa "ABC-1", "ABC-2", jne.
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

# Kilpailu alkaa
kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autot:
        # Arvotaan nopeuden muutos -10 ja +15 km/h välillä
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)
        # Käsketään auto kulkemaan yhden tunnin ajan
        auto.kulje(1)
        # Tarkistetaan, onko auto saavuttanut vähintään 10 000 km
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break

# Kilpailu on päättynyt, tulostetaan kaikkien autojen tiedot
print(f"{'Rekisteritunnus':<12} {'Huippunopeus (km/h)':<20} {'Nopeus (km/h)':<15} {'Kuljettu matka (km)':<20}")
print("="*67)
for auto in autot:
    print(f"{auto.rekisteritunnus:<12} {auto.huippunopeus:<20} {auto.nopeus:<15} {auto.kuljettu_matka:<20.2f}")
