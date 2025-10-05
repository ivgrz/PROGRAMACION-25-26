"""
Escribir un programa que almacene nunha lista os
seguintes prezos, 50, 75, 46, 22, 80, 65, 8, e mostre por
pantalla o menor e o maior dos prezos.

precios.sort() #Ordena de menor a mayor
"""
def mymen():

    precios = [50, 75, 46, 22, 80, 65, 8]

    menor = min(precios)
    mayor = max(precios)



    print(menor,mayor)



mymen()