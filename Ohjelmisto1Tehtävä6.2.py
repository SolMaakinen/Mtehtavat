import random
tahkot = int(input("Kuinka monta tahkoa nopassa on? "))
def heitto():
    return random.randint(1,tahkot)


tulos = 0
while tulos != tahkot:
    heitto()
    tulos = heitto()
    print(tulos)