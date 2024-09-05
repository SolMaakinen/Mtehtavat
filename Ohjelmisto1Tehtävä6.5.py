luvut = []

def parilliset(luvut):
    return [i for i in luvut if i % 2 == 0]

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luku = int(luku)
    luvut.append(luku)
print(luvut)
print(parilliset(luvut))