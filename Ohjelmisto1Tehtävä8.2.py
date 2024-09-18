import mysql.connector

def hae_lentokentat_tyypeittain(maakoodi):
        yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',  # Vaihda omaksi tietokannan nimeksi
            user='root',             # Vaihda omaksi käyttäjänimeksi
            password='2c1dr21n',     # Vaihda omaksi salasanaksi
            autocommit=True
        )

        kursori = yhteys.cursor()

        sql_kysely = """SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"""

        kursori.execute(sql_kysely, (maakoodi,))

        tulokset = kursori.fetchall()
        if tulokset:
            print(f"Lentokenttien lukumäärät maassa {maakoodi}:")
            for rivi in tulokset:
                    print(f"{rivi[0]}: {rivi[1]} kpl")
        else:
            print(f"Maasta {maakoodi} ei löytynyt lentokenttiä.")

maakoodi = input("Anna maakoodi (esim. FI): ").upper()

hae_lentokentat_tyypeittain(maakoodi)