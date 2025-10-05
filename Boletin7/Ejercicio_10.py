"""
Tenta escribir un método, que dado un obxecto da clase str conte
diferentes tipos de caracteres. En particular, o método deberá imprimir
o número de letras, díxitos e espazos en branco da cadea. Tenta facer
un programa que escriba o cálculo da cadea: «Ola, son alumno de
DAM1, e son programador desde o 2025».
"""

def conta_caracteres():

    vocales = ["a","e","i","o","u"]
    cantvocal = 0
    digitos = 0


    cadena_texto = f"Hola, soy un alumno de DAM1, y soy programador desde el 2025"
    cadena_texto_min = cadena_texto.lower()
    espacios = cadena_texto_min.count(" ")
    for i in cadena_texto_min:
        if i in vocales:
            cantvocal += 1
        elif i.isdigit():
            digitos += 1
    print(f"La cantidad de vocales son {cantvocal} y la cantidad de digitos son {digitos} "
          f"y hay {espacios} espacios en blanco")






conta_caracteres()