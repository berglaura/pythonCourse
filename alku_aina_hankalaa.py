def pyyda_syote(pyynto, virheviesti):
    while True:
        try:
            luku = int(input(pyynto))
        except ValueError:
            print(virheviesti)
        else:
            if luku <= 1:
                print(virheviesti)
            else:
                return luku

def tarkista_alkuluku(luku):
    for i in range(2, luku):
        if luku % i == 0:
            return False
    return True

luku = pyyda_syote(
    "Anna kokonaisluku, joka on suurempi kuin 1: ",
    "Pieleen meni :'(."
)
alkuluku = tarkista_alkuluku(luku)
if alkuluku == True:
    print("Kyseessä on alkuluku.")
else:
    print("Kyseessä ei ole alkuluku.")
