import haravasto

hiiri = {
    haravasto.HIIRI_VASEN: "vasen",
    haravasto.HIIRI_KESKI: "keski",
    haravasto.HIIRI_OIKEA: "oikea"
}

def kasittele_hiiri(x, y, hiiren_painike, muokkausnapit):
    """
    Tätä funktiota kutsutaan kun käyttäjä klikkaa sovellusikkunaa hiirellä.
    Tulostaa hiiren sijainnin sekä painetun napin terminaaliin.
    """
    print("Hiiren nappia ", hiiri[hiiren_painike], " painettiin kohdassa ", x, ", ", y)

def main():
    """
    Luo sovellusikkunan ja asettaa käsittelijäfunktion hiiren klikkauksille.
    Käynnistää sovelluksen.
    """
    haravasto.luo_ikkuna(leveys=800, korkeus=600, taustavari=(240, 240, 240, 255))
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()


if __name__ == "__main__":
    main()
