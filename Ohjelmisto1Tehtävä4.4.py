import random
vastaus = random.randint(1,10)
syote = int(input("Mitä lukua mietin? "))
while syote != vastaus:
    if syote > vastaus:
        print("Liian suuri arvaus. ")
    elif syote < vastaus:
        print("Liian pieni arvaus. ")
    syote = int(input("Mitä lukua mietin? "))
if syote == vastaus:
    print("Oikein. ")