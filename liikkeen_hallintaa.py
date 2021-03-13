import math

def muunna_xy_koordinaateiksi(kulma, vektorin_pituus):
    return(int(round(vektorin_pituus * math.cos(kulma), 0)),
    int(round(vektorin_pituus * math.sin(kulma), 0)))

def kysy_liike(hahmo):
    hahmo["suunta"] = float(input("Anna liikkumissuunta asteina: "))
    hahmo["nopeus"] = float(input("Anna liikenopeus: "))

def paivita_sijainti(hahmo):
    suunta_radiaaneina = math.radians(hahmo["suunta"])
    x, y = muunna_xy_koordinaateiksi(suunta_radiaaneina, hahmo["nopeus"])
    hahmo["x"] = hahmo["x"] + x
    hahmo["y"] = hahmo["y"] + y

hahmo_1 = {
    "x": 0,
    "y": 0,
    "suunta": 0,
    "nopeus": 0
}

hahmo_2 = {
    "x": 50,
    "y": 50,
    "suunta": 0,
    "nopeus": 0
}

print("Pelaajan 1 vuoro")
print("Hahmo on sijainnissa (", hahmo_1["x"], ",", hahmo_1["y"], ")")
kysy_liike(hahmo_1)
paivita_sijainti(hahmo_1)
print("Uusi sijainti: (", hahmo_1["x"], ",", hahmo_1["y"], ")")
print("Pelaajan 2 vuoro")
print("Hahmo on sijainnissa (", hahmo_2["x"], ",", hahmo_2["y"], ")")
kysy_liike(hahmo_2)
paivita_sijainti(hahmo_2)
print("Uusi sijainti: (", hahmo_2["x"], ",", hahmo_2["y"], ")")
