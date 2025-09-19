"""
Dados 3 números que se supoñen distintos, indicar cal é o
maior
"""
def identificar_mayor():
    n1 = float(input(f"Introduce un numero:"))
    n2 = float(input(f"Introduce otro numero:"))
    n3 = float(input(f"Introduce otro numero mas:"))

    if n1 > n2 and n1>n3:
        print(f"El numero mayor es {n1}")
    elif n2 > n1 and n2>n3:
        print(f"El numero mayor es {n2}")
    else:
        print(f"El numero mayor es {n3}")
identificar_mayor()