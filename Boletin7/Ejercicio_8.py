"""
Compara se o String “Python” é igual que o String “ JavaScript”.
"""

def compara_cadenas():
    cadena_texto1 = "Python"
    cadena_texto2 = " JavaScript"

    cadena_texto2_sine = cadena_texto2.replace(" ", "")

    for i in cadena_texto1:
        if i == cadena_texto2_sine:
            print(f"Las cadenas son iguales")
        else:
            print(f"Las cadenas son diferentes")
        break





compara_cadenas()