"""
Escribir unha función que reciba unha lista de tuplas (Apelido, Nome,
Inicial_segundo_nome) e devolte unha lista de cadenas onde cada unha
conteña primero o nome, logo a inicial cun punto, e logo o apelido.
"""
def formato_nombres(lista_tuplas):
    lista_formateada = []

    for apellido, nombre, inicial in lista_tuplas:
        cadena_f = f"{nombre} {inicial} {apellido}" # Formatear la cadena según el requisito
        lista_formateada.append(cadena_f) # Rellenar la lista con la cadena formateada

    return lista_formateada

# Exemplo de uso
tuplas = [("González", "Ana", "M."), ("López", "Juan", "P."), ("Martínez", "Lucía", "A.")]

nombres_formateados = formato_nombres(tuplas)
print(nombres_formateados)