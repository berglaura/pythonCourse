def pituus():
    print("Valitse pituusyksikkö seuraavien joukosta syöttämällä suluissa annettu lyhenne")
    print("Tuuma (in tai \")")
    print("Jalka (ft tai ')")
    print("Jaardi (yd)")
    print("Maili (mi)")
    print()
    arvo = float(input("Anna muutettava arvo: "))
    yksikko = input("Anna muutettava yksikkö: ")
    if yksikko == "in" or yksikko == "\"":
        print("{us_arvo:.2f}\" on {si_arvo:.2f} cm".format(us_arvo=arvo, si_arvo=arvo * 2.54)) 
    elif yksikko == "ft" or yksikko == "'":
        print("{us_arvo:.2f}' on {si_arvo:.2f} cm".format(us_arvo=arvo, si_arvo=arvo * 30.48))
    elif yksikko == "yd":
        print("{us_arvo:.2f} yd on {si_arvo:.2f} m".format(us_arvo=arvo, si_arvo=arvo * 0.9144))
    elif yksikko == "mi":
        print("{us_arvo:.2f} mi on {si_arvo:.2f} km".format(us_arvo=arvo, si_arvo=arvo * 1.609344))
    else:
        print("Valitsemaasi yksikköä ei voida muuntaa")

def massa():
    print("Valitse painoyksikkö seuraavien joukosta syöttämällä suluissa annettu lyhenne")
    print("Unssi (oz)")
    print("Pauna (lb)")
    print()
    arvo = float(input("Anna muutettava arvo: "))
    yksikko = input("Anna muutettava yksikkö: ")
    if yksikko == "oz":
        print("{us_arvo:.2f} oz on {si_arvo:.2f} g".format(us_arvo=arvo, si_arvo=arvo * 28.349523125)) 
    elif yksikko == "lb":
        print("{us_arvo:.2f} lb on {si_arvo:.2f} kg".format(us_arvo=arvo, si_arvo=arvo * 0.45359237))
    else:
        print("Valitsemaasi yksikköä ei voida muuntaa")

def tilavuus():
    print("Valitse nestetilavuusyksikkö seuraavien joukosta syöttämällä suluissa annettu lyhenne")
    print("Kupillinen (cp)")
    print("Pintti (pt)")
    print("Varttigallona (qt)")
    print("Gallona (gal)")
    print()
    arvo = float(input("Anna muutettava arvo: "))
    yksikko = input("Anna muutettava yksikkö: ")
    if yksikko == "cp":
        print("{us_arvo:.2f} cp on {si_arvo:.2f} dl".format(us_arvo=arvo, si_arvo=arvo * 2.365882365)) 
    elif yksikko == "pt":
        print("{us_arvo:.2f} pt on {si_arvo:.2f} dl".format(us_arvo=arvo, si_arvo=arvo * 4.73176473))
    elif yksikko == "qt":
        print("{us_arvo:.2f} qt on {si_arvo:.2f} l".format(us_arvo=arvo, si_arvo=arvo * 0.946352946))
    elif yksikko == "gal":
        print("{us_arvo:.2f} gal on {si_arvo:.2f} l".format(us_arvo=arvo, si_arvo=arvo * 3.785411784))
    else:
        print("Valitsemaasi yksikköä ei voida muuntaa")

def lampotila():
    print("Lämpötilamuunnos Fahrenheit-asteista Celsius-asteiksi")
    fahrenheit = float(input("Anna lämpötila: "))
    celsius = (5 / 9) * (fahrenheit - 32)
    print("{us_arvo:.2f} °F on {si_arvo:.2f} °C".format(us_arvo=fahrenheit, si_arvo=celsius))

print("Tämä ohjelma muuntaa yhdysvaltalaisia yksiköitä SI-yksiköiksi")
print("Mahdolliset toiminnot:")
print("(P)ituus")
print("(M)assa")
print("(T)ilavuus")
print("(L)ämpotila")
print()
valinta = input("Tee valintasi: ").strip().lower()
if valinta == "p" or valinta == "pituus":
    pituus()
elif valinta == "m" or valinta == "massa":
    massa()
elif valinta == "t" or valinta == "tilavuus":
    tilavuus()
elif valinta == "l" or valinta == "lämpötila":
    lampotila()
else:
    print("Valitsemaasi toimintoa ei ole olemassa")