"""
Descarga da páxina de euroestat os datos en formato csv da táboa que mostra esta url. Facer o programa que permita extraer a seguinte información sobre o consumo de enerxía renovable:
A produción total de enerxía renovable por país no período nos que están tomados os datos.
A produción de enerxía renovable dun país nun ano especificado.
Pais con maior crecemento porcentual dende o primeiro ano da estatística ata o último.
Pais con maior produción de enerxía renovable nun ano especificado.
O programa ofrecerá un menú coas opcións, os períodos, países e anos se introducirán por teclado é o resultado se mostrará por pantalla.


"""
import csv


class energia_renovable:
    def leer_csv_eurostat(self):
        datos = []
        with open("eurostat.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)  # salta cabecera
            for fila in reader:
                datos.append(fila)
        return datos

    def total_por_pais(self, datos):
        totales = {}
        for fila in datos:
            if fila[13]:
                pais = fila[10]
                valor = float(fila[13])
                totales[pais] = totales.get(pais, 0) + valor
        for pais, total in totales.items():
            print(f"{pais}: {total:.2f}%")

    def produccion_pais_ano(self, datos, pais, ano):
        for fila in datos:
            if fila[10] == pais and fila[11] == ano:
                if fila[13]:
                    print(f"{pais} en {ano}: {fila[13]}%")

    def lista_pais_crecimiento_anual(self, datos):
        valores = {}
        for fila in datos:
            if fila[13]:
                pais = fila[10]
                valor = float(fila[13])
                if pais not in valores:  # Verifica la existencia del pais
                    # Si es la primera vez que aparece guarda el ultimo y primer valor como iguales
                    valores[pais] = [valor, valor]
                else:
                    # Si no actualiza solo el segundo elemento
                    valores[pais][1] = valor

        mejor_pais = None
        mejor_crec = None
        # Desempaquetar el dict en primero - ultimo crecimiento
        for pais, (primero, ultimo) in valores.items():
            crecimiento = ((ultimo - primero)/primero) * \
                100  # Calcula crecimiento porcentual
            # Comprueba si es la primera vez que se evalua o si supera al mejor actual
            if mejor_crec is None or crecimiento > mejor_crec:
                mejor_crec = crecimiento  # Actualiza el mejor crecimiento
                mejor_pais = pais  # Guarda el pais de mejor crecimiento
        print(f"{mejor_pais}: {mejor_crec:.2f}%")

    def pais_mejor_prod_ano(self, datos, ano):
        mejor_pais = None
        mejor_valor = None
        for fila in datos:
            if fila[11] == ano and fila[13]:
                pais = fila[10]
                valor = float(fila[13])
                if mejor_valor is None or valor > mejor_valor:
                    pass
