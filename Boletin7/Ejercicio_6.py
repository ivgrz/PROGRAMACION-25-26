"""
Divide a cadea de texto “ www. phytonparatodos. com” en duas partes “
www. phyton” e “paratodos. com”. Para posteriormente concaténalas e
mostralas de novo.
"""

def texto_partido():

    cadena_texto= " www. phytonparatodos. com"

    cadena_texto_sin_espacios = cadena_texto.replace(" ","")
    cadenaf = cadena_texto_sin_espacios.lower()

    primera_parte = cadenaf[:10] #Caracteres antes del indice 11
    segunda_parte = cadenaf[10:] # Caracteres despues del indice 11 incluyendolo

    texto_final = primera_parte + segunda_parte

    print(f"Concatenamos {primera_parte}")
    print(f"Con {segunda_parte}")
    print(f"Obtenemos {primera_parte} + {segunda_parte} = {texto_final}")



texto_partido()