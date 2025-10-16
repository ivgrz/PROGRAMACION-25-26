"""
Escribir unha función que reciba unha tupla con nomes e para cada nome
imprima unha mensaxe ‘Estimado don/dona Nome’
"""
def estimar_nombres(nombres):
    for nombre in nombres: # Usamos un bucle para recorrer cada nombre de la tupla
        print(f"Estimado don/doña {nombre}")

# Ejemplos de uso

print(estimar_nombres(("Ana","Luis","María","Pedro")))