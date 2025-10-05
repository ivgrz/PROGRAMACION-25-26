"""
Sobre a cadea de texto “ Jeve jeve jeve”, substitúe todas as vocais e
pola vogal para dando como resultado “java java java”.
"""

def reemplazar_vocal():

    cadena_texto = " Jeve jeve jeve"

    cadena_texto_corregida = cadena_texto.replace("e","a")

    print(f"La antigua cadena era: {cadena_texto}")
    print(f"La nueva cadena es: {cadena_texto_corregida}")


reemplazar_vocal()