luvut = []

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luku = float(luku)
    luvut.append(luku)

luvut.sort(reverse=True)
print(luvut[0:5])