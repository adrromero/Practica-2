"""Amb el teu company, clona un mateix repositori per treballar de manera conjunta:

    Afegeix a l'alumne 2 com a col·laborador al teu projecte
    Crear un fitxer de python que mostri un menú de selecció amb 3 opcions:

    1-Introdueix una frase
    2-Elimina les vocals
    3-Elimina les consonants
    4-Ordena la frase al revés i printala per pantalla
    5-Ordena les paraules de la frase en orde ascendent i printales per pantalla
    6-Des d'aquest moment, pugeu els canvis al repositori.
    7-L'alumne 1 treballarà en una branca nova anomenada “vocals” i desenvoluparà les funcions 1, 2 i 4.
    8-L'alumne 2 treballarà en una branca nova anomenada “consonants” i desenvoluparà les funcions 3 i 5.
    9-El projecte final haurà de fer funcionar tot conjuntament
    10-Afegeix un fitxer Readme.md el més personalitzat possible.

    Mínim 3 commits per usuari.

Fes un petit tutorial en PDF amb captures de què has fet i com justificant tot. (1 per parella).

Adjunta al tutorial la URL del repositori."""


def sinVocales(f):
    vocales = ("a", "e", "i", "o", "u")
    for letra in vocales:
        f = f.replace(letra, "")
    return f


frase = input("Dame una frase: ")

print(sinVocales(frase.lower()))

frase = frase[::-1]
print(frase)
