"""
Un almacén clasifica os seus produtos segundo a seguinte táboa de
vendas anuais:
Vendas anuais Artigo de consumo
< = 100 produtos baixo
>100 e < = 500 medio
> 500 e < = 1000 alto
> 1000 primeira necesidade
Coñecido o nome do artigo e as vendas anuais. Indicar de que tipo é.
"""

def almacen():
    nomart = input("Nome del articulo:")
    ventas = int(input("Ventas anuales:"))
    if ventas <= 100:
        print(f"{nomart} es un producto bajo :( ")
    if 100 < ventas <= 500:
        print(f"{nomart} es un producto medio -_-")
    if 500 < ventas <= 1000:
        print(f"{nomart} es un producto con alta demanda")
    if ventas > 1000:
        print(f"{nomart} es un producto de primera necesidad")
almacen()