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


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus  # Kilpailun pituus kilometreinä
        self.autot = autot  # Lista kilpailuun osallistuvista autoista
        self.aika = 0  # Kilpailun kuluva aika tunneissa

    def tunti_kuluu(self):
        for auto in self.autot:
            # Arvotaan nopeuden muutos -10 ja +15 km/h välillä
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            # Käsketään auto kulkemaan yhden tunnin ajan
            auto.kulje(1)
        self.aika += 1

    def tulosta_tilanne(self):
        print(f"\nTilanne {self.aika} tunnin kohdalla:")
        print(f"{'Rekisteritunnus':<12} {'Huippunopeus (km/h)':<20} {'Nopeus (km/h)':<15} {'Kuljettu matka (km)':<20}")
        print("=" * 67)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<12} {auto.huippunopeus:<20} {auto.nopeus:<15} {auto.kuljettu_matka:<20.2f}")

    def kilpailu_ohi(self):
        # Tarkistetaan, onko jokin auto saavuttanut kilpailun pituuden
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


# Pääohjelma
# Luodaan 8000 kilometrin kilpailu nimeltä "Suuri romuralli"
kilpailun_pituus = 8000
autot = []

# Luodaan 10 autoa satunnaisilla huippunopeuksilla ja rekisteritunnuksilla
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)  # Arvotaan huippunopeus 100-200 km/h
    rekisteritunnus = f"ABC-{i}"  # Luodaan rekisteritunnus muotoa "ABC-1", "ABC-2", jne.
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

# Luodaan kilpailu
kilpailu = Kilpailu("Suuri romuralli", kilpailun_pituus, autot)

# Simuloidaan kilpailua
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()

    # Tulostetaan tilanne joka kymmenes tunti
    if kilpailu.aika % 10 == 0:
        kilpailu.tulosta_tilanne()

# Kilpailu päättyi, tulostetaan lopputilanne
print("\nKilpailu on päättynyt!")
kilpailu.tulosta_tilanne()
