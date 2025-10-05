"""
Transforma a cadea de texto “ Phytoneros” a maiúsculas. Garda o valor
na variable e posteriormente convértea novamente a minúsculas.
"""

def mayusymin():

    cadena_texto = " Phytoneros"
    cadena_texto_sine = cadena_texto.replace(" ","")
    cadena_textoM = cadena_texto_sine.upper()
    print(f"En mayusculas: {cadena_textoM}")
    cadena_texto = cadena_textoM
    print(f"La cadena reemplazada: {cadena_texto}")

    print(f"En minusculas: {cadena_texto.lower()}")







mayusymin()