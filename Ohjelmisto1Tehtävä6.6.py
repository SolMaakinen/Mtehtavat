import math
def pizza(halkaisija,hinta):
    pizala= math.pi*(halkaisija/2)**2
    return hinta / pizala

halkaisija = int(input("Anna ensimmäisen pizzan halkaisija "))
hinta = int(input("Anna ensimmäisen pizzan hinta "))

halkaisija1 = int(input("Anna toisen pizzan halkaisija "))
hinta1 = int(input("Anna toisen pizzan hinta "))

if pizza(halkaisija,hinta) < pizza(halkaisija1,hinta1):
    print("Ensimmäinen pizza antaa paremman vastineen rahalle")
else:
    print("Toinen pizza antaa paremman vastineen rahalle")

