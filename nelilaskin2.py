valinta = input("Valitse operaatio (+, -, *, /): ")
if valinta == "+":
    try:
        luku_1 = float(input("Anna luku 1: "))
        luku_2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        tulos = luku_1 + luku_2
        print("Tulos: ", tulos)
elif valinta == "-":
    try:
        luku_1 = float(input("Anna luku 1: "))
        luku_2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        tulos = luku_1 - luku_2
        print("Tulos: ", tulos)
elif valinta == "*":
    try:
        luku_1 = float(input("Anna luku 1: "))
        luku_2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        tulos = luku_1 * luku_2
        print("Tulos: ", tulos)
elif valinta == "/":
    try:
        luku_1 = float(input("Anna luku 1: "))
        luku_2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        if luku_2 == 0:
            print("Tällä ohjelmalla ei pääse äärettömyyteen")
        else:
            tulos = luku_1 / luku_2
            print("Tulos: ", tulos)
else:
    print("Operaatiota ei ole olemassa")
