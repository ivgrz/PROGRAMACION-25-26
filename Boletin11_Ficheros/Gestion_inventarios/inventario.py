"""
Realizar un programa para a xestión de Inventario. O programa ten que
facer as seguintes operacións sobre un ficheiro CSV:
●
Calculo do valor total do inventario: Dado un ficheiro produtos.csv (con
columnas: id, nome, prezo, stock), o programa ten realizar o cálculo (prezo ×
stock).
●
Existencias baixas: Crea un novo ficheiro baixo_stock.csv que conteña
só os produtos cun número de existencias inferior a 5 unidades.


"""
import csv


class Gestion_inventario:
    def calculo_valor_total(self):
        valor_total = 0
        with open("produtos.csv", "r") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                precio = float(fila['prezo'])
                stock = int(fila['stock'])
                valor_total += precio * stock
        return valor_total

    def bajo_stock(self):
        with open("produtos.csv", "r") as f1:
            with open("bajo_stock.csv", "w", newline='') as f2:
                reader = csv.DictReader(f1)
                writer = csv.DictWriter(
                    f2, fieldnames=['id', 'nome', 'prezo', 'stock'])
                writer.writeheader()
                for fila in reader:
                    if int(fila['stock']) < 5:
                        writer.writerow(fila)


if __name__ == "__main__":
    g = Gestion_inventario()
    print(g.calculo_valor_total())
    g.bajo_stock()
