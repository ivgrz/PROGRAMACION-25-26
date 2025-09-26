"""
Escribir un programa que imprima tódolos números pares entre dous números que se
lle pidan o usuario
"""
import sys


def num_pares():
    lista = []
    print(f"Introduce 10 numeros")

    for i in range(10):
        num = int(input("> "))
        lista.append(num)

    pares = [num for num in lista if num % 2 == 0]
# num for num significa que por cada num en lista si num % 2 == 0 (es decir, si es par) lo añade a la nueva lista pares
    pares_ordenados = sorted(pares)
# sorted() ordena la lista de menor a mayor
    print(f"Los numeros pares de esta lista son: {pares_ordenados}")
num_pares()