vuosi = int(input("Anna vuosi. "))
if vuosi%400<=0 and vuosi%100 == 0:
    print("Vuosi on karkausvuosi. ")
elif vuosi%4 == 0 and not vuosi%100 == 0:
    print("Vuosi on karkausvuosi. ")
else: print("Vuosi ei ole karkausvuosi. ")