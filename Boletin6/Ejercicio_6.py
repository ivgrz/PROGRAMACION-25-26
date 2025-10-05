"""
Escribir un programa que pida o usuario unha palabra e
mostre por pantalla si é un palíndromo.
"""

def palindromo():

    palabras = []

    palabra = input(f"Escribe una palabra: ")
    palabras.append(palabra)
    palabra = palabra.lower()
    invertida = palabra[:: -1] #Invierte la cadena de strings

    if invertida == palabra:
        print(f"La palabra es palindromo")
    else:
        print(f"No es palindromo")



palindromo()