"""
Escribir un programa que pida o usuario unha palabra e
mostre por pantalla o número de veces que conten cada
vogal.
"""

def numvocal():

    vocales = ["a","e","i","o","u"]
    palabra = input(f"Escribe una palabra: ")
    lista_caracteres = list(palabra)

    for vocal in vocales:
        cantidad = lista_caracteres.count(vocal) #Cuenta las vocales de la palabra guardada en la lista usando COUNT
        print(f"La vocal {vocal} aparece {cantidad} veces")

numvocal()