"""
Realiza un algoritmo e codifica o programa correspondente que lea, dende o teclado,
unha cantidade enteira en euros e amose, por pantalla, o seu desglose en billetes
de 100, 20, 5 e moedas de 1 €.
"""

def separacion_euros():

    euros = int(input(f"Introduce los euros que tienes:"))
# separamos la cantidad de billetes que hay y usamos el resto para saber la cantidad de euros que quedan de la division

    billetes_c = euros // 100
    euros = euros % 100
    billetes_v = euros // 20
    euros = euros % 20
    billetes_5 = euros // 5
    euros = euros % 5
    monedas_1 = euros // 1
    euros = euros % 1
# Mostramos el resultado de la separacion por pantalla
    print(f"Separacion de billetes y monedas:")
    print(f"Billetes de 100: {billetes_c}")
    print(f"Billetes de 20: {billetes_v}")
    print(f"Billetes de 5: {billetes_5}")
    print(f"Monedas de 1: {monedas_1}")
separacion_euros()

