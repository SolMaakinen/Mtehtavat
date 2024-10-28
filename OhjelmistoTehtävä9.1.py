class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0  # Tämänhetkinen nopeus asetetaan automaattisesti nollaksi
        self.kuljettu_matka = 0  # Kuljettu matka asetetaan automaattisesti nollaksi

# Pääohjelma
auto = Auto("ABC-123", 142)

# Tulostetaan auton kaikki ominaisuudet
print(f"Rekisteritunnus: {auto.rekisteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Tämänhetkinen nopeus: {auto.nopeus} km/h")
print(f"Kuljettu matka: {auto.kuljettu_matka} km")
