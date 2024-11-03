import requests

def hae_saata(paikkakunta, api_avain):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}&units=metric&lang=fi"
    try:
        vastaus = requests.get(url)
        vastaus.raise_for_status()  # Tämä nostaa virheen, jos statuskoodi ei ole 200.
        data = vastaus.json()
        saakuvaus = data["weather"][0]["description"]
        lampotila_celsius = data["main"]["temp"]
        lampotila_kelvin = lampotila_celsius + 273.15

        print(f"Sää paikkakunnalla {paikkakunta}: {saakuvaus}")
        print(f"Lämpötila: {lampotila_celsius:.2f} °C / {lampotila_kelvin:.2f} K")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP-virhe: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Verkkovirhe: {req_err}")
    except KeyError:
        print("Virhe tietojen hakemisessa. Tarkista paikkakunta tai API-avain.")

# Pääohjelma
api_avain = "5e146058c07536ce27465a6d4e0ce692"
paikkakunta = input("Anna paikkakunnan nimi: ")
hae_saata(paikkakunta, api_avain)
