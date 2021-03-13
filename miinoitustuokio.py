import random
import haravasto

tila = {
    "kentta": []
}

def miinoita(kentta, vapaat_ruudut, miinojen_lkm):
    """
    Asettaa kentälle N kpl miinoja satunnaisiin paikkoihin.
    """
    viela_vapaat_ruudut = vapaat_ruudut
    pituus = len(viela_vapaat_ruudut)
    i = 0
    while i < miinojen_lkm:
        indeksi = random.randint(0, (pituus - 1))
        x, y = vapaat_ruudut[indeksi]
        kentta[y][x] = "x"
        viela_vapaat_ruudut.remove(vapaat_ruudut[indeksi])
        pituus = pituus - 1
        i += 1

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

def main():
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """

    haravasto.lataa_kuvat("/Users/lauraberg/Downloads/spritet")
    haravasto.luo_ikkuna(600, 400)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aloita()

if __name__ == "__main__":
    kentta = []
    for rivi in range(10):
        kentta.append([])
        for sarake in range(15):
            kentta[-1].append(" ")

    tila["kentta"] = kentta

    jaljella = []
    for x in range(15):
        for y in range(10):
            jaljella.append((x, y))

    miinoita(tila["kentta"], jaljella, 35)
    main()
