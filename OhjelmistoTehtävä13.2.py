from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def hae_lentokentan_tiedot(icao_koodi):
    """Hakee lentokentän nimen ja kaupungin tietokannasta annettua ICAO-koodia vastaavasti."""
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',  # Vaihda tietokannan nimi omaksi
        user='',  # Vaihda omaksi käyttäjänimeksi
        password='',  # Vaihda omaksi salasanaksi
        autocommit=True
    )

    kursori = yhteys.cursor()
    sql_kysely = """SELECT ident, name, municipality FROM airport WHERE ident = %s"""
    kursori.execute(sql_kysely, (icao_koodi,))

    tulos = kursori.fetchone()
    yhteys.close()

    if tulos:
        return {
            "ICAO": tulos[0],
            "Name": tulos[1],
            "Municipality": tulos[2]
        }
    else:
        return None


@app.route('/kenttä/<string:icao_koodi>', methods=['GET'])
def get_airport_by_icao(icao_koodi):
    """Reitti, joka palauttaa lentokentän nimen ja kaupungin JSON-muodossa ICAO-koodin perusteella."""
    lentokentan_tiedot = hae_lentokentan_tiedot(icao_koodi.upper())
    if lentokentan_tiedot:
        return jsonify(lentokentan_tiedot)
    else:
        return jsonify({"error": f"Airport with ICAO code {icao_koodi.upper()} not found"}), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
