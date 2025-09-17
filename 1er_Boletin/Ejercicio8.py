"""
Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, con espacios intermedios.
"""

def primeraforma():
    palabra = input("Ingrese una palabra:")
    print((palabra + " ") * 1000)

def segundaforma():
    palabra = input("Ingresa una palabra:")
    for i in range(1000):
        print(palabra, end=" ")
    print(f"\n")  # Salto de línea al final


# Extra: Imprimir la palabra con la primera letra en mayúsculay el resto en minúscula, dividida en dos partes.
def primMay_dividida():
    palabra = input("Ingrese una palabra:")
    # Convertir la primera letra a mayúscula y el resto a minúscula
    palabra = palabra.capitalize()
    #Dividir la palabra en dos partes
    mitad = len(palabra) // 2
    parte1 = palabra[:mitad]
    parte2 = palabra[mitad:]
    resultado = parte1 + " " + parte2
    # Imprimir las dos partes con un espacio intermedio

    for i in range (1000):
        print (resultado, end=" ")




if __name__ == "__main__":
    primeraforma()
    segundaforma()
    primMay_dividida()

