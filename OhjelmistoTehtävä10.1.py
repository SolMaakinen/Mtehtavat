class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros  # Uusi hissi alkaa aina alimmasta kerroksesta

    def siirry_kerrokseen(self, kohde_kerros):
        while self.nykyinen_kerros < kohde_kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohde_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo ylimmässä kerroksessa!")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")
        else:
            print("Hissi on jo alimmassa kerroksessa!")

# Pääohjelma
# Luodaan hissi, jossa alin kerros on 1 ja ylin kerros on 10
h = Hissi(1, 10)

# Käsketään hissi siirtymään viidenteen kerrokseen
print("Siirrytään viidenteen kerrokseen:")
h.siirry_kerrokseen(5)

# Käsketään hissi siirtymään takaisin alimpaan kerrokseen
print("Palataan alimpaan kerrokseen:")
h.siirry_kerrokseen(1)
