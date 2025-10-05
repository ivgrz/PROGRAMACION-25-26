"""
Escribir un programa que almacene o abecedario nunha
lista, e cree outra lista a partir dela, onde non aparezan as
letras que ocupen posicións múltiplos de 3, e mostre por
pantalla a lista resultante.
"""
import string


def abc():

    labc = list(string.ascii_lowercase)

    labc.insert(14, "ñ")



    # 2) MOSTRAR ÍNDICES Y LETRAS


    for i, letra in enumerate(labc, start=1):
        print(i,"->", letra)

    # 3) SELECCIONAR LETRAS QUE NO ESTÁN EN POSICIONES MÚLTIPLOS DE 3

    letrasf = []

    for i, letra in enumerate(labc, start=1):
        if i%3 == 0:
            letrasf.append(letra)
    print("\n Resultado de lista: ")
    print(letrasf)

abc()
