import mysql.connector
from geopy.distance import geodesic

def hae_koordinaatit(icao_code):
        yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='2c1dr21n',
            autocommit=True
        )

        kursori = yhteys.cursor()

        sql_kysely = """SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"""

        kursori.execute(sql_kysely, (icao_code,))

        tulos = kursori.fetchone()

        if tulos:
            return (tulos[0], tulos[1])
        else:
            print(f"Lentokenttää ICAO-koodilla {icao_code} ei löytynyt.")
            return None

def laske_etaisyys(icao1, icao2):
    koordinaatit1 = hae_koordinaatit(icao1)
    koordinaatit2 = hae_koordinaatit(icao2)

    if koordinaatit1 and koordinaatit2:
        etaisyys = geodesic(koordinaatit1, koordinaatit2).kilometers
        print(f"Etäisyys {icao1} ja {icao2} välillä on {etaisyys:.2f} kilometriä.")
    else:
        print("Etäisyyden laskeminen epäonnistui. Tarkista ICAO-koodit.")

icao1 = input("Anna ensimmäinen ICAO-koodi: ").upper()
icao2 = input("Anna toinen ICAO-koodi: ").upper()

laske_etaisyys(icao1, icao2)