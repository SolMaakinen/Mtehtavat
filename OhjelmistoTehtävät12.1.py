import requests


def fetch_chuck_norris_joke():
    # Hae satunnainen vitsi Chuck Norris API
    response = requests.get("https://api.chucknorris.io/jokes/random")

    # Tarkista, että vastaus on onnistunut
    if response.status_code == 200:
        joke = response.json().get("value")  # Hae pelkkä vitsin teksti
        print(joke)  # Tulosta vitsi käyttäjälle
    else:
        print("Jotain meni pieleen vitsiä haettaessa.")


# Kutsu funktiota hakeaksesi ja tulostaaksesi vitsin
fetch_chuck_norris_joke()
