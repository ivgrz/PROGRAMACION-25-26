"""
Crea un algoritmo que cambie euros a dólares (O cambio pídese por teclado).
Codifica o programa, correspondente, para executar o programa co nome boletin2_3
"""
def cambio_euros_a_dolares():

    euros = float(input("introduce la cantidad de euros que vas a cambiar:"))

    cambio = 1.18

    dolares = euros * cambio

    print(f"{euros} euros son {dolares} dolares")

cambio_euros_a_dolares()