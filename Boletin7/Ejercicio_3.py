"""
Invertir o texto: “Python para todos”
"""
def inversiontexto():
    print(f"PRIMERA FORMA")


    oracion = "Python para todos"
    oracioninvertida = oracion[::-1]
    print(oracioninvertida)

inversiontexto()

def inversiontexto2():
    print(f"SEGUNDA FORMA")

    texto = "python para todos"
    texto_invertido = "".join(reversed(texto))
    print(texto_invertido)


inversiontexto2()