"""
Escribir un programa que imprima todos los números pares entre dos números que se
le pidan al usuario
"""

def num_pares():
    # Pedimos dos números al usuario
    print("Introduce el primer número:")
    num1 = int(input("> "))
    print("Introduce el segundo número:")
    num2 = int(input("> "))

    # Determinamos el menor y el mayor para recorrer correctamente el rango
    inicio = min(num1, num2)
    fin = max(num1, num2)

    # Generamos la lista de todos los números con el rango especificado
    numeros = list(range(inicio, fin + 1))
    # Filtramos solo los números pares
    pares = []
    for x in numeros:
        if x % 2 == 0:
            pares.append(x)

    # Mostramos el resultado
    print(f"Los números pares entre {inicio} y {fin} son: {pares}")

num_pares()