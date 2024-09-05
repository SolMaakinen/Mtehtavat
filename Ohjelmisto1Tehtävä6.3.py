def muunnos(gallon):
    return gallon * 3.785

gallon = int(input("Anna bensiinin määrä galloneina"))

while gallon > 0:
    print(f"Tässä määrä litroina: {muunnos(gallon)}")
    gallon = int(input("Anna bensiinin määrä galloneina"))