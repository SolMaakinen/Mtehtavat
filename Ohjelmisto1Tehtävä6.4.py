luvut = []
def summa(luvut):
    return sum(luvut)

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luku = int(luku)
    luvut.append(luku)
print(summa(luvut))