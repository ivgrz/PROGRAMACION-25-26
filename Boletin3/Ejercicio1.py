"""
Codifica un programa que solicite un número por teclado e
que saque un mensaxe que diga “É un número positivo”,
sempre que cumpra esa condición.
"""

def mostrar_posit():
    numero = float(input("introduce un numero:"))

    if numero > 0:
        print(f"El numero {numero} es positivo")
    else:
        print(f"Solo acepto positivos bro")

mostrar_posit()