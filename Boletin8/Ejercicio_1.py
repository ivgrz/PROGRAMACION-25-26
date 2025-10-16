"""
Escribir unha función que reciba unha tupla de elementos e indique si se
encontran ordeados de menor a maior ou non.
"""
def maiorymenor(*tnum):

    verificacion = False


    if tnum == tuple(sorted(tnum)): # Comprobamos si la tupla esta ordenada de menor a mayor, eso lo indica el sorted
            print(f"La tupla {tnum} esta ordenada de menor a mayor")
            verificacion = True
    else:
        print(f"La tupla {tnum} no esta ordenada de menor a mayor")


    return verificacion

# Para colocar ejemplos de uso con un print es recomendable pasar la tupla por parametro usando un *tupla

print(maiorymenor(1,2,3,4,5))
print(maiorymenor(5,4,3,2,1))