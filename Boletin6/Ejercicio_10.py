"""
Escribir un programa que almacene as matrices
a = (1,2,3) b = (-1,0)
    (4,5,6)      (0,1)
                (1,1)
nunha lista e mostre por pantalla o seu produto.
Nota: Para representar matrices mediante listas usar listas
anidadas, representando cada vector fila nunha tupla

"""

def matrices():
    matriza = [(1,2,3), (4,5,6) ]

    matrizb = [ (-1,0), (0,1),(1,1)]

    print(matriza, matrizb)

    filaA = len(matriza)
    colA = len(matriza[0])
    filaB = len(matrizb)
    colB = len(matrizb[0])

    if colA != filaB: #Comprobamos que matematicamente las matrices se pueden multiplicar
        print(f"\n No se pueden multiplicar: Las columnas de A son diferentes de las filas de B")


    # Crea una "matriz" (lista de listas) llena de ceros, del tamaño filaA x colB.
    # - El bucle interior [0 for _ in range(colB)] crea una FILA con tantos ceros como columnas tenga la matriz B.
    #   Ejemplo: si colB = 3 → [0, 0, 0]
    # - El bucle exterior [... for _ in range(filaA)] repite esa fila tantas veces como filas tenga la matriz A.
    #   Ejemplo: si filaA = 2 → [[0, 0, 0], [0, 0, 0]]
    # En resumen: resultado será una lista de 'filaA' filas, cada una con 'colB' ceros.
    resultado = [[0 for _ in range(colB)] for _ in range(filaA)]

    print("\n Matriz resultado inicial: ")
    for fila in resultado:
        print(fila)

    print("\n Calculo: \n")

    for i in range(filaA):
        for j in range(colB):
            suma = 0
            for k in range(colA):
                a = matriza[i][k]
                b = matrizb[k][j]
                prod = a * b
                suma += prod
                print(f"A[{i}][{k}]({a}) * B[{k}][{j}]({b}) = {prod} -> suma = {suma}")
                resultado[i][j] = suma
                print(f"-> C[{i}][{j}] = {suma}\n")

    print("Matriz resultado del producto de A * B: ")
    for fila in resultado:
        print(fila)


matrices()
