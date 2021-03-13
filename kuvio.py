import math

def laske_nelio_ala(sivun_pituus):
    return sivun_pituus ** 2

def laske_sektorin_ala(sade, sisakulma):
    return (sisakulma / 360) * math.pi * sade ** 2

def laske_sivun_pituus(hypotenuusa):
    return hypotenuusa / math.sqrt(2)

def laske_kuvion_ala(x):
    nelio = laske_nelio_ala(x)
    kolmion_sivu = laske_sivun_pituus(x)
    kolmion_ala = (kolmion_sivu ** 2) / 2
    pienen_ympyran_ala = math.pi * (kolmion_sivu ** 2)
    iso_nelio = (kolmion_sivu * 2) ** 2
    ison_ympyran_ala = math.pi * (kolmion_sivu * 2) ** 2
    return (nelio + kolmion_ala + pienen_ympyran_ala * (1 / 8)
        + iso_nelio + ison_ympyran_ala * (3 / 4))


    # tämän funktion sisällä kutsumalla
    # aiempia funktioita välituloksia varten

x = float(input("Anna x: "))
koko_ala = laske_kuvion_ala(x)
print("Kuvion ala: ", round(koko_ala, 4))
# kutsuu laskufunktiota ja tulostaa alan
# pyöristettynä
