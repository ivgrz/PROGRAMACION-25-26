"""
Escribir un programa que imprima por pantalla tódalas fichas de dominó, de unha por liña e
sen repetir.
"""
def fichas_domino():
    for i in range(7): #El rango empieza en 0 y termina en 7 para incluir el 6
        for j in range (i,7): # El rango empieza en i y termina en 7 para incluir el 6
            print(f"[{i}|{j}]") # Imprime la ficha de domino en el formato [i|j]
fichas_domino()
# El primer bucle for itera sobre los valores de i desde 0 hasta 6
# El segundo bucle for itera sobre los valores de j desde i hasta 6
# Esto asegura que no se repitan las fichas, ya que j siempre es mayor o igual a i
# La impresión de la ficha se hace en el formato [i|j]
