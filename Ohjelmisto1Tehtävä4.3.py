luvut = []

luku = input("Anna luku. ")
luvut.append(float(luku))
while luku != "":
    luku = input("Anna luku. ")
    if luku == "":
        break
    luvut.append(float(luku))

if luvut:
    print("Pienin luku on:", min(luvut))
    print("Suurin luku on:", max(luvut))