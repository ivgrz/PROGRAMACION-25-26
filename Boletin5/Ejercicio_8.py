"""
Modificar o programa anterior para que poida xerar fichas dun xogo que pode ter números
de 0 a n.
"""
def fichas_domino2(n): # Siempre incluir n por parametro en programas que necesiten un rango definido
    for i in range (n + 1): # El rango empieza en 0 y termina en n + 1 para incluir n (el número máximo)
        for j in range (i, n + 1): # El rango empieza en i y termina en n + 1 para incluir n
            print(f"[{i}|{j}]") # Imprime la ficha de domino en el formato [i|j]
fichas_domino2(int(input("Introduce el número máximo para las fichas de dominó: ")))
# Llama a la función fichas_domino2 y le pasa el número introducido por el usuario como argumento
# se coloca aqui para que se ejecute después de definir la función

"""
Basicamente este programa genera todas las combinaciones
posibles de fichas de dominó pasandole un numero n (escrito por usuario)
como parametro, donde n es el número máximo en las fichas.
"""