"""
Escribir un programa que pregunte o usuario os números
gañadores da lotería primitiva, os almacene nunha lista e
os muestre por pantalla ordenados de menor a maior
"""
def loteria():

    numerosl = []

    for i in range(6):
        num = input(f"Dame el  numero ganador {i + 1}:")
        numerosl.append(num)

    numerosl.sort() #Ordenamos la lista de menor a mayor

    print(f"\n Los numeros de la loteria de menor a mayor son: ")
    print(numerosl)

loteria()