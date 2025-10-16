"""
Pregado de un texto. Escribir unha función que reciba un texto e unha
lonxitude e devolva unha lista de cadeas de como máximo esa lonxitude. As
líñas deben cortarse correctamente nos espazos (sen cortar as palabras).
"""

def texto_pegado():
    texto = input("Introduce un texto: ")
    texto = texto.strip()
    try:
        longitud = int(input("Introduce una longitud: "))
    except ValueError:
        print("Error: La longitud debe ser un número entero.")
        return []
    lista_lineas = []
    while len(texto) > longitud:
        fragmento = texto[:longitud]
        indice_corte = fragmento.rfind(" ")
        if indice_corte == -1:
            indice_corte = longitud
        linea_actual = texto[:indice_corte]
        lista_lineas.append(linea_actual)
        texto = texto[indice_corte:].strip()
    if texto:
        lista_lineas.append(texto)
    return lista_lineas

resultado = texto_pegado()
print("\n--- Resultado del Plegado ---")
for linea in resultado:
    print(linea)
