ELAIMET = {
    "a": "aasi",
    "k": "koira",
    "@": "kissa",
    "h": "hemuli",
    "l": "lammas"
}

def tutki_ruutu(merkki, rivi, sarake):
    y = rivi
    x = sarake
    for i in ELAIMET:
        if i == merkki:
            print("Ruudusta ({}, {}) löytyy {}".format(x, y, ELAIMET[merkki]))

def tutki_kentta(KENTTA):
    for i, rivi in enumerate(KENTTA):
        rivit = rivi
        y = i
        for j, sarakkeet in enumerate(rivit):
            x = j
            tutki_ruutu(KENTTA[i][j], y, x)
