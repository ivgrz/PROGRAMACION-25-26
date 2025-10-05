"""
Elimina os espazos do texto: “Guido Van Rossum creou Python”
"""

def eliminaespacios():

    texto = "Guido Van Rossum creo Python"

    texto_sin_espacios = texto.replace(" ","")

    print(texto_sin_espacios)


eliminaespacios()