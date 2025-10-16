"""
Escribir unha función que reciba unha tupla con nomes, unha posición de
orixen p e unha cantidade n, e imprima a mensaxe anterior (exercicio 3) para
os n nombres que se encontran a partires da posición p.
"""
def estimar_nombres_parciales(nombres, p, n):

    slice = p + n

    nombres_s = nombres[p:slice]
# Los [] indican que estamos haciendo un corte (slice) de la tupla nombres desde la posición p hasta la posición slice (no inclusiva)
    if not nombres_s:
        print(f"Nombre fuera de rango, intente de nuevo")

# Verificacion para que funcione de manera logica


    for nombre in nombres_s:
        print(f"Estimado don/doña {nombre}")
        verificacion = True
    return verificacion

t_nombres = ("Ana", "Pedro", "Juan", "Thiago", "Joaquin", "Edgar", "Paco", "Susana")



print(estimar_nombres_parciales(t_nombres,2,6))
