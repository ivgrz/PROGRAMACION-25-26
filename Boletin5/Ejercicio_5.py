"""
Escribir un programa que reciba un número n por parámetro e imprima os primeiros n
números triangulares, xunto co seu índice. Os números triangulares obteñense
mediante a suma dos números naturales dende 1 ata n. É dicir, si se piden os primeros
5 números triangulares, o programa debe imprimir:
1 - 1
2 - 3
3 - 6
4 - 10
5 - 15

 facelo usando e sen usar a ecuación n ∗ (n + 1) / 2. Cal realiza máis operacións?

"""

def num_triangulares(n):
    lista_nt = []
    for i in range (1, n+1):
        nt = (i * (i + 1)) // 2
# La fórmula para calcular el número triangular en la posición i es (i * (i + 1)) / 2
        lista_nt.append((i, nt))
# El append sirve para añadir un elemento al final de la lista y usa lista_nt para referirse a la lista creada
# la tupla (i, nt) añade el índice y el número triangular a la lista

    for indice, valor in lista_nt:
            print(f"{indice} - {valor}")


num_triangulares(int(input("Introduce un número para ver los primeros números triangulares: ")))


def num_triangularessin_n(n):
    lista_t = []
    for i in range(1, n + 1):

# El rango empieza en 1 y termina en n + 1 para incluir n, ya que el rango no incluye el último número
# Tengo que incluir n porque si no, no se imprimirá el último número triangular

        if i == 1:
            nt = 1
        else:
            nt = lista_t[-1][1] + i # Accede al último número triangular calculado en la lista y le suma el índice actual i

# La fórmula para calcular el número triangular sin usar la ecuación es sumar el índice actual i
# al último número triangular calculado, que se encuentra en la última posición de la lista

        lista_t.append((i, nt))

    # Append añade la tupla (i, nt) a la lista, usamos una tupla y no una lista porque es más eficiente en estos casos
    # Si usara una lista, cada vez que se añade un elemento, se crea una nueva lista en memoria
    # y se copia el contenido de la lista original a la nueva lista, lo que es menos eficiente
    # En cambio, una tupla es inmutable

    for indice, valor in lista_t:
            print(f"{indice} - {valor}")



num_triangularessin_n(int(input("Introduce un número para ver los primeros números triangulares sin usar la ecuación: ")))

# Llama a la función num_triangularessin_n y le pasa el número introducido por el usuario como argumento
# se coloca aqui para que se ejecute después de definir la función
# y no antes, ya que si se coloca antes, dará error porque la función no estará definida aún

