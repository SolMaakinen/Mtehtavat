import random
#Pisteiden kokonaismäärä
N = 10000000
#Kuinka monta toistoa tehty
n = 0
#Pisteet ympyrän sisällä
ympyra = 0

while n != N:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            ympyra += 1
        n += 1

pi = (4 * ympyra) / N
print(f"Piin likiarvo: {pi}")

