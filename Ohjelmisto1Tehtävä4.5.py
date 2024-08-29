oikeatunnus = "python"
oikeasalasana = "rules"

yritys = 0
maxyritys = 5

while yritys < maxyritys:
    tunnus = input("Anna käyttäjätunnus. ")
    salasana = input("Anna salasana. ")

    if tunnus == oikeatunnus and salasana == oikeasalasana:
        print("Tervetuloa!")
        break
    else:
        print("Pääsy evätty")
        yritys += 1

if yritys == maxyritys:
    print("Pääsy evätty")

