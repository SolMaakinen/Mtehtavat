import random
#Pisteiden kokonaismäärä
N = 1000000
#Pisteet ympyrän sisällä
inside_circle = 0
suoritettu = 0

while suoritettu != N:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
        suoritettu += 1

pi = (4 * inside_circle) / N
print(f"Piin likiarvo: {pi}")

