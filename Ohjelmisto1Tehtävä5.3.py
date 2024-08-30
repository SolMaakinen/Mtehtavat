luku = int(input("Anna luku: "))

if luku > 1:
    for x in range(2, luku):
        if (luku % x) == 0:
            print("Luku ei ole alkuluku.")
            break
    else:
        print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")
