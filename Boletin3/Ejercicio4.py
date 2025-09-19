"""
Coñecidos, o nome e o peso de dúas persoas, o programa
escribirá por consola os datos da persoa que pesa máis e a
diferenza de peso entre elas.

"""

def calc_pesos():

    nom1 = input(f"Introduce el nombre de la persona 1:")
    nom2 = input(f"Introduce el nombre de la persona 2:")
    peso1 = float(input(f"Introduce el peso de {nom1}:"))
    peso2 = float(input(f"Introduce el peso de {nom2}:"))

    if peso1 > peso2:
        print(f"{nom1} pesa mas que {nom2} y la diferencia entre ellos es de {peso1 - peso2} kg")
    elif peso2 > peso1:
        print(f"{nom2} pesa mas que {nom1} y la diferencia entre ellos es de {peso2 - peso1} kg")
    else:
        print(f"{nom1} y {nom2} pesan igual")
        
calc_pesos()