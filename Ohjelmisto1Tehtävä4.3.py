luku1 = float(input("Anna luku: "))
pienin = suurin = luku1

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luku = float(luku)
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku

print(f"Pienin luku on: {pienin}")
print(f"Suurin luku on: {suurin}")