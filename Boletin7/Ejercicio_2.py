"""
Desmenuza o String “Python” mostrándoo por pantalla carácter a
carácter.
"""
def stringp():

    palabra = "Python"

    lista_caracteres = list(palabra)

    print(f"Mostrando caracter por caracter... ")
    print(lista_caracteres)

    print(f"Uno por uno... ")
    for i in palabra:
        print(i)

stringp()