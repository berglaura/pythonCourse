import haravasto

tila = {
    "kentta": []
}

def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()
    for i, rivi in enumerate(tila["kentta"]):
        rivit = rivi
        y = i
        for j, sarakkeet in enumerate(rivit):
            x = j
            haravasto.lisaa_piirrettava_ruutu(tila["kentta"][y][x], x * 40, y * 40)
    haravasto.piirra_ruudut()

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

turvalliset = []

def tulvataytto(planeetta, x, y):
    """
    Merkitsee planeetalla olevat tuntemattomat alueet turvalliseksi siten, että
    täyttö aloitetaan annetusta x, y -pisteestä.
    """
    if planeetta[y][x] == " ":
        turvalliset.append((x, y))
        korkeus = len(planeetta)
        leveys = len(planeetta[0])
        while len(turvalliset) > 0:
            x, y = turvalliset.pop()
            planeetta[y][x] = "0"
            if x == 0 and y == 0:
                for i, rivi in enumerate(planeetta[0:2]):
                    rivit = rivi
                    y_k = i
                    for j, ruutu in enumerate(rivit[0:2]):
                        x_k = j
                        if planeetta[y_k][x_k] == " ":
                            turvalliset.append((x_k, y_k))
                            #print(turvalliset)
            elif x == 0:
                for i, rivi in enumerate(planeetta[y - 1:y + 2], y - 1):
                    rivit = rivi
                    y_k = i
                    for j, ruutu in enumerate(rivit[0:2]):
                        x_k = j
                        if planeetta[y_k][x_k] == " ":
                            turvalliset.append((x_k, y_k))
                            #print(turvalliset)
            elif y == 0:
                for i, rivi in enumerate(planeetta[0:2]):
                    rivit = rivi
                    y_k = i
                    for j, ruutu in enumerate(rivit[x - 1:x + 2], x - 1):
                        x_k = j
                        if planeetta[y_k][x_k] == " ":
                            turvalliset.append((x_k, y_k))
                            #print(turvalliset)

            else:
                for i, rivi in enumerate(planeetta[y - 1:y + 2], y - 1):
                    rivit = rivi
                    y_k = i
                    for j, ruutu in enumerate(rivit[x - 1:x + 2], x - 1):
                        x_k = j
                        if planeetta[y_k][x_k] == " ":
                            turvalliset.append((x_k, y_k))
                            #print(turvalliset)

def main(planeetta):
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """

    leveys = len(planeetta[0]) * 40
    korkeus = len(planeetta) * 40
    haravasto.lataa_kuvat("/Users/lauraberg/Downloads/spritet")
    haravasto.luo_ikkuna(leveys, korkeus)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aloita()

if __name__ == "__main__":
    planeetta = [
    [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "],
    [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", "x", " "],
    [" ", "x", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x", " "],
    ["x", "x", "x", "x", "x", " ", " ", "x", " ", "x", " ", " ", " "],
    ["x", "x", "x", "x", " ", " ", " ", " ", "x", " ", "x", " ", " "],
    [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
    ]
    tila["kentta"] = planeetta
    tulvataytto(planeetta, 4, 0)
    main(planeetta)
