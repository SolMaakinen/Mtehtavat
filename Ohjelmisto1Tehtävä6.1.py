import random
def heitto():
    return random.randint(1,6)

tulos = 0
while tulos != 6:
    heitto()
    tulos = heitto()
    print(tulos)