"""
Escribir unha función que indique si duas fichas de dominó encaixan ou non.
As fichas son recibidas en duas tuplas, por exemplo: (3,4) e (5,4). A función
devolta un booleano co resultado do encaixe.
"""

def encaje(ficha1, ficha2):


    if ficha1[0] in ficha2 or ficha1 [1] in ficha2:
        print(f"Las fichas {ficha1} y {ficha2} encajan")
        verificacion = True
    else:
        print(f"Las fichas {ficha1} y {ficha2} no encajan")
        verificacion = False

    return verificacion

print(encaje((3,4), (5,4)))
print(encaje((1,2), (5,4)))
print(encaje((6,2), (2,4)))
print(encaje((0,0), (0,4)))
print(encaje((1,1), (5,5)))

