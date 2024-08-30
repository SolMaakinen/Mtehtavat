import random
tulokset = []

lkm = int(input("Kuinka monta kertaa noppaa heitetään? "))

for luku in range(lkm):
    tulokset.append(random.randint(1,6))
print(f"Tässä on heittojen summa: {sum(tulokset)}")