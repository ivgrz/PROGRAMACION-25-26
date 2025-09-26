"""
Escribir un programa que tome unha cantidade m de valores ingresados polo usuario, a
cada un lle calcule o factorial e imprima o resultado xunto co número de orden
correspondiente
"""
def factorial_():

    print(f"Ingresa varios numeros (maximo 10)")

    l = []
    for i in range(10):
        m = int(input(f"> "))
        l.append(m)
    for numero in l:
        factorial = 1
        for i in range(1, numero + 1):
            # El rango empieza en 1 y termina en numero + 1 para incluir el numero,
            # ya que el rango no incluye el último número,
            # porque es exclusivo de la función range, por eso se le suma 1, para que lo incluya
            factorial *= i # El operador *= es una forma abreviada de escribir factorial = factorial * i
        print(f"El factorial de {numero} es {factorial}") # Imprime el resultado

factorial_()