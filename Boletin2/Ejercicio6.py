"""
Deseña un programa para o software dunha máquina, que converta una cantidade
enteira de diñeiro, que está presentada en billetes de 100, 20, 5 e moedas de 1 €, no
seu equivalente en euros. Por exemplo 2 billetes de 100€, 3 billetes de 20 €, 6
moedas de 1€ visualizaríamos 266 € ).
"""

def mostrar_euros():
    billetes_c = int(input(f"Introduce la cantidad de billetes de $100: "))
    billetes_v = int(input(f"Introduce la cantidad de billetes de $20: "))
    billetes_cin = int(input(f"Introduce la cantidad de billetes de 5: "))
    mon_uno = int(input(f"Introduce la cantidad de monedas de uno: "))

    billetescien = (billetes_c*100)
    billetesv = (billetes_v * 20)
    billetescin = (billetes_cin * 5)
    monuno = (mon_uno * 1)

    resultado = billetescien + billetesv + billetescin + monuno
    print(f"La cantidad de euros que tienes es: {resultado} €")

mostrar_euros()