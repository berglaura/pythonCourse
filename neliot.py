from turtle import *

def piirra_nelio(sivu, x, y):
    if x < 0:
        up()
        setx(x)
        sety(y)
        down()
        color("red")
        begin_fill()
        forward(sivu)
        right(90)
        forward(sivu)
        right(90)
        forward(sivu)
        right(90)
        forward(sivu)
        end_fill()

    else:
        up()
        setx(x)
        sety(y)
        down()
        color("blue")
        begin_fill()
        forward(sivu)
        right(90)
        forward(sivu)
        right(90)
        forward(sivu)
        right(90)
        forward(sivu)
        end_fill()

    # tähän funktio joka piirtää neliön
    # joko punaisena tai sinisenä riippuen
    # siitä onko aloituspisteen x-koordinaatti
    # positiivinen (sininen) vai negativiinen
    # (punainen)

piirra_nelio(40, -100, 100)
piirra_nelio(60, 100, -100)
piirra_nelio(100, -50, -20)
piirra_nelio(80, 90, 30)
done()
