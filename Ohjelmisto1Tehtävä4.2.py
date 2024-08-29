tuumat = float(input("Anna tuumamäärä"))

sentti = tuumat*2.54
while sentti >0:
    print(f"Tässä tuumat sentteinä: {tuumat*2.54}")
    tuumat = float(input("Anna tuumamäärä"))
    if tuumat <0:
        break
