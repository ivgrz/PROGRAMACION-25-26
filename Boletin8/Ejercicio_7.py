"""
Dada unha lista de números enteiros e un enteiro k, escribir unha función
que:
● Devolte tres listas, unha cos menores, outra cos maiores e outra cos
iguais a k.
● Devolte unha lista con aqueles que son múltiplos de k.
"""
def separar_numeros(lista, k):
    menores = []
    mayores = []
    iguales = []
    multiplos = []

    for numero in lista:
        if numero < k:
            menores.append(numero)
        elif numero > k:
            mayores.append(numero)
        elif numero == k:
            iguales.append(numero)
        if k != 0 and numero % k == 0:
            multiplos.append(numero)
        
    return menores, mayores, iguales, multiplos
lista_numeros = [3, 5, 7, 10, 15, 20, 25, 30, 35, 40, 45, 50]
k = 10

menores_k, mayores_k, iguales_k, multiplos_k = separar_numeros(lista_numeros, k)

print(f"--- Análisis de la Lista con K = {k} ---")
print(f"Lista Original: {lista_numeros}")


print(f"1. Números Menores que {k}:")
print(menores_k)

print(f"\n2. Números Mayores que {k}:")
print(mayores_k)

print(f"\n3. Números Iguales a {k}:")
print(iguales_k)

print(f"\n4. Múltiplos de {k}:")
print(multiplos_k)