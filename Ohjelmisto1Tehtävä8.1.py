import mysql.connector

def hae_icao(icao_code):
        icao_code = icao_code.upper()
        yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='2c1dr21n',
            autocommit=True
        )

        kursori = yhteys.cursor()

        sql_kysely = f"SELECT name, municipality FROM airport WHERE ident = '{icao_code}'"
        kursori.execute(sql_kysely)
        tulos = kursori.fetchone()

        if tulos:
            print(f"Airport Name: {tulos[0]}, Municipality: {tulos[1]}")
        else:
            print("No airport found with the given ICAO code.")

icao_code = input("Anna ICAO-koodi: ")
hae_icao(icao_code)
