"""
Määrittelee aasigotchin käyttöliittymän toiminnot.
"""


def nayta_tila(aasidata):
    """
    Tulostaa aasin tilan.
    """
    print("Aasi on ", aasidata["IKÄ"], " vuotta vanha ja rahaa on ", aasidata["RAHA"], " mk.")
    print("Kylläisyys: ", aasidata["KYLLÄISYYS"])
    print("Onnellisuus: ", aasidata["ONNELLISUUS"])
    print("Jaksaminen: ", aasidata["JAKSAMINEN"])
    if aasidata["ELÄKE"] == True:
        print("Aasi on jäänyt eläkkeelle.")

def pyyda_syote(aasidata):
    """
    Näyttää käyttäjälle aasin tilaa vastaavat mahdolliset syötteet ja kysyy uutta
    syötettä kunnes käyttäjä antaa laillisen syötteen. Saatu syöte palautetaan.
    """
    if aasidata["ELÄKE"] == False:
        print("Valinnat: q, r, k, t")
        syote = input("Anna seuraava valinta: ")
        while syote not in ('q', 'r', 'k', 't'):
            print("Virheellinen syöte!")
            syote = input("Anna seuraava valinta: ")
        return syote
    else:
        print("Valinnat: q, a")
        syote = input("Anna seuraava valinta: ")
        while syote not in ('q', 'a'):
            print("Virheellinen syöte!")
            syote = input("Anna seuraava valinta: ")
        return syote
