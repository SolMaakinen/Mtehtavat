sukupuoli = input("Mikä on biologinen sukupuoli? ")
hemoglobiini = int(input("Mikä on hemoglobiiniarvo? "))

if sukupuoli == "Nainen":
    if hemoglobiini <117:
        print(" Hemoglobiiniarvo on alhainen. ")
    elif hemoglobiini <=175:
        print(" Hemoglobiiniarvo on normaali. ")
    elif hemoglobiini >175:
        print(" Hemoglobiiniarvo on korkea. ")

if sukupuoli == "Mies":
    if hemoglobiini <134:
        print(" Hemoglobiiniarvo on alhainen. ")
    elif hemoglobiini <=195:
        print(" Hemoglobiiniarvo on normaali. ")
    elif hemoglobiini >195:
        print(" Hemoglobiiniarvo on korkea. ")