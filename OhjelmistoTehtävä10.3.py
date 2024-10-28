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

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]  # Luodaan hissit

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        if 0 <= hissi_numero < len(self.hissit):
            print(f"Ajetaan hissiä numero {hissi_numero + 1} kohdekerrokseen {kohde_kerros}.")
            hissi = self.hissit[hissi_numero]
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print("Virhe: Hissin numero ei ole kelvollinen.")

# Pääohjelma
# Luodaan talo, jossa alin kerros on 1, ylin kerros on 10 ja talossa on 3 hissiä
talo = Talo(1, 10, 3)

# Ajetaan talon eri hisseillä
print("\nAjetaan ensimmäistä hissiä viidenteen kerrokseen:")
talo.aja_hissiä(0, 5)

print("\nAjetaan toista hissiä seitsemänteen kerrokseen:")
talo.aja_hissiä(1, 7)

print("\nAjetaan kolmatta hissiä ylimpään kerrokseen:")
talo.aja_hissiä(2, 10)

print("\nPalataan ensimmäisen hissin avulla takaisin alimpaan kerrokseen:")
talo.aja_hissiä(0, 1)
