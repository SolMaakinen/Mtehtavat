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

# Aliluokka Sähköauto
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)  # Kutsutaan yliluokan alustajaa
        self.akkukapasiteetti = akkukapasiteetti  # Asetetaan akkukapasiteetti

# Aliluokka Polttomoottoriauto
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)  # Kutsutaan yliluokan alustajaa
        self.bensatankin_koko = bensatankin_koko  # Asetetaan bensatankin koko

# Pääohjelma
# Luodaan yksi sähköauto ja yksi polttomoottoriauto
sahkoauto = Sähköauto("ABC-15", 180, 52.5)  # Akkukapasiteetti 52.5 kWh
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)  # Bensatankin koko 32.3 litraa

# Asetetaan autojen nopeudet
sahkoauto.kiihdytä(120)  # Sähköauto kiihdytetään 120 km/h nopeuteen
polttomoottoriauto.kiihdytä(100)  # Polttomoottoriauto kiihdytetään 100 km/h nopeuteen

# Ajetaan autoilla 3 tuntia
sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

# Tulostetaan autojen matkamittarilukemat
print(f"Sähköauton matkamittarilukema: {sahkoauto.kuljettu_matka} km")
print(f"Polttomoottoriauton matkamittarilukema: {polttomoottoriauto.kuljettu_matka} km")
