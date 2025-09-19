"""
Escribe un programa que solicite o usuario un número comprendido
entre 1 e 99. O programa ten que mostralo con letras, por exemplo, para
o 56, mostrará: “Cincuenta e seis”.
"""

def num_letras():
# Listas con decenas, unidades y numeros especiales
    unidades = [" ", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = [" ", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    especiales = ["once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve"]
# Solicitar numero
    n = int(input("Escribe un numero ente el 1 y el 99:"))
# Rangos de operacion
    if 1 <= n <= 9:
# Imprimir unidades de 1 a 9, la posicion 0 es un espacio en blanco y la n indica que numero es
        print(unidades[n])
# Imprimir numeros especiales del 11 al 19, la posicion 0 es un espacio en blanco y la n-11 indica que numero es
    elif 10 <= n <= 19:
        if n == 10:
            print(decenas[1])
        else:
# n-11 indica la posicion del numero especial en la lista
            print(especiales[n - 11])
    elif 20 <= n <= 99:
# d es la posicion de la decena y u la posicion de la unidad
        d = n // 10
        u = n % 10
# Si la unidad es 0, solo imprime la decena, si no, imprime decena y unidad
        if u == 0:
            print(decenas[d])
        else:
            print(f"{decenas[d]} y {unidades[u]}")
    else:
        print("Numero fuera de rango")
num_letras()