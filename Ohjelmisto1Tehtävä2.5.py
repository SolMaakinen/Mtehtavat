leiviskät = float(input("Anna leiviskät. "))
naulat = float(input("Anna naulat. "))
luodit = float(input("Anna luodit. "))

kokonaisgrammat = (luodit*13.3+naulat*425.6+leiviskät*8512)
kilogrammat = int(kokonaisgrammat/1000)
grammat = (kokonaisgrammat % 1000)
print(f"Massa nykymittojen mukaan: {kilogrammat} kilogrammaa {grammat:5.2f} grammaa. ")
