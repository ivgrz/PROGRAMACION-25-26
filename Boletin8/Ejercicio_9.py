"""
Escribir una función empaquetar para una lista,
donde empaquetar significa indicar la repetición de valores consecutivos mediante una tupla
 (valor, cantidad de repeticiones). Por ejemplo, empaquetar [1, 1, 1, 3, 5, 1, 1, 3, 3]
 debe devolver [(1, 3), (3, 1), (5, 1), (1, 2), (3, 2)].
"""

def empaquetar(lista):
    if not lista:
        return []

    lista_e = []

    valor_actual = lista[0]
    contador = 1

    for i in range(1, len(lista)): # Empezar desde el segundo elemento para comparar con el primero
        if lista[i] == valor_actual:
            contador += 1  # Incrementar el contador si el valor es igual al actual
        else:
            lista_e.append((valor_actual, contador)) # Añadir la tupla (valor, contador) a la lista empaquetada
            valor_actual = lista[i] # Actualizar el valor actual
            contador = 1 # Reiniciar el contador
    lista_e.append((valor_actual, contador))  # Añadir el último valor y su contador
    return lista_e

# --- Ejemplos de uso ---

lista_ejemplo = [1, 1, 1, 3, 5, 1, 1, 3, 3]
resultado = empaquetar(lista_ejemplo)

print(f"Lista original: {lista_ejemplo}")
print(f"Lista empaquetada: {resultado}")

# Ejemplo de una lista sin repeticiones consecutivas
lista_simple = [1, 2, 3, 4]
print(f"\nLista original: {lista_simple}")
print(f"Lista empaquetada: {empaquetar(lista_simple)}")

# Ejemplo con repeticiones al final
lista_final = [4, 4, 2, 2, 2]
print(f"\nLista original: {lista_final}")
print(f"Lista empaquetada: {empaquetar(lista_final)}")


