"""
Dada unha lista de números enteiros, escribir unha función que:
● Devolte unha lista con tódolos que sexan primos.
● Devolte o sumatorio e o promedio dos valores.
● Devolte unha lista co factorial de cada un de eses números.
"""
import math


def numeros_primos(numeros):

    primos = []

    for i in numeros:

        es_primo = True

        if i <= 1:
            es_primo = False
        elif i == 2:
            es_primo = True
        elif i % 2 == 0:
            es_primo = False

        else:
            limite = int(math.sqrt(i)) # Calculamos la raíz cuadrada del número
            for j in range(3, limite + 1, 2): # Usamos un rango que vaya desde 3 hasta la raíz cuadrada del número, incrementando de 2 en 2 (solo números impares)
                if i % j == 0:
                    es_primo = False
                    break
        if es_primo:
            primos.append(i)
    return primos


def sumatorio_promedio(numeros):

    sumatorio = sum(numeros)
    promedio = sumatorio / len(numeros)

    return sumatorio, promedio

def factorial_numeros(numeros):

    factoriales = []

    for i in numeros:
        factoriales.append(math.factorial(i))
    return factoriales

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# REFRENCIA: Calculamos todo unha vez para no ter que recalcular cada vez que se chama ao menú

primos = numeros_primos(lista_numeros)
sumatorio, promedio = sumatorio_promedio(lista_numeros)
factoriales = factorial_numeros(primos)

def menu():
    print("Menú de opcións:")
    print("1. Mostrar números primos")
    print("2. Mostrar sumatorio e promedio")
    print("3. Mostrar factoriales")
    print("4. Saír")

    while True:
        opcion = input("Seleccione unha opción (1-4): ")

        if opcion == '1':
            print(f"Lista original: {lista_numeros}")
            print(f"Números primos: {primos}")
        elif opcion == '2':
            print(f"Lista original: {lista_numeros}")
            print(f"Sumatorio: {sumatorio}, Promedio: {promedio}")
        elif opcion == '3':
            print(f"Lista referencia: {primos}")
            print(f"Factoriais dos primos: {factoriales}")
        elif opcion == '4':
            print("Saíndo do programa...")
            break
        else:
            print("Opción non válida, por favor intente de novo.")

menu()
