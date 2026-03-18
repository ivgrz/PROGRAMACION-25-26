"""
Descarga da páxina de euroestat os datos en formato tsv (tab separated values) da táboa que mostra esta url. Tratade este formato como un ficheiro de texto, con tabulacións como separadores. Facer o programa que permita extraer a seguinte información sobre a porcentaxe de traballadores IT sobre o total:
Mostrar os 5 países que teñen a porcentaxe de maior porcentaxe empregabilidade nun ano determinado.
Mostrar o país con maior variación entre dous anos dados.
Dado un país, mostrar a diferencia de porcentaxe, con respecto a España nun período comprendido entre dous anos dados.
Agrupando en períodos de 4 anos, facer unha gráfica con separadores de forma que mostre a porcentaxe deses anos visualmente dun país solicitado. Exemplo
España
04/08	|||||||||				3%
08/12	||||||||||||||			4%
12/16	|||||||||||||||||			5%
16/20	||||||||||||||||||||||			7%
20|24	|||||||||||||||||||||||||		9%

"""


class Energia_renovable_2:
    def __init__(self):
        self.datos = {}  # {pais: {ano: valor}}
        self.anos = []

    def leer_tsv(self, ficheiro):
        with open(ficheiro, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        cabecera = lineas[0].strip().split("\t")
        # La primera celda es "dim1,dim2,...,geo\TIME_PERIOD", el resto son años
        for i in range(1, len(cabecera)):
            self.anos.append(cabecera[i].strip())

        for linea in lineas[1:]:
            partes = linea.strip().split("\t")
            if len(partes) < 2:
                continue
            # El país es el último valor de la primera columna (separada por comas)
            dims = partes[0].split(",")
            pais = dims[-1].strip()
            self.datos[pais] = {}

            for i in range(1, len(partes)):
                if i - 1 >= len(self.anos):
                    break
                ano = self.anos[i - 1]
                # Eurostat añade flags como "3.1 b" o "4.2 p", quedamos solo con el número
                valor_str = partes[i].strip().split(" ")[0]
                try:
                    self.datos[pais][ano] = float(valor_str)
                except ValueError:
                    pass

    def top5_pais_ano(self, ano):
        # Guardamos (pais, valor) en una lista y buscamos los 5 mayores
        resultados = []
        for pais in self.datos:
            if ano in self.datos[pais]:
                resultados.append([pais, self.datos[pais][ano]])

        # Ordenamos de mayor a menor con burbuja simple
        for i in range(len(resultados)):
            for j in range(i + 1, len(resultados)):
                if resultados[j][1] > resultados[i][1]:
                    resultados[i], resultados[j] = resultados[j], resultados[i]

        print(f"\nTop 5 países en {ano}:")
        for i in range(min(5, len(resultados))):
            print(f"  {resultados[i][0]}: {resultados[i][1]:.2f}%")

    def pais_maior_variacion(self, ano1, ano2):
        mejor_pais = None
        mejor_var = 0

        for pais in self.datos:
            if ano1 in self.datos[pais] and ano2 in self.datos[pais]:
                var = abs(self.datos[pais][ano2] - self.datos[pais][ano1])
                if var > mejor_var:
                    mejor_var = var
                    mejor_pais = pais

        if mejor_pais:
            print(f"\nPaís con maior variación entre {ano1} e {ano2}: {mejor_pais} ({mejor_var:.2f}%)")
        else:
            print("Non se atoparon datos para ese período.")

    def diferencia_con_espana(self, pais, ano1, ano2):
        if "ES" not in self.datos:
            print("Non hai datos de España (ES).")
            return
        if pais not in self.datos:
            print(f"Non hai datos para o país {pais}.")
            return

        print(f"\nDiferencia de {pais} con respecto a España ({ano1}-{ano2}):")
        for ano in self.anos:
            if ano1 <= ano <= ano2:
                if ano in self.datos[pais] and ano in self.datos["ES"]:
                    dif = self.datos[pais][ano] - self.datos["ES"][ano]
                    print(f"  {ano}: {dif:+.2f}%")

    def grafica_periodos(self, pais):
        if pais not in self.datos:
            print(f"Non hai datos para o país {pais}.")
            return

        # Recogemos los años numéricos disponibles para ese país
        anos_disponibles = []
        for ano in self.anos:
            if ano.isdigit() and ano in self.datos[pais]:
                anos_disponibles.append(int(ano))

        if not anos_disponibles:
            print("Non hai datos numéricos para ese país.")
            return

        inicio = (anos_disponibles[0] // 4) * 4
        fin = anos_disponibles[-1]

        print(f"\n{pais}")
        periodo = inicio
        while periodo < fin:
            periodo_fin = periodo + 4

            # Calculamos la media del período
            suma = 0
            cuenta = 0
            for ano in range(periodo, periodo_fin):
                ano_str = str(ano)
                if ano_str in self.datos[pais]:
                    suma += self.datos[pais][ano_str]
                    cuenta += 1

            if cuenta > 0:
                media = suma / cuenta
                barras = "|" * int(media * 3)
                etiqueta = f"{str(periodo)[2:]}/{str(periodo_fin)[2:]}"
                print(f"{etiqueta}\t{barras}\t\t{media:.0f}%")

            periodo = periodo_fin


if __name__ == "__main__":
    er = Energia_renovable_2()
    ficheiro = input("Nome do ficheiro TSV (por defecto: eurostat_it.tsv): ").strip()
    if not ficheiro:
        ficheiro = "eurostat_it.tsv"
    er.leer_tsv(ficheiro)

    opcion = ""
    while opcion != "5":
        print("\n--- Menú Traballadores IT ---")
        print("1. Top 5 países nun ano determinado")
        print("2. País con maior variación entre dous anos")
        print("3. Diferencia con España nun período")
        print("4. Gráfica por períodos de 4 anos dun país")
        print("5. Saír")
        opcion = input("Escolle unha opción: ").strip()

        match opcion:
            case "1":
                ano = input("Introduce o ano: ").strip()
                er.top5_pais_ano(ano)
            case "2":
                ano1 = input("Introduce o primeiro ano: ").strip()
                ano2 = input("Introduce o segundo ano: ").strip()
                er.pais_maior_variacion(ano1, ano2)
            case "3":
                pais = input("Introduce o código do país (ex: DE, FR): ").strip().upper()
                ano1 = input("Ano de inicio: ").strip()
                ano2 = input("Ano de fin: ").strip()
                er.diferencia_con_espana(pais, ano1, ano2)
            case "4":
                pais = input("Introduce o código do país (ex: ES, DE): ").strip().upper()
                er.grafica_periodos(pais)
            case "5":
                print("Ata logo!")
            case _:
                print("Opción non válida.")
