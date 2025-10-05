"""
Escribir un programa que pregunte por unha mostra de
números, separados por comas, os garde nunha lista e mostre
por pantalla a súa media e desviación típica.
"""
import math



def numeros():

    numerosMD = []

    for i in range(10):
        while True:
            try:

                num = float(input(f"Dame el numero de posicion {i+1} (maximo 10): "))
                #Hay que poner un float antes del input para que no lo detecte como string, pasa mucho al usar for de esta manera
                if num in numerosMD:
                    print(f"Este numero ya fue ingresado, prueba otro")
                    continue #Vuelve a pedir

                numerosMD.append(num)
                break
            except ValueError:
                print(f"Debe ingresar un numero...")

    print(f"La lista de numeros es: ")
    print(" , ".join(map(str,numerosMD)))

    suma = sum(numerosMD)

    cantidad = len(numerosMD)

    promedio = suma/cantidad

    print(f"El promedio de estos numeros es: {promedio}")

    diferencias = []

    for x in numerosMD:
        diferencia = x - promedio
        diferencia_cuadrado = diferencia ** 2
        diferencias.append(diferencia_cuadrado)

    varianza = sum(diferencias) / len(numerosMD)

    desviacionT = math.sqrt(varianza)

    print(f"La desviacion tipica de estos numeros es: {desviacionT:.2f}")



numeros()

