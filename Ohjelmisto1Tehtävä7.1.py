# Määritellään vuodenajat kuukausien perusteella monikkotietorakenteena
vuodenajat = ("talvi", "kevät", "kesä", "syksy")

# Määritellään kuukausia vastaavat vuodenajat (1-12 kuukausille)
kuukausien_vuodenajat = (vuodenajat[0], vuodenajat[0], vuodenajat[1], vuodenajat[1], vuodenajat[1], vuodenajat[2], vuodenajat[2], vuodenajat[2], vuodenajat[3], vuodenajat[3], vuodenajat[3], vuodenajat[0])

# Kysytään käyttäjältä kuukauden numero
kuukausi = int(input("Anna kuukauden numero (1-12): "))

# Tarkistetaan, että annettu kuukausi on välillä 1-12
if 1 <= kuukausi <= 12:
    # Tulostetaan kuukautta vastaava vuodenaika
    print(f"Kuukauden {kuukausi} vuodenaika on {kuukausien_vuodenajat[kuukausi - 1]}.")
else:
    print("Virheellinen kuukausi. Anna numero väliltä 1-12.")
