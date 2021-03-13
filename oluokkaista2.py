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

def laske_ninjat(x, y, huone_lista):
    korkeus = len(huone_lista)
    leveys = len(huone_lista[0])
    ninjojen_maara = 0
    if x == 0 and y == 0:
        for i, rivi in enumerate(huone_lista[0:2]):
            rivit = rivi
            y_k = i
            for j, ruutu in enumerate(rivit[0:2]):
                x_k = j
                if huone_lista[y_k][x_k] == 'N':
                    ninjojen_maara += 1
    elif x == 0:
        for i, rivi in enumerate(huone_lista[y - 1:y + 2], y - 1):
            rivit = rivi
            y_k = i
            for j, ruutu in enumerate(rivit[0:2]):
                x_k = j
                if huone_lista[y_k][x_k] == 'N':
                    ninjojen_maara += 1
    elif y == 0:
        for i, rivi in enumerate(huone_lista[0:2]):
            rivit = rivi
            y_k = i
            for j, ruutu in enumerate(rivit[x - 1:x + 2], x - 1):
                x_k = j
                if huone_lista[y_k][x_k] == 'N':
                    ninjojen_maara += 1

    else:
        for i, rivi in enumerate(huone_lista[y - 1:y + 2], y - 1):
            rivit = rivi
            y_k = i
            for j, ruutu in enumerate(rivit[x - 1:x + 2], x - 1):
                x_k = j
                if not sijainti_kentalla(x_k, y_k, leveys, korkeus) == "ulkona":
                    if huone_lista[y_k][x_k] == 'N':
                        ninjojen_maara += 1
    return ninjojen_maara

huone = [['N', ' ', ' ', ' ', ' '],
         ['N', 'N', 'N', 'N', ' '],
         ['N', ' ', 'N', ' ', ' '],
         ['N', 'N', 'N', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ']]

ninjat = laske_ninjat(1, 1, huone)
print(ninjat)
ninjat_1 = laske_ninjat(2, 1, huone)
print(ninjat_1)
ninjat_2 = laske_ninjat(4, 5, huone)
print(ninjat_2)
