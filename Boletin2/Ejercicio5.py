"""
Escribe un programa que lea o valor dunha distancia en millas mariñas e a pase a
metros ( 1 milla mariña = 1852 m ).
Codifica o programa correspondente para executar o programa
"""
def millas_metros():

    millas = float(input(f"Introduce la cantidad de millas:"))

    factor_conversion = 1852

    metros = millas * factor_conversion

    print(f"{millas} millas son {metros} metros")

millas_metros()