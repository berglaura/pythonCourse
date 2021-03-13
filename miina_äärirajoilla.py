def sijainti_kentalla(x, y, leveys, korkeus):
    if ((x == 0 and y == 0) or (x == 0 and y == korkeus - 1)
    or (y == 0 and x == leveys - 1) or (x == leveys - 1 and y == korkeus - 1)):
        return "nurkassa"
    elif (x < 0) or (x > leveys - 1) or (y < 0) or (y > korkeus - 1):
        return "ulkona"
    elif (x == 0) or (x == leveys - 1) or (y == 0) or (y == korkeus - 1):
        return "laidalla"
    else:
        return "keskellä"


def tulosta_sijainti(avainsana):
    print(TULOSTUKSET[avainsana])

TULOSTUKSET = {
    "ulkona": "Antamasi ruutu on kentän ulkopuolella.",
    "nurkassa": "Antamasi ruutu on kentän nurkassa.",
    "laidalla": "Antamasi ruutu on kentän laidalla.",
    "keskellä": "Antamasi ruutu on keskikentällä."
}


oma_leveys = int(input("Anna kentän leveys: "))
oma_korkeus = int(input("Anna kentän korkeus: "))
if oma_leveys <= 0 or oma_korkeus <= 0:
    print("Noin pienelle kentälle ei mahdu ainuttakaan ruutua!")
else:
    oma_x = int(input("Anna x-koordinaatti: "))
    oma_y = int(input("Anna y-koordinaatti: "))
    sijainti = sijainti_kentalla(oma_x, oma_y, oma_leveys, oma_korkeus)
    tulosta_sijainti(sijainti)
